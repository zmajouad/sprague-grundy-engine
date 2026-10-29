from grundy_engine.mex import mex
from grundy_engine.octal_game import  generate_decoded_digits

def octal_sequence(code, N):
    decoded = generate_decoded_digits(code)
    G = [0]
    for heap_size in range(1, N+1):
        options = []
        for i in range(1, min(len(decoded), heap_size+1)): # i is the amount to remove
            flags = decoded[i]
            if flags["take_all"] and i == heap_size: # if take_all is allowed and items being removed is the same as the heap size, add value = 0 as an option
                 options.append(0)
            if flags["reduce"] and i < heap_size: # if reducing is allowed and items being removed is less than the heap size, leave one smaller heap of size heap_size - i, whose value is G[n - i]
                options.append(G[heap_size-i])
            if flags["split"] and heap_size-i >= 2: # if splitting is allowed, and removing i leaves 2 or more, it can be split into 2 positive heaps
                remaining = heap_size - i
                for a in range(1, (remaining//2)+1):
                    options.append(G[a] ^ G[remaining - a]) # XOR combines the values of the 2 heaps that can exist so mex only has to work with one heap
        G.append(mex(options))
    return G
