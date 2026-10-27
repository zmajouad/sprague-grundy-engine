# Sprague–Grundy Engine

I built this in Python to compute Grundy values for impartial games, starting with Nim and going up to octal games like Kayles and Dawson's Chess. Then I wrote a detector that looks for periodicity in the sequences I generated and checked everything I could against published results.

It was my first proper Git project, so the history is meant to show how it was built step by step, bugs included.

## What's in the project

- `src/grundy_engine/mex.py`: the mex function
- `src/grundy_engine/grundy.py`: one  `grundy(position, moves, cache)` that works for any game, because the game rules are passed in
- `src/grundy_engine/nim.py`: moves for a single Nim heap (used as a sanity check, G(n) = n)
- `src/grundy_engine/octal_game.py`: reads an octal code like `"0.137"` and generates every legal move
- `src/grundy_engine/periodicity.py`: finds the smallest period and the earliest start
- `scripts/validate_periodicity.py`: computes the sequences and runs the detector
- `scripts/plot_results.py`: draws the plots in `results/`
- `tests/`: 30 pytest tests

## How it works

**Grundy values.** The value of a position is the mex of the values of the positions you can move to. A position with no moves has value 0. `grundy()` does this recursively and caches every result.

**Octal codes.** Each digit after the point says what is allowed when you remove that many tokens. I read the digit as three bits: 1 means you can take the whole heap, 2 means you can leave one smaller heap, and 4 means you can leave two heaps. So `7` allows all three. Dawson's Chess is `0.137`, Kayles is `0.77`.

**Positions.** A position is a tuple of heap sizes. After every move I sort the tuple and drop empty heaps, so `(2, 1)` and `(1, 2)` count as the same position and share one cache entry. A split generates every pair (a, b) with a + b equal to what is left, each pair once.

## Bugs I hit and fixed

- **`mex` gave wrong answers.** My first version looped over a set and compared each item to a counter. Sets have no guaranteed order, so it broke. I changed it to `while lowest in integers`. A test with unordered input now catches this.
- **Mutable default cache.** `cache={}` as a default argument is created once and shared between every call. I used `cache=None` and made a new dict inside the function.
- **Wrong value cached.** My first memoised version stored an intermediate value inside the loop. It now stores the final mex once, after the loop.
- **Range off by one.** I ran Dawson's Chess with `range(119)`, which stops at n = 118. The detector found nothing because it was one term short of two full periods. With the missing last term it found the period.
- **False period at n = 64 for Treblecross.** The detector said period 1 because the last three values happened to be equal. Running to n = 100 removed it.
- **Slow runs.** Computing each term with a new cache was very slow. Sharing one cache across the whole loop fixed most of that.

## The theory

**Sprague–Grundy.** In a finite game where both players have the same moves and the last player to move wins, every position has a Grundy value, and a position with value g plays like a Nim heap of size g. Value 0 means the player to move loses.

if the value is 0, none of the positions you can move to has value 0, so every move gives your opponent a nonzero position. From a nonzero position the opponent can always move back to a 0. Eventually you run out of moves. If the value is nonzero, a 0 position is reachable, so you move there and win.

**Why XOR.** If you play several games at once, each turn you move in just one of them. Each game acts like a Nim heap of its Grundy value, so the combined game acts like ordinary Nim. Nim is lost for the player that is going to move exactly when the XOR of the heap sizes is 0. So the Grundy value of the combined game is the XOR of the separate values. This means I can solve each game on its own and combine the answers, without searching the whole combined game tree.

I tested this on Dawson's Chess: the value of a two-heap position computed by mex over the whole tree equals the XOR of the two single-heap values.

## Results

| Game | Code | Period | Pre-period (my detector) | Published | Checked against |
|---|---|---|---|---|---|
| Dawson's Chess | 0.137 | 34 | 52 | 51, with n = 51 listed as an exception | OEIS A002187 |
| Kayles | 0.77 | 12 | 71 | 70 or 71, depending on the source | OEIS A002186 |
| Dawson's Kayles | 0.07 | 34 | 53 | follows from the shift below | Dawson's Chess |
| Treblecross | 0.007 | none found up to n = 100 | n/a | open problem | n/a |

For Kayles the sources disagree between 70 and 71. My result of 71 agrees with the source that states 71.

Plots are in `results/`, with the periodic region shaded green.

## What I did

- **Validated:** Dawson's Chess and Kayles match their OEIS sequences. Nim gives G(n) = n. The XOR rule holds on my test cases. The detector finds the right period on both real games and on hand-made sequences.
- **Dawson's Kayles is not independent.** The literature says Dawson's Kayles at size n+1 equals Dawson's Chess at size n. I computed it directly only to about n = 89, and it matched that rule term for term. The longer sequence in my tests is `[0] + dawsons_chess`, so its period comes from Dawson's Chess, not from a separate run.
- **Treblecross is not validated.** I did not compare it to a published table. Its periodicity is a known open problem. Finding no period up to n = 100 does not show it is aperiodic. It only means I did not find one in that range.
- **Largest heap computed from scratch:** n = 118 (Dawson's Chess). The last term in my stored Dawson's Chess sequence comes from the published values.
- **The detector is weak near the end of a sequence.** It only needs one repeat of data after the start. The false period at n = 64 came from that. A longer sequence is stronger evidence.
- **Runtime.** Split-heavy games get expensive fast. Dawson's Chess took about an hour to reach n = 119 and one run used over 16 GB of RAM. Kayles took about three hours to reach about n = 95. A Dawson's Kayles run was taking about 1000 seconds per term by n = 109 when I stopped it. The tests use stored sequences, so they run in seconds.

## Running it

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
pytest
```

`scripts/validate_periodicity.py` recomputes everything from scratch and takes hours. The finished sequences are stored as comments in that file and as lists in the tests.

## Licence

MIT