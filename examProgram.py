import json
import random

# Load the JSON file
with open('answers.json', 'r', encoding='utf-8') as file:
    quiz_data = json.load(file)

# Access the questions
questions = quiz_data['questions']

# Shuffle the order of the questions
random.shuffle(questions)

# Define how many questions the user will be tested on
num_questions = int(input("How many questions would you like to be tested on? "))

# Ensure the number of questions doesn't exceed the total available
num_questions = min(num_questions, len(questions))

# Initialize score tracking
correct_answers = 0

# Loop through the selected number of questions
for i in range(num_questions):
    question = questions[i]
    print(f"Question: {question['question_text']}")
    for choice in question['choices']:
        print(choice)
    
    # Get the user's answer
    user_answer = input("Your answer: ").lower()

    # Check if the answer is correct
    if user_answer == question['correct_answer'].lower():
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect. The correct answer is {question['correct_answer']}.")

    print()  # Print a blank line between questions

# Display final score
print(f"\nYour final score: {correct_answers} out of {num_questions}")
