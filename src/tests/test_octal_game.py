from grundy_engine.octal_game import decode_digit

def test_decode_digit_all():
    flags = decode_digit(7)
    assert flags == {"take_all": True, "reduce": True, "split": True}
    
def test_decode_digit_take_all():
    flags = decode_digit(1)
    assert flags == {"take_all": True, "reduce": False, "split": False}

def test_decode_digit_none():
    flags = decode_digit(0)
    assert flags == {"take_all": False, "reduce": False, "split": False}