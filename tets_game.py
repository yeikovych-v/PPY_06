import json
import pytest
from game import TicTacToe

# Test for checking correct number of players
def test_correct_num_players():
    num_players = 2
    player_names = ['Player 1', 'Player 2']
    grid_size = 5
    game = TicTacToe(num_players, player_names, grid_size)
    assert game.num_players == num_players


# Test for checking incorrect number of players
def test_incorrect_num_players():
    num_players = 1  # Incorrect number of players (less than 2)
    player_names = ['Player 1']
    grid_size = 5
    with pytest.raises(ValueError):
        TicTacToe(num_players, player_names, grid_size)


# Test for checking correct size of the game board
def test_correct_grid_size():
    num_players = 2
    player_names = ['Player 1', 'Player 2']
    grid_size = 5
    game = TicTacToe(num_players, player_names, grid_size)
    assert len(game.board) == grid_size
    assert len(game.board[0]) == grid_size


# Test for checking incorrect size of the game board
def test_incorrect_grid_size():
    num_players = 2
    player_names = ['Player 1', 'Player 2']
    grid_size = 3  # Incorrect size of the game board (less than 5)
    with pytest.raises(ValueError):
        TicTacToe(num_players, player_names, grid_size)


# Test for checking correct syntax of the game-init.json file
def test_correct_game_init_json():
    # Load game-init.json
    with open('game-init.json', 'r') as file:
        game_init_data = json.load(file)
    num_players = game_init_data['num_players']
    player_names = game_init_data['player_names']
    grid_size = game_init_data['grid_size']
    player_symbols = game_init_data.get('player_symbols')

    # Check if player names match the list of names assigned to symbols
    if player_symbols:
        assert set(player_names) == set(player_symbols.keys())

    # Additional checks can be added as needed


# Test for checking correct initialization of player symbols
def test_correct_player_symbols_initialization():
    num_players = 2
    player_names = ['Player 1', 'Player 2']
    grid_size = 5
    player_symbols = {'Player 1': '#', 'Player 2': '$'}  # Manually defined player symbols
    game = TicTacToe(num_players, player_names, grid_size, player_symbols)
    assert game.player_symbols == player_symbols


# Test for checking default initialization of player symbols
def test_default_player_symbols_initialization():
    num_players = 2
    player_names = ['Player 1', 'Player 2']
    grid_size = 5
    game = TicTacToe(num_players, player_names, grid_size)
    assert all(symbol in game.symbols for symbol in game.player_symbols.values())


# Test for checking correct symbol assignment to players
def test_correct_symbol_assignment():
    num_players = 3
    player_names = ['Player 1', 'Player 2', 'Player 3']
    grid_size = 5
    game = TicTacToe(num_players, player_names, grid_size)
    assert len(set(game.player_symbols.values())) == num_players  # Each player should have a unique symbol


# Test for checking player switch after making a move
def test_player_switch_after_move():
    num_players = 2
    player_names = ['Player 1', 'Player 2']
    grid_size = 5
    game = TicTacToe(num_players, player_names, grid_size)
    current_player = game.current_player
    game.make_move(0, 0)  # Make a move
    assert game.current_player != current_player  # Player should switch after making a move


# Test for checking correct decrement of moves left after each move
def test_moves_left_decrement():
    num_players = 2
    player_names = ['Player 1', 'Player 2']
    grid_size = 5
    game = TicTacToe(num_players, player_names, grid_size)
    initial_moves_left = game.moves_left
    game.make_move(0, 0)  # Make a move
    assert game.moves_left == initial_moves_left - 1  # Moves left should decrement after each move
