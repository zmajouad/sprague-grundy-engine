from grundy_engine.sequence import octal_sequence
from grundy_engine.grundy import grundy
from grundy_engine.nim import nim_moves
from grundy_engine.octal_game import generate_decoded_digits, octal_moves

def generate_v1_sequences(code, length):
    decoded = generate_decoded_digits(code)
    moves_fn = lambda pos: octal_moves(pos, decoded) # creates one-line lambda function which takes pos as an input and returns octal_moves(pos, decoded)
    sequence = []
    for n in range(length+1):
        sequence.append(grundy((n,), moves_fn))
    return sequence

def test_nim_sequence_matches_v1():
    nim_code = "0." + "3" * 20
    assert octal_sequence(nim_code, 14) == generate_v1_sequences(nim_code, 14)

def test_dawsons_chess_sequence_matches_v1():
    assert octal_sequence("0.137", 11) == generate_v1_sequences("0.137", 11)

def test_kayles_sequence_matches_v1():
    assert octal_sequence("0.77", 11) == generate_v1_sequences("0.77", 11) 

def test_dawsons_kayles_sequence_matches_v1():
    assert octal_sequence("0.07", 11) == generate_v1_sequences("0.07", 11)

def test_treblecross_sequence_matches_v1():
    assert octal_sequence("0.007", 11) == generate_v1_sequences("0.007", 11)
