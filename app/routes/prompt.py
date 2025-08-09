"""Prompt相关的接口定义"""
from flask import Blueprint, request, jsonify
from app.database import db
from app.models.prompt import Prompt, PromptVersion

# 创建Blueprint以组织路由
prompt_bp = Blueprint("prompt", __name__)


@prompt_bp.route("/prompts", methods=["POST"])
def create_prompt():
    """创建新的Prompt并保存初始版本"""
    data = request.get_json() or {}
    title = data.get("title", "")
    content = data.get("content", "")
    tags = data.get("tags", "")

    # 保存Prompt基本信息
    prompt = Prompt(title=title, content=content, tags=tags)
    db.session.add(prompt)
    db.session.flush()  # 先写入以获得ID

    # 保存版本信息，版本号从1开始
    version = PromptVersion(prompt_id=prompt.id, content=content, version=1)
    db.session.add(version)
    db.session.commit()

    return jsonify({"id": prompt.id}), 201


@prompt_bp.route("/prompts", methods=["GET"])
def list_prompts():
    """列出所有Prompt"""
    prompts = Prompt.query.all()
    result = [
        {"id": p.id, "title": p.title, "tags": p.tags, "content": p.content}
        for p in prompts
    ]
    return jsonify(result)


@prompt_bp.route("/prompts/<int:prompt_id>", methods=["PUT"])
def update_prompt(prompt_id: int):
    """更新指定Prompt并记录新版本"""
    prompt = Prompt.query.get_or_404(prompt_id)
    data = request.get_json() or {}
    content = data.get("content", prompt.content)
    tags = data.get("tags", prompt.tags)

    prompt.content = content
    prompt.tags = tags

    # 新版本号为当前版本数量+1
    version_number = len(prompt.versions) + 1
    version = PromptVersion(prompt_id=prompt.id, content=content, version=version_number)
    db.session.add(version)
    db.session.commit()

    return jsonify({"id": prompt.id, "version": version_number})
