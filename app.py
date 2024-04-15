from flask import Flask, render_template, request, jsonify
from game import TicTacToe
import json

app = Flask(__name__)

# Function to read game initialization data from game-init.json
def read_game_init():
    with open('game-init.json', 'r') as file:
        game_init_data = json.load(file)
    return game_init_data

# Read game initialization data
game_init_data = read_game_init()
num_players = game_init_data['num_players']
player_names = game_init_data['player_names']
grid_size = game_init_data['grid_size']
player_symbols = game_init_data.get('player_symbols', None)  # Get player symbols from game-init.json, if available
game = TicTacToe(num_players, player_names, grid_size, player_symbols)  # Initialize the game with player symbols

@app.route('/')
def index():
    return render_template('index.html', grid_size=grid_size, current_player=game.current_player, player_symbols=game.player_symbols)

@app.route('/make_move', methods=['POST'])
def make_move():
    global game
    if not game:
        return jsonify({'error': 'Game has not been initialized.'}), 500

    data = request.json
    row = data['row']
    col = data['col']
    result, winner, winning_cells = game.make_move(row, col)  # Include winning_cells in the response
    return jsonify({'result': result, 'winner': winner, 'winning_cells': winning_cells, 'current_player': game.current_player})

if __name__ == '__main__':
    app.run(debug=True)