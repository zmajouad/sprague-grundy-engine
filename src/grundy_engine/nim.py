def nim_moves(heap_size):
    possible = []
    for i in range(heap_size-1, -1, -1):
        possible.append(i)
    return possible