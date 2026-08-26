from grundy_engine.mex import mex

def test_mex_with_gap():
    assert mex({0, 1, 3}) == 2

def test_mex_empty():
    assert mex(set()) == 0

def test_mex_missing_zero():
    assert mex({1, 2, 3}) == 0

def test_mex_unordered_input():
    assert mex({4, 0, 2, 1}) == 3

def test_mex_no_gaps():
    assert mex({0, 1, 2}) == 3