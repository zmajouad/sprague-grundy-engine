import matplotlib.pyplot as plt

# Dawson's Chess

sequence = [0, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 0, 5, 2, 2, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 2, 7, 4, 0, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 2, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 3, 7, 4, 8, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 9, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 3, 7, 4, 8, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 9]
period_start = 52

heap_sizes = list(range(len(sequence)))

plt.figure(figsize=(12, 5))
plt.plot(heap_sizes, sequence, linewidth=1)
plt.axvspan(period_start, len(sequence), alpha=0.15, color='green', label=f'Periodic region (from n={period_start})')
plt.xlabel("Heap size (n)")
plt.ylabel("Grundy value")
plt.title("Dawson's Chess (0.137) — Grundy sequence")
plt.legend()
plt.savefig("results/dawsons_chess.png", dpi=150, bbox_inches='tight')
plt.show()


# Kayles

sequence = [0, 1, 2, 3, 1, 4, 3, 2, 1, 4, 2, 6, 4, 1, 2, 7, 1, 4, 3, 2, 1, 4, 6, 7, 4, 1, 2, 8, 5, 4, 7, 2, 1, 8, 6, 7, 4, 1, 2, 3, 1, 4, 7, 2, 1, 8, 2, 7, 4, 1, 2, 8, 1, 4, 7, 2, 1, 4, 2, 7, 4, 1, 2, 8, 1, 4, 7, 2, 1, 8, 6, 7, 4, 1, 2, 8, 1, 4, 7, 2, 1, 8, 2, 7, 4, 1, 2, 8, 1, 4, 7, 2, 1, 8, 2, 7]
period_start = 71

heap_sizes = list(range(len(sequence)))

plt.figure(figsize=(12, 5))
plt.plot(heap_sizes, sequence, linewidth=1)
plt.axvspan(period_start, len(sequence), alpha=0.15, color='green', label=f'Periodic region (from n={period_start})')
plt.xlabel("Heap size (n)")
plt.ylabel("Grundy value")
plt.title("Kayles (0.77) — Grundy sequence")
plt.legend()
plt.savefig("results/kayles.png", dpi=150, bbox_inches='tight')
plt.show()


# Dawson's Kayles

sequence = [0, 0, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 0, 5, 2, 2, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 2, 7, 4, 0, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 2, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 3, 7, 4, 8, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 9, 3, 3, 0, 1, 1, 3, 0, 2, 1, 1, 0, 4, 5, 3, 7, 4, 8, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 4, 5, 5, 9]
period_start = 53

heap_sizes = list(range(len(sequence)))

plt.figure(figsize=(12, 5))
plt.plot(heap_sizes, sequence, linewidth=1)
plt.axvspan(period_start, len(sequence), alpha=0.15, color='green', label=f'Periodic region (from n={period_start})')
plt.xlabel("Heap size (n)")
plt.ylabel("Grundy value")
plt.title("Dawson's Kayles (0.07) — Grundy sequence")
plt.legend()
plt.savefig("results/dawson_kayles.png", dpi=150, bbox_inches='tight')
plt.show()


# Treblecross

sequence = [0, 0, 0, 1, 1, 1, 2, 2, 0, 3, 3, 1, 1, 1, 0, 4, 3, 3, 3, 2, 2, 2, 4, 4, 0, 5, 5, 2, 2, 2, 3, 3, 0, 5, 0, 1, 1, 1, 3, 3, 3, 5, 6, 4, 4, 1, 0, 5, 5, 6, 6, 2, 7, 7, 7, 8, 0, 1, 9, 2, 7, 2, 3, 3, 3, 9, 0, 5, 4, 4, 8, 6, 6, 2, 7, 1, 1, 1, 0, 5, 5, 9, 3, 1, 8, 2, 8, 5, 0, 1, 1, 12, 2, 2, 7, 3, 3, 9, 4, 4, 0]

heap_sizes = list(range(len(sequence)))

plt.figure(figsize=(12, 5))
plt.plot(heap_sizes, sequence, linewidth=1)
plt.xlabel("Heap size (n)")
plt.ylabel("Grundy value")
plt.title("Treblecross (0.007) — Grundy sequence")
plt.legend()
plt.savefig("results/treblecross.png", dpi=150, bbox_inches='tight')
plt.show()