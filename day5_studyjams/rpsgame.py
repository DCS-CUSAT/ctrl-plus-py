import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def play_rps(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    # Update computer's choice label
    computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"
    
    # Show result in a popup
    messagebox.showinfo("Game Over", result)

# Create the main window
root = tk.Tk()
print("Tkinter window opened!")  # Debugging message to check if the window is being created
root.title("Rock, Paper, Scissors Game")

# Set window size and background color
root.geometry("400x400")
root.config(bg="#f0f8ff")

# Create title label
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 24, "bold"), bg="#f0f8ff")
title_label.pack(pady=20)

# Create a frame for the buttons
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=20)

# Button for rock
rock_button = tk.Button(frame, text="Rock", font=("Arial", 16), width=10, height=2, bg="#ff6347", fg="white", command=lambda: play_rps("rock"))
rock_button.grid(row=0, column=0, padx=10)

# Button for paper
paper_button = tk.Button(frame, text="Paper", font=("Arial", 16), width=10, height=2, bg="#4682b4", fg="white", command=lambda: play_rps("paper"))
paper_button.grid(row=0, column=1, padx=10)

# Button for scissors
scissors_button = tk.Button(frame, text="Scissors", font=("Arial", 16), width=10, height=2, bg="#32cd32", fg="white", command=lambda: play_rps("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Label for computer's choice
computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 14), bg="#f0f8ff")
computer_choice_label.pack(pady=20)

# Run the main event loop
print("Starting Tkinter mainloop...")  # Debugging message before mainloop
root.mainloop()
