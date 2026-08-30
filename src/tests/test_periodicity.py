from grundy_engine.periodicity import is_periodic_from, find_periodicity

def test_is_periodic_from_index_zero():
    sequence = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    assert is_periodic_from(sequence, 0, 3) == True

def test_is_periodic_from_index_zero_false():
    sequence = [0, 1, 2, 0, 1, 2, 0, 1, 3]
    assert is_periodic_from(sequence, 0, 3) == False
    
def test_find_periodicity_true():
    sequence = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    assert find_periodicity(sequence) == {"is_periodic": True, "start": 0, "period": 3}

def test_find_periodicity_returns_min_period():
    sequence = [0, 1, 2] * 5
    result = find_periodicity(sequence)
    assert result["period"] == 3

def test_find_periodicity_one_repeat():
    sequence = [1, 2, 3, 4, 1, 2, 3, 4]
    result = find_periodicity(sequence)
    assert result == {"is_periodic": True, "start": 0, "period": 4}
    
def test_find_periodicity_non_periodic():
    sequence = [1, 5, 7, 6, 2, 3, 1, 3]
    result = find_periodicity(sequence)
    assert result == {"is_periodic": False, "start": None, "period": None}