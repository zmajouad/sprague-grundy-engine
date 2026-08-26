from grundy_engine.nim import nim_moves

def test_nim_moves_heap_3():
    assert set(nim_moves(4)) == {0, 1, 2, 3}

def test_nim_moves_heap_0():
    assert set(nim_moves(0)) == set()