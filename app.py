import json
from game import TicTacToe

# Function to read game initialization data from game-init.json
def read_game_init():
    with open("game-init.json", "r") as file:
        game_init_data = json.load(file)
    return game_init_data

# Initialize the game
def initialize_game():
    game_init_data = read_game_init()
    num_players = game_init_data["num_players"]
    player_names = game_init_data["player_names"]
    grid_size = game_init_data["grid_size"]
    player_symbols = game_init_data.get("player_symbols", None)

    return TicTacToe(num_players, player_names, grid_size, player_symbols)

# Function to print the game board
def print_board(board):
    for row in board:
        print(row)

# Function to handle player moves
def handle_player_move(game):
    while True:
        try:
            x = int(input("Enter row: "))
            y = int(input("Enter column: "))
            result, winner, winning_cells = game.make_move(x, y)

            if result == "success":
                print_board(game.board)
            elif result == "win":
                print(f"Congratulations {game.current_player} won!")
                return False  # End the game
            elif result == "draw":
                print("It's a draw!")
                return False  # End the game
            elif result == "occupied":
                print("The cell is occupied.")
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")
            continue

# Main function to run the game
def main():
    game = initialize_game()
    print("Let's start Tic Tac Toe!")
    print_board(game.board)

    while True:
        if not handle_player_move(game):
            break

if __name__ == "__main__":
    main()
