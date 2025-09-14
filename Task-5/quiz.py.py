import requests
import time

def fetch_question():
    url = 'https://opentdb.com/api.php?amount=1&type=multiple'
    response = requests.get(url)
    data = response.json()
    if data['response_code'] != 0:
        return None
    q = data['results'][0]
    question = q['question']
    correct = q['correct_answer']
    options = q['incorrect_answers'] + [correct]
    # Shuffle options
    import random
    random.shuffle(options)
    return question, options, correct

def quiz():
    score = 0
    total = 3  # total questions
    print("Welcome to Simple Quiz! You have 15 seconds to answer each question.\n")
    for i in range(total):
        q_data = fetch_question()
        if not q_data:
            print("Failed to fetch question. Try again later.")
            break
        question, options, correct = q_data
        print(f"Q{i+1}: {question}")
        for idx, opt in enumerate(options, 1):
            print(f"{idx}. {opt}")
        start_time = time.time()
        answer = input("Your answer (enter number): ")
        elapsed = time.time() - start_time

        if elapsed > 15:
            print("Time's up! No points.\n")
            continue

        if not answer.isdigit() or int(answer) < 1 or int(answer) > len(options):
            print("Invalid input! No points.\n")
            continue

        chosen = options[int(answer)-1]

        if chosen == correct:
            print("Correct! +1 point\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {correct}\n")

    print(f"Quiz Over! Your score: {score}/{total}")

if __name__ == "__main__":
    quiz()
