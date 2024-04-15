import json
import os
from game import TicTacToe
import keyboard

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
def print_grid(board, cursor_row, cursor_col):
    rows, cols = len(board), len(board[0])
    os.system('cls' if os.name == 'nt' else 'clear')
    cell_width = 5

    for r in range(rows):
        for c in range(cols):
            print('+' + '-' * cell_width, end='')
        print('+')

        for c in range(cols):
            if r == cursor_row and c == cursor_col:
                content = f'[ {board[r][c]} ]'
            else:
                content = f' {board[r][c]} '

            print(f'|{content:^{cell_width}}', end='')

        print('|')

    for c in range(cols):
        print('+' + '-' * cell_width, end='')
    print('+')

    # Display instructions at the bottom
    print("\nUse arrow keys to move, 'enter' to place your symbol, and 'q' to quit the game.")

# Function to handle player moves
def handle_player_move(game, cursor_row, cursor_col, update_needed):
    print_grid(game.board, cursor_row, cursor_col)
    while True:
        event = keyboard.read_event(suppress=True)

        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'up':
                cursor_row = max(0, cursor_row - 1)
                update_needed = True
            elif event.name == 'down':
                cursor_row = min(game.grid_size - 1, cursor_row + 1)
                update_needed = True
            elif event.name == 'left':
                cursor_col = max(0, cursor_col - 1)
                update_needed = True
            elif event.name == 'right':
                cursor_col = min(game.grid_size - 1, cursor_col + 1)
                update_needed = True
            elif event.name == 'q':
                update_needed = True
                print('Exiting....')
                exit()
            elif event.name == 'enter':
                result, winner, winning_cells = game.make_move(cursor_row, cursor_col)
                if result == "success":
                    return True
                elif result == "win":
                    print_grid(game.board, cursor_row, cursor_col)
                    print(f"Congratulations {game.current_player} won!")
                    return False  # End the game
                elif result == "draw":
                    print_grid(game.board, cursor_row, cursor_col)
                    print("It's a draw!")
                    return False  # End the game
                elif result == "occupied":
                    print("The cell is occupied.")

        if update_needed:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_grid(game.board, cursor_row, cursor_col)
            update_needed = False

# Main func
def main():

    game = initialize_game()
    cursor_row, cursor_col = 0, 0
    update_needed = True


    while True:
        if not handle_player_move(game, cursor_row, cursor_col, update_needed):
            break

if __name__ == "__main__":
    main()
