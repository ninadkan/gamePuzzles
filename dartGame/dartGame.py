TARGET = 501

# ---------- Build the combined list (same as before) ----------
numbers = list(range(1, 21))
doubled = [n * 2 for n in numbers]
tripled = [n * 3 for n in numbers]

combined = sorted(set(numbers + doubled + tripled))
for value in (25, 50):
    if value not in combined:
        combined.append(value)

doubled_set = set(doubled)
marked = [(value, value in doubled_set) for value in combined]
marked.sort(key=lambda item: item[0], reverse=True)

print("Combined list (* = in the multiplied-by-2 list):")
print([f"{v}*" if m else str(v) for v, m in marked])
print()

# ---------- Helpers ----------
def digits(n):
    return set(str(n))

def subset_sums(values, limit):
    """All totals (up to limit) that can be made from a subset of values."""
    sums = {0}
    for v in values:
        sums |= {s + v for s in sums if s + v <= limit}
    return sums

def can_still_finish(gap, remaining):
    """Can the gap still be closed exactly, with a marked value as the last addition?"""
    for i, (m, is_marked) in enumerate(remaining):
        if is_marked and m <= gap:
            others = [v for j, (v, _) in enumerate(remaining) if j != i]
            if gap - m in subset_sums(others, gap - m):
                return True
    return False

def pick(available, banned_digits, total, first_move):
    """Choose the next value:
       1. first move must be the highest allowed marked value
       2. never use a digit from the opponent's previous move
       3. take a winning move (a marked value landing exactly on TARGET) if there is one
       4. otherwise take the highest value that stays below TARGET and still
          leaves a way to finish exactly on TARGET with a marked value
    """
    allowed = [(v, m) for v, m in available if digits(v).isdisjoint(banned_digits)]
    if first_move:
        allowed = [(v, m) for v, m in allowed if m]

    for value, is_marked in allowed:                       # winning move
        if is_marked and total + value == TARGET:
            return value, is_marked

    for value, is_marked in allowed:                       # highest safe move
        if total + value >= TARGET:
            continue
        remaining = [item for item in available if item != (value, is_marked)]
        if can_still_finish(TARGET - total - value, remaining):
            return value, is_marked
    return None

# ---------- Game ----------
available = list(marked)                                    # values still free to use
players = ["Beth", "Amy"]
totals = {p: 0 for p in players}
picks = {p: [] for p in players}
last_move = {p: None for p in players}                      # each player's previous value
winner = None
turn = 0
passes_in_a_row = 0

while winner is None:
    player = players[turn % 2]
    opponent = players[(turn + 1) % 2]
    turn += 1

    banned = digits(last_move[opponent]) if last_move[opponent] is not None else set()
    choice = pick(available, banned, totals[player], first_move=not picks[player])

    if choice is None:
        print(f"{player:<5} has no valid number - passes")
        passes_in_a_row += 1
        if passes_in_a_row == 2:
            print("Neither player can move - game over.")
            break
        continue

    passes_in_a_row = 0
    available.remove(choice)
    value, is_marked = choice
    totals[player] += value
    picks[player].append(value)
    last_move[player] = value
    print(f"{player:<5} takes {value:>2}{'*' if is_marked else ' '}  "
          f"(banned digits {sorted(banned) or '-'})  total = {totals[player]}")

    if totals[player] == TARGET:
        winner = player

print()
for p in players:
    print(f"{p:<5}: {picks[p]}  -> total {totals[p]}")
print()

if winner:
    loser = players[1] if winner == players[0] else players[0]
    print(f"{winner} wins, landing exactly on {TARGET} with the marked value {last_move[winner]}.")
    print(f"Sum of the losing player ({loser}): {totals[loser]}")
else:
    print(f"Nobody landed exactly on {TARGET}.")
