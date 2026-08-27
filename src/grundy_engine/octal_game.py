def decode_digit(n):
    return {
        "take_all": bool(n & 1),
            "reduce": bool(n & 2),
            "split": bool(n & 4),
    }
    
def generate_decoded_digits(code):
    str_code = str(code)
    decoded_digits = [None]
    for c in range (2, len(code)):
        decoded_digits.append(decode_digit(int(str_code[c])))
    return decoded_digits    
    


def octal_moves(position, decoded_digits):
    moves = []
    for n in range(len(position)): # n is index of heap in tuple        
        heap_size = position[n]
        for i in range(1, heap_size+1):
            if i < len(decoded_digits):
                flags = decoded_digits[i]
                if flags["take_all"] and i == heap_size: # if take_all is allowed and items being removed is the same as the heap size, remove that heap from tuple
                    new_pos = list(position)
                    new_pos.pop(n)
                    moves.append(tuple(sorted(new_pos)))
                if flags["reduce"] and i < heap_size: # if reducing is allowed and items being removed is less than the heap size, change the heap_size at the position by the amount being removed
                    new_pos = list(position)
                    new_pos[n] = heap_size-i
                    moves.append(tuple(sorted(new_pos)))
                if flags["split"] and heap_size-i >= 2: # if splitting is allowed, and removing i leaves 2 or more, it can be split into 2 positive heaps
                    a = heap_size-i-1
                    b = 1
                    while a >= 1 and a >= b:
                        new_pos = list(position)
                        new_pos[n] = a
                        new_pos.append(b)
                        moves.append(tuple(sorted(new_pos)))
                        a -= 1
                        b += 1    
    return moves
