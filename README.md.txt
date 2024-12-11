Interactive Chess Game

This project is a web-based chess application built with Streamlit and the python-chess library. It allows players to enjoy a chess game in their browser with an interactive interface.

Features

Interactive Chess Board: Displays the current state of the chess game.

Move Validation: Ensures all moves are valid according to chess rules.

Game End Conditions: Detects checkmate, stalemate, and other game-ending conditions.

Web-Based: No installation required beyond basic Python libraries.

Setup Instructions

Prerequisites

Ensure you have Python 3.8 or later installed on your system.

Steps to Run

Clone the Repository:

git clone https://github.com/your-username/chess-app.git
cd chess-app

Install Dependencies:
Use the provided requirements.txt to install necessary libraries.

pip install streamlit python-chess cairosvg

Run the App:
Start the Streamlit server to launch the app.

streamlit run chess_app.py

Open in Browser:
Once the server starts, Streamlit will provide a local URL (e.g., http://localhost:8501). Open it in your browser to play the game.

How to Play

Enter moves in UCI notation (e.g., e2e4 for moving a pawn from e2 to e4).

The app validates the move and updates the board.

The game ends with a checkmate, stalemate, or other official chess rule conditions.

Project Structure

chess_app.py: Main Python script for the Streamlit application.

README.md: Documentation for the project.

.gitignore: Specifies files to be ignored by Git.

Requirements

Python 3.8 or higher

Libraries: streamlit, python-chess, cairosvg

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the app.

Steps to Contribute

Fork the repository.

Create a new branch for your feature/bug fix.

Submit a pull request describing your changes.

License

This project is open-source and available under the MIT License.