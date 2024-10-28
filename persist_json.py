import json
import os
import quiz

def load(qobject):

    try:
        quiz_name = f"{qobject.name}.json"
        path = os.path.join("data", quiz_name)
        with open(path, "r") as data_file:
            data = json.load(data_file)
        keys = ("question", "correct_answer", "incorrect_answers")
        for questions in data:
            qobject.add(questions.get(keys[0]), questions.get(keys[1]), questions.get(keys[2]))
        return qobject

    except IOError:
        raise IOError(f"{qobject.name}.json not found")

def store(qobject):

    try:
        quiz_name = f"{qobject.name}.json"
        path = os.path.join("data", quiz_name)
        if os.path.exists(path):
            raise FileExistsError(f"Quiz {quiz_name} file already exists")
        quiz_store = [
            {"question": q.question, "correct_answer": q.correct_answer, "incorrect_answers": q.incorrect_answers}
            for q in qobject]
        with open(path, "w") as file:
            json.dump(quiz_store, file)
    except Exception:
        raise IOError(f"Quiz {qobject.name}.json already exists")


def destroy(quiz_name):

    path = os.path.join("data", f"{quiz_name}.json")
    if os.path.isfile(path):
        os.remove(path)
    else:
        raise IOError(f"quiz {quiz_name} was never saved")


