from grundy_engine.grundy import grundy
from grundy_engine.nim import nim_moves
from grundy_engine.octal_game import generate_decoded_digits, octal_moves

def test_grundy():
    for n in range(20):
        assert grundy(n, nim_moves) == n
        
def test_kayles_grundy_sequence():
    decoded = generate_decoded_digits("0.137")
    moves_fn = lambda pos: octal_moves(pos, decoded) # creates one-line lambda function which takes pos as an input and returns octal_moves(pos, decoded)
    sequence = []
    for n in range(12):
        sequence.append(grundy((n,), moves_fn))
    # compare against Dawson's Chess published sequence online: https://oeis.org/A002187
    assert sequence == [0, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2]