from flask import Blueprint, jsonify, request, abort

bp = Blueprint('prompts', __name__, url_prefix='/prompts')

_prompts = {}
_next_id = 1


def _get_next_id():
    global _next_id
    pid = _next_id
    _next_id += 1
    return pid


@bp.get('')
def list_prompts():
    return jsonify(list(_prompts.values()))


@bp.post('')
def create_prompt():
    data = request.get_json() or {}
    title = data.get('title')
    content = data.get('content')
    if not title or not content:
        abort(400, 'title and content required')
    pid = _get_next_id()
    prompt = {'id': pid, 'title': title, 'content': content}
    _prompts[pid] = prompt
    return jsonify(prompt), 201


@bp.put('/<int:pid>')
def edit_prompt(pid):
    if pid not in _prompts:
        abort(404)
    data = request.get_json() or {}
    title = data.get('title')
    content = data.get('content')
    if not title or not content:
        abort(400, 'title and content required')
    prompt = {'id': pid, 'title': title, 'content': content}
    _prompts[pid] = prompt
    return jsonify(prompt)
