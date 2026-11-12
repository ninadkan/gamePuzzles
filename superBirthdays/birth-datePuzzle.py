from collections import defaultdict
from itertools import product

# Super-auspicious dates: day d -> polygon with d+2 sides
def super_dates(y_lo, y_hi):
    out = []
    for d in range(1, 32):
        n = d + 2
        if 360 % n:                      # interior angle 180 - 360/n must be whole
            continue
        ang = 180 - 360 // n
        for m in range(1, 13):
            if ang % m:                  # month must divide the angle
                continue
            for y in range(y_lo, y_hi + 1):
                if y % ang == 0:         # year must be a multiple of the angle
                    out.append((y, m, d, ang))
    return out

MIN_GAP = 13                             # youngest plausible parent age
dates = super_dates(1925, 2024)          # Jay under 100 on his 2024 birthday

sols = []
for jay, kay, elle, em in product(dates, repeat=4):
    J = jay[1]
    # Kay & Em: month before last; Elle: month after next
    if not (kay[1] == em[1] == J - 2 and elle[1] == J + 2):
        continue
    if not (kay[0] - jay[0] >= MIN_GAP and elle[0] - kay[0] >= MIN_GAP
            and em[0] - elle[0] >= MIN_GAP):
        continue
    sols.append((jay, kay, elle, em))

print("All consistent families:")
for s in sols:
    print("  ", [f"{d:02d}/{m:02d}/{y} ({a}°)" for y, m, d, a in s])

# Chef knows the dinner date = Jay's birthday (day, month)
by_dinner = defaultdict(list)
for s in sols:
    by_dinner[(s[0][2], s[0][1])].append(s)

print("\nDinner dates where the chef can be certain:")
for (d, m), group in sorted(by_dinner.items(), key=lambda kv: kv[0][::-1]):
    if len(group) == 1:
        jay, kay, elle, em = group[0]
        print(f"  Dinner {d:02d}/{m:02d}/2024 -> Jay {jay[2]:02d}/{jay[1]:02d}/{jay[0]}, "
              f"Kay {kay[2]:02d}/{kay[1]:02d}/{kay[0]}, Elle {elle[2]:02d}/{elle[1]:02d}/{elle[0]}, "
              f"Em {em[2]:02d}/{em[1]:02d}/{em[0]}")
    else:
        print(f"  Dinner {d:02d}/{m:02d}/2024 -> ambiguous ({len(group)} families)")
