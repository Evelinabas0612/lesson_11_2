import json

from flask import app
from werkzeug.exceptions import abort


def load_candidates() -> list[dict]:
    '''загрузка кандидатов'''
    with open('candidates.json', 'r', encoding='utf-8') as file:
        new_file = json.load(file)
        file.close()
        return new_file


def get_candidate_by_id(candidate_id: int) -> dict:
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    app.logger.debug('Candidate does not found')
    abort(404)


def get_candidate_by_name(candidate_name) -> list[dict]:
    candidates = load_candidates()
    result = []
    candidate_name_lower = candidate_name.lower()
    for candidate in candidates:
        if candidate['name'].lower() == candidate_name_lower:
            result.append(candidate)
    if len(result) == 0:
        app.logger.debug('Position does not found')
        abort(404)
    return result


def get_candidate_by_skill(skill) -> list[dict]:
    candidates = load_candidates()
    result = []
    skill_lower = skill.lower()
    for candidate in candidates:
        if skill_lower in candidate['skills'].lower().split(', '):
            result.append(candidate)
    if len(result) == 0:
        app.logger.debug('Position does not found')
        abort(404)
    return result




