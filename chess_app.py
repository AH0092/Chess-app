import chess
import streamlit as st
from chess.svg import board as svg_board

# Function to initialize the board
@st.cache_data(allow_output_mutation=True)
def initialize_board():
    return chess.Board()

# Main function for the Streamlit app
def main():
    st.title("Interactive Chess Game")
    st.write("Play a chess game in your browser! Enter moves in algebraic notation (e.g., e2e4).")

    # Initialize the chess board
    board = initialize_board()

    # Display the chess board
    st.subheader("Chess Board")
    st.image(svg_board(board), use_column_width=True)

    # Input move from the user
    if not board.is_game_over():
        move = st.text_input("Enter your move (e.g., e2e4):")

        if move:
            try:
                chess_move = chess.Move.from_uci(move.strip())
                if chess_move in board.legal_moves:
                    board.push(chess_move)
                    st.experimental_rerun()
                else:
                    st.error("Illegal move. Please try again.")
            except ValueError:
                st.error("Invalid move format. Use UCI notation (e.g., e2e4).")

    # Game outcome
    if board.is_game_over():
        if board.is_checkmate():
            st.success("Checkmate! Game over.")
        elif board.is_stalemate():
            st.info("Stalemate. Game over.")
        elif board.is_insufficient_material():
            st.info("Draw due to insufficient material. Game over.")
        elif board.is_seventyfive_moves():
            st.info("Draw due to the 75-move rule. Game over.")
        elif board.is_fivefold_repetition():
            st.info("Draw due to fivefold repetition. Game over.")

if __name__ == "__main__":
    main()


