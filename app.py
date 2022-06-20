from flask import Flask, render_template

from utils import load_candidates, get_candidate_by_id, get_candidate_by_name, get_candidate_by_skill

app = Flask(__name__)


@app.route('/')
def all_candidates():
    candidates: list[dict] = load_candidates()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:uid>')
def candidate_person_card(uid):
    candidate: dict = get_candidate_by_id(uid)
    if not candidate:
        return "Кандидат не найден"
    return render_template('card.html', candidate=candidate)

@app.route('/search/<name>')
def candidate_search_name(name):
    candidates: list[dict] = get_candidate_by_name(name)
    return render_template('search.html', candidates=candidates)

@app.route('/skill/<position>')
def candidate_search_position(position):
    candidates: list[dict] = get_candidate_by_skill(position)
    return render_template('skill.html', skill=position, candidates=candidates)

app.run()

