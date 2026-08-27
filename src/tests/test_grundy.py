from grundy_engine.grundy import grundy
from grundy_engine.nim import nim_moves

def test_grundy():
    for n in range(20):
        assert grundy(n, nim_moves) == n