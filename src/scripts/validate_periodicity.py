import time

from grundy_engine.grundy import grundy
from grundy_engine.octal_game import octal_moves, generate_decoded_digits
from grundy_engine.periodicity import find_periodicity

# Dawson's Chess
print("Dawson's Chess (0.137)")
decoded = generate_decoded_digits("0.137") #  code for Dawson's Chess
moves_fn = lambda pos: octal_moves(pos, decoded) # creates one-line lambda function which takes pos as an input and returns octal_moves(pos, decoded)
sequence = []
cache = {}
start_time = time.time()

# This loop takes about 1 hour, the sequence it creates it listed below, commented

for n in range(120):    
    sequence.append(grundy((n,), moves_fn, cache)) # Creates a sequence the exact length needed to detect periodicity
    print(n)

# sequence = [0, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 0, 5, 2, 2, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 2, 7, 4, 0, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 2, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 3, 7, 4, 8, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 9, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 3, 7, 4, 8, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 9]

print(sequence)
print(f"Grundy sequence took {time.time() - start_time:.2f}s")

result = find_periodicity(sequence)
print(f"Periodic: {result["is_periodic"]}\n",
      f"Start: {result["start"]}\n",
      f"Period: {result["period"]}")


# Kayles
print("\nKayles (0.77)")
decoded = generate_decoded_digits("0.77") #  code for Dawson's Chess
moves_fn = lambda pos: octal_moves(pos, decoded) # creates one-line lambda function which takes pos as an input and returns octal_moves(pos, decoded)
sequence = []
cache = {}
start_time = time.time()

# This loop takes about 3 hours, the sequence it creates it listed below, commented

for n in range(96):    
    sequence.append(grundy((n,), moves_fn, cache)) # Creates a sequence the exact length needed to detect periodicity
    
# sequence = [0, 1, 2, 3, 1, 4, 3, 2, 1, 4, 2, 6, 4, 1, 2, 7, 1, 4, 3, 2, 1, 4, 6, 7, 4, 1, 2, 8, 5, 4, 7, 2, 1, 8, 6, 7, 4, 1, 2, 3, 1, 4, 7, 2, 1, 8, 2, 7, 4, 1, 2, 8, 1, 4, 7, 2, 1, 4, 2, 7, 4, 1, 2, 8, 1, 4, 7, 2, 1, 8, 6, 7, 4, 1, 2, 8, 1, 4, 7, 2, 1, 8, 2, 7, 4, 1, 2, 8, 1, 4, 7, 2, 1, 8, 2, 7]

print(sequence)
print(f"Grundy sequence took {time.time() - start_time:.2f}s")

result = find_periodicity(sequence)
print(f"Periodic: {result["is_periodic"]}\n",
      f"Start: {result["start"]}\n",
      f"Period: {result["period"]}")
