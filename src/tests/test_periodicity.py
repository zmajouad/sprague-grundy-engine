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
    
def test_find_periodicity_dawsons_chess():
    # In the published papers, the sequence has  period 34 with the only exceptions at n=0, 14, 16, 17, 31, 34 and 51.
    # This would translate to period 34 and start 52 in our one.
    sequence = [0, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 0, 5, 2, 2, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 2, 7, 4, 0, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 2, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 3, 7, 4, 8, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 9, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 3, 7, 4, 8, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 9]
    result = find_periodicity(sequence)
    assert result == {"is_periodic": True, "start": 52, "period": 34}
    
def test_find_periodicity_kayles():
    # In the published statement, it says:
    # From n=71 on, the sequence is periodic with period 12. The only exceptions are n=0, 3, 6, 9, 11, 15, 18, 21, 22, 28, 34, 39, 57 and 70.
    sequence = [0, 1, 2, 3, 1, 4, 3, 2, 1, 4, 2, 6, 4, 1, 2, 7, 1, 4, 3, 2, 1, 4, 6, 7, 4, 1, 2, 8, 5, 4, 7, 2, 1, 8, 6, 7, 4, 1, 2, 3, 1, 4, 7, 2, 1, 8, 2, 7, 4, 1, 2, 8, 1, 4, 7, 2, 1, 4, 2, 7, 4, 1, 2, 8, 1, 4, 7, 2, 1, 8, 6, 7, 4, 1, 2, 8, 1, 4, 7, 2, 1, 8, 2, 7, 4, 1, 2, 8, 1, 4, 7, 2, 1, 8, 2, 7]
    result = find_periodicity(sequence)
    assert result == {"is_periodic": True, "start": 71, "period": 12}
    
def test_find_periodicity_dawson_kayles():
    # In the published statement, it says:
    # Octal game .07 (Dawson's Kayles) has values a(n-1), so it is the same sequence as Dawson's Chess with a 0 at the beginning and shifted up by 1
    sequence = [0, 0, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 0, 5, 2, 2, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 2, 7, 4, 0, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 2, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 3, 7, 4, 8, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 9, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 3, 7, 4, 8, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 9]
    result = find_periodicity(sequence)
    assert result == {"is_periodic": True, "start": 53, "period": 34}