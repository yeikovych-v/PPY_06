from game import TicTacToe
import json


# Function to read game initialization data from game-init.json
def read_game_init():
    global game_init_data
    with open('game-init.json', 'r') as file:
        game_init_data = json.load(file)
    return game_init_data


# Read game initialization data
game_in_progress = True
game_init_data = read_game_init()
num_players = game_init_data['num_players']
player_names = game_init_data['player_names']
grid_size = game_init_data['grid_size']
player_symbols = game_init_data.get('player_symbols', None)  # Get player symbols from game-init.json, if available
game = TicTacToe(num_players, player_names, grid_size, player_symbols)  # Initialize the game with player symbols


# @app.route('/')
# def index():
#     return render_template('index.html', grid_size=grid_size, current_player=game.current_player,
#                            player_symbols=game.player_symbols)


def print_grid(grid):
    for row in grid:
        print(row)


def make_move():
    global game, game_in_progress

    input_x = input("row: ")
    input_y = input("col: ")
    x = int(input_x)
    y = int(input_y)
    result, winner, winning_cells = game.make_move(x, y)  # Include winning_cells in the response
    if result == 'success':
        print_grid(game.board)
    if result == 'win':
        print(f"Congratulations Player {game.current_player} won!")
        game_in_progress = False
    if result == 'draw':
        print(f"Congratulations Its draw!")
        game_in_progress = False


while game_in_progress:
    make_move()
