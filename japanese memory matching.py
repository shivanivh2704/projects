import tkinter as tk
import random
import pygame

# Initialize Pygame
pygame.init()

# Hiragana and Katakana data
hiragana_questions = [
    {"type": "Hiragana", "question": "あ", "options": ["a", "i", "u", "e"], "answer": "a"},
    {"type": "Hiragana", "question": "い", "options": ["i", "e", "o", "a"], "answer": "i"},
    {"type": "Hiragana", "question": "う", "options": ["u", "o", "i", "e"], "answer": "u"},
    {"type": "Hiragana", "question": "え", "options": ["e", "a", "i", "u"], "answer": "e"},
    {"type": "Hiragana", "question": "お", "options": ["o", "e", "a", "u"], "answer": "o"},
    {"type": "Hiragana", "question": "か", "options": ["ka", "ki", "ku", "ke"], "answer": "ka"},
    {"type": "Hiragana", "question": "き", "options": ["ki", "ka", "ku", "ko"], "answer": "ki"},
    {"type": "Hiragana", "question": "く", "options": ["ku", "ka", "ki", "ko"], "answer": "ku"},
    {"type": "Hiragana", "question": "け", "options": ["ke", "ka", "ki", "ku"], "answer": "ke"},
    {"type": "Hiragana", "question": "こ", "options": ["ko", "ka", "ki", "ku"], "answer": "ko"},
    # Add more Hiragana characters as needed
]

katakana_questions = [
    {"type": "Katakana", "question": "ア", "options": ["a", "i", "u", "e"], "answer": "a"},
    {"type": "Katakana", "question": "イ", "options": ["i", "e", "o", "a"], "answer": "i"},
    {"type": "Katakana", "question": "ウ", "options": ["u", "o", "i", "e"], "answer": "u"},
    {"type": "Katakana", "question": "エ", "options": ["e", "a", "i", "u"], "answer": "e"},
    {"type": "Katakana", "question": "オ", "options": ["o", "e", "a", "u"], "answer": "o"},
    {"type": "Katakana", "question": "カ", "options": ["ka", "ki", "ku", "ke"], "answer": "ka"},
    {"type": "Katakana", "question": "キ", "options": ["ki", "ka", "ku", "ko"], "answer": "ki"},
    {"type": "Katakana", "question": "ク", "options": ["ku", "ka", "ki", "ko"], "answer": "ku"},
    {"type": "Katakana", "question": "ケ", "options": ["ke", "ka", "ki", "ku"], "answer": "ke"},
    {"type": "Katakana", "question": "コ", "options": ["ko", "ka", "ki", "ku"], "answer": "ko"},
    # Add more Katakana characters as needed
]

# Combine Hiragana and Katakana questions
questions = hiragana_questions + katakana_questions

# Function to display next question
def next_question():
    global current_question, score, questions_shuffled
    if current_question < len(questions_shuffled):
        question_data = questions_shuffled[current_question]
        question_label.config(text=question_data["question"])
        type_label.config(text=f"Type: {question_data['type']}")
        for i, option in enumerate(question_data["options"]):
            option_buttons[i].config(text=option, state=tk.NORMAL, bg=random.choice(button_colors))
    else:
        question_label.config(text=f"Game Over! Your score: {score}")
        type_label.config(text="")
        for button in option_buttons:
            button.config(state=tk.DISABLED)
        retry_button.config(state=tk.NORMAL)

# Function to check the answer
def check_answer(selected_option):
    global current_question, score
    if questions_shuffled[current_question]["options"][selected_option] == questions_shuffled[current_question]["answer"]:
        score += 1
    current_question += 1
    next_question()

# Function to restart the game
def restart_game():
    global current_question, score, questions_shuffled
    current_question = 0
    score = 0
    questions_shuffled = random.sample(questions, len(questions))
    next_question()
    retry_button.config(state=tk.DISABLED)

# Initialize Tkinter window
root = tk.Tk()
root.title("Hiragana and Katakana Quiz")
root.attributes('-fullscreen', True)

# Create question label
question_label = tk.Label(root, text="", font=("Arial", 48))
question_label.pack(pady=20)

# Create type label
type_label = tk.Label(root, text="", font=("Arial", 24))
type_label.pack(pady=10)

# Create option buttons
button_colors = ["#FF9999", "#99FF99", "#9999FF", "#FFFF99"]
option_buttons = []
for i in range(4):
    button = tk.Button(root, text="", font=("Arial", 24), width=10, command=lambda i=i: check_answer(i))
    button.pack(pady=10)
    option_buttons.append(button)

# Create retry button
retry_button = tk.Button(root, text="Retry", font=("Arial", 24), command=restart_game)
retry_button.pack(pady=20)
retry_button.config(state=tk.DISABLED)

# Start the quiz
current_question = 0
