from flask import Flask, render_template, request
import requests
import html
import uuid
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    category = request.args.get('category')
    base_url = "https://opentdb.com/api.php?amount=5&type=multiple"
    if category:
        base_url += f"&category={category}"

    response = requests.get(base_url)
    data = response.json()

    questions = []
    question_mapping = {}

    q_counter = 0
    for item in data["results"]:
        question_text = html.unescape(item["question"])
        correct_answer = html.unescape(item["correct_answer"])
        incorrect_answers = [html.unescape(ans) for ans in item["incorrect_answers"]]

        options = incorrect_answers + [correct_answer]
        options = sorted(options, key=lambda x: uuid.uuid4())

        question = {
            "id": q_counter,
            "question": question_text,
            "options": options
        }

        questions.append(question)
        question_mapping[str(q_counter)] = {
            "correct": correct_answer,
            "options": options
        }

        q_counter += 1

    return render_template("quiz.html", questions=questions, mapping=question_mapping)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form
    selected_checkboxes = [key for key in form_data if key.startswith("checkbox_")]

    mapping = json.loads(form_data.get("mapping"))

    question_answers = {}
    for checkbox_id in selected_checkboxes:
        _, qid, option_index = checkbox_id.split("_")
        if qid not in question_answers:
            question_answers[qid] = []
        question_answers[qid].append(int(option_index))

    total = len(mapping)
    correct = 0
    feedback = []

    for qid, data in mapping.items():
        selected_indices = question_answers.get(qid, [])
        user_selected = [data["options"][i] for i in selected_indices] if selected_indices else []
        is_correct = len(user_selected) == 1 and user_selected[0] == data["correct"]
        if is_correct:
            correct += 1

        feedback.append({
            "question": data["options"],
            "options": data["options"],
            "selected": user_selected,
            "correct": data["correct"],
            "is_correct": is_correct
        })

    return render_template("result.html", total=total, correct=correct, feedback=feedback)


if __name__ == '__main__':
    app.run(debug=True)
