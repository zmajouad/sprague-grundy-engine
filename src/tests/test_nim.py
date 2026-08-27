from grundy_engine.nim import nim_moves

def test_nim_four():
    assert set(nim_moves(4)) == {0, 1, 2, 3}

def test_nim_zero():
    assert set(nim_moves(0)) == set()