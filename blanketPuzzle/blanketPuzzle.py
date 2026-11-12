# Problem Statement
#A seamstress is making a patchwork blanket from knitted squares of two colours, red and orange, forming a rectangular pattern. She has already sewn eight rows of seven squares each. Row A has its red squares in columns 1, 2, 4, 6 & 7; B has 2, 3, 6 & 7; C has 3, 4, 5 & 7; D has 1, 2, 3 & 5; E has 1, 2, 3, 5 & 6; F has 1, 3, 4 & 7; G has 2, 4, 6 & 7; H has 4, 5 & 6. All other squares are orange.

#She wants to assemble the rows (without reversing any left to right) into a rectangle, but choosing the order so that each column has exactly one run of exactly three consecutive reds, with all other reds having no red neighbours in the column, and with more reds in the top half than in the bottom half.

from itertools import permutations

rows = {'A':[1,2,4,6,7], 'B':[2,3,6,7], 'C':[3,4,5,7], 'D':[1,2,3,5],
        'E':[1,2,3,5,6], 'F':[1,3,4,7], 'G':[2,4,6,7], 'H':[4,5,6]}

sols = []
# Generating all permutations of a set in Python involves creating every possible ordered arrangement of its elements
for p in permutations(rows):
    print ("-- New Permutation -- ")
    for u in p:
        print(u)
        print(rows[u])
    ok = True
    for c in range(1, 8):
        # [col is a list of binary [FALSE, FALSE, TRUE, TRUE, FALSE, FALSE, TRUE, TRUE] etc for each column
        # r contains A, B, C, D, E, F, G, H
        # c in rows[r] meaning, say. rows['A'], checks if C from 1 to 7 is present in rows[r]
        col = [c in rows[r] for r in p]
        print ("col = {} ".format(col))
        runs = []; n = 0
        # print ("Col + [False] = {}".format(col + [False]))
        # col + [False] - adds a extra False at the end of the list, to ensure we capture the last value
        for v in col + [False]:
            if v: n += 1  # if encountered a TRUE, add to n
            elif n: runs.append(n); n = 0 # if encountered a FALSE and previous was TRUE, append to list. Set n=0, so the flag is reset
            print("runs = {}".format(runs)) # For 'HGFEDCBA' this is first column is [3,1], second column  is [1,2,2]
            # Column rule: a column passes only if it has exactly one run of 3 and every other run is 1 long. 
            # That means no runs of 2 and none of 4 or more.
            ''' 
            (1, 3) is a tuple, a fixed list of the two allowed run lengths.

            x not in (1, 3) is a membership test. It gives True when x is neither 1 nor 3. 
            not in is a single operator and means the same as not (x in (1, 3)).

            ... for x in runs is a generator expression. It works through each number in runs and produces one True/False result for each. 
            It produces them one at a time when asked, rather than building a full list first. 
            Inside a function call, the call's own brackets also serve as the generator's brackets, so you don't need a second pair.

            any(...) returns True as soon as one of those results is True. 
            Otherwise it returns False. It stops at the first True, so the rest of the runs aren't checked.

            Equivalent Code 
            found_bad = False
            for x in runs:
                if x not in (1, 3):
                    found_bad = True
                    break
            '''
        if sorted(runs).count(3) != 1 or any(x not in (1, 3) for x in runs):
            ok = False; break
    if not ok: continue
    top = sum(len(rows[r]) for r in p[:4])
    bot = sum(len(rows[r]) for r in p[4:])
    sols.append((''.join(p), top, bot))

for s in sols: print(s)
