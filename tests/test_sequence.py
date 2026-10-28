from grundy_engine.sequence import octal_sequence
from grundy_engine.grundy import grundy
from grundy_engine.nim import nim_moves
from grundy_engine.octal_game import generate_decoded_digits, octal_moves

from pathlib import Path
DATA = Path(__file__).parent / "data"

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

def ttest_dawsons_chess_matches_oeis_a002187():
    terms = []
    with open(DATA / "a002187.txt") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            n, value = line.split()
            terms.append(int(value))
    assert octal_sequence("0.137", len(terms) - 1) == terms

def test_dawsons_chess_matches_oeis_a002186():
    terms = []
    with open(DATA / "a002186.txt") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            n, value = line.split()
            terms.append(int(value))
    assert octal_sequence("0.77", len(terms) - 1) == terms
