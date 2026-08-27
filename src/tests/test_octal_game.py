from grundy_engine.octal_game import decode_digit, octal_moves, generate_decoded_digits

def test_decode_digit_all():
    flags = decode_digit(7)
    assert flags == {"take_all": True, "reduce": True, "split": True}
    
def test_decode_digit_take_all():
    flags = decode_digit(1)
    assert flags == {"take_all": True, "reduce": False, "split": False}

def test_decode_digit_none():
    flags = decode_digit(0)
    assert flags == {"take_all": False, "reduce": False, "split": False}
    
def test_generate_decoded_digits_dawson():
    result = generate_decoded_digits("0.137")
    assert result[0] is None
    assert result[1] == {"take_all": True, "reduce": False, "split": False}
    assert result[2] == {"take_all": True, "reduce": True, "split": False}
    assert result[3] == {"take_all": True, "reduce": True, "split": True}
    
def test_generate_decoded_digits_one_digit():
    result = generate_decoded_digits("0.7")
    assert result[0] is None
    assert result[1] == {"take_all": True, "reduce": True, "split": True}

def test_octal_moves_take_all():
    decoded = [ # this would be 0.1
        None, # index 0 unused
        {"take_all": True, "reduce": False, "split": False} # when removing 1, can only take_all
    ]
    result = octal_moves((1,), decoded)
    assert set(result) == {()}

def test_octal_moves_reduce():
    decoded = [ # this would be 0.02
        None,                                                    # index 0 unused
        {"take_all": False, "reduce": False, "split": False},    # cannot remove 1 at all
        {"take_all": False, "reduce": True, "split": False},     # can only reduce when removing 2
    ]
    result = octal_moves((3,), decoded)
    assert set(result) == {(1,)}

def test_octal_moves_split():
    decoded = [ # this would be 0.4
            None,                                                    # index 0 unused
            {"take_all": False, "reduce": False, "split": True},     # when removing 1, can only split
        ]
    result = octal_moves((4,), decoded)
    assert set(result) == {(1, 2)}

def test_octal_moves_ignores_other_heaps():
    decoded = [None, {"take_all": True, "reduce": False, "split": False}]
    result = octal_moves((1, 2), decoded)
    assert set(result) == {(2,)}  # heap 0 (size 5) untouched since take_all needs i==5, only i=1..5 checked; think about this one yourself actually

    
'''
def test_octal_moves_leaves_other_heaps_untouched():
    # position (5, 2) - moving on heap 0 shouldn't affect heap 1
    decoded = [None, {"take_all": True, "reduce": False, "split": False}]
    result = octal_moves((5, 2), decoded)
    # every result tuple should still contain a "2" somewhere
'''