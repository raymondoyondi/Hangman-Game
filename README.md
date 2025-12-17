# Hangman Game 

## About The Project

Welcome to the **Hangman Game**, my first major project in Python! This is a classic command-line implementation of the beloved word-guessing game.

The project is designed with modularity in mind, making use of a dedicated Python package to encapsulate the game's core logic. This repository is a testament to applying fundamental programming concepts, including control flow, data structures, and object-oriented programming principles.

## ✨ Key Features

* **Classic Gameplay**: Enjoy the traditional Hangman experience right in your terminal.
* **Word Selection**: A secret word is randomly chosen from an internal list for a fresh challenge every time.
* **Limited Guesses**: Players are given a total of **7 chances** to guess the correct word.
* **Guess Tracking**: The game clearly displays the current progress of the hidden word and the letters that have already been guessed.
* **Modular Design**: The core game logic is neatly organized within a dedicated `hangman` package.

## 🛠️ Installation & Setup

To get this project running on your local machine, follow these simple steps:

### Prerequisites

You only need Python 3 installed on your system.

### Running the Game

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/raymondoyondi/Hangman-Game](https://github.com/raymondoyondi/Hangman-Game)
    ```
2.  **Navigate to the Project Directory:**
    ```bash
    cd Hangman-Game
    ```
3.  **Execute the Script:**
    (Assuming your main executable file is named `main.py` or similar)
    ```bash
    python <your_main_script_name>.py
    ```
    *The game will start immediately.*

## 🕹️ How to Play

The objective is to guess the secret word before you run out of attempts.

1.  **Start:** When the script runs, it will select a word and display a set of underscores (`_`), showing you exactly how many letters are in the secret word.
2.  **Guess a Letter:** You will be prompted to `Enter a letter:`. Type a single alphabet character and press Enter.
3.  **Feedback:**
    * **Correct Guess:** If the letter is in the word, it will be revealed in all its corresponding positions.
    * **Incorrect Guess:** Your remaining chances will be reduced by one. (You start with 7 chances).
4.  **Win/Loss:**
    * **You Win!** if you successfully guess all the letters in the word.
    * **Game Over!** if your remaining chances drop to zero.

## 📁 Project Structure

The project maintains a clean structure for readability and maintenance:

| File/Directory | Description |
| :--- | :--- |
| `hangman/` | **The core package** containing all game methods and logic. |
| `hangman/hangman.py` | Contains the core `Hangman` class, word list, and methods for game state, letter checking, and chance reduction. |
| `README.md` | This file. |

## 🌟 About the Developer

This project holds a special place as **my first Python project**. It was an exciting journey of learning and applying Python fundamentals to build a functional, interactive game. Any feedback, suggestions, or constructive criticism is highly welcome as I continue to grow my skills.

## 📝 License

This project is open-sourced under the MIT License. See the `LICENSE` file for more details (if a license file is included in your repository).
