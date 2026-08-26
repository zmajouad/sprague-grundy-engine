from grundy_engine.mex import mex

def grundy(position, moves, cache=None):
    if cache == None:
        cache = {}
    if position in cache:
        return cache[position]
    reachable = set()
    for next_pos in moves(position):
        g = (grundy(next_pos, moves, cache))
        reachable.add(g)
    m = mex(reachable)    
    cache[position] = m
    return m