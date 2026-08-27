def decode_digit(n):
    return {
        "take_all": bool(n & 1),
            "reduce": bool(n & 2),
            "split": bool(n & 4),
    }