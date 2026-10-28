import time
from grundy_engine.sequence import octal_sequence

start = time.time()
G = octal_sequence("0.137", 10000)
print(len(G), time.time() - start)

terms = []
with open("tests/data/a002186.txt") as f:
    for line in f:
        if line.startswith("#") or not line.strip():
            continue
        n, value = line.split()
        terms.append(int(value))

print(terms)
print(len(terms))