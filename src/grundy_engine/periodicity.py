def is_periodic_from(sequence, start, period):
    periodic = True
    n = start
    while n <= len(sequence)-period-1 and periodic == True:
        if sequence[n] != sequence[n + period]:
            periodic = False
            break
        n += 1
    return periodic

def find_periodicity(sequence):
    periodic = False
    period = 1
    starting_index = -1
    while periodic == False and starting_index + 2 * period <= len(sequence):
        starting_index +=1
        for p in range(1, len(sequence)//2+1):
            if starting_index + 2 * p <= len(sequence):
                if is_periodic_from(sequence, starting_index, p):
                    periodic = True
                    period = p
                    break        
    if periodic:
        return {
                "is_periodic": True,
                "start": starting_index,
                "period": period
            }
    else:
        return {
            "is_periodic": False,
            "start": None,
            "period": None
        }
    
