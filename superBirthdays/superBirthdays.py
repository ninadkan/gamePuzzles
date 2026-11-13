'''
Generations Jay, Kay, Elle and Em

Polygonian newborns are allocated a regular polygon talisman for the day of 
the month they are born (1st = triangle, 2nd = square to 31st  = 33-agon). 
Super-auspicious birth dates occur when the talisman’s internal angle is a 
whole number of degrees and the month number (Jan = 1 to Dec = 12) divides 
into it exactly and the year is a multiple of it.

Polygonians, Em, her mam Elle, Elle’s mam Kay and Kay’s dad Jay dined out 
on Jay’s birthday in 2024. Chef said, “Congratulations, you’re looking fit Jay. 
You’ll live to 100.” Elle stated they all had super-auspicious birth dates 
and her 2024 birthday was in the month after next. Em added that she and Kay 
had their 2024 birthdays in the month before last. 
Chef then deduced their birth dates with certainty.
Give Em’s birth date

'''
import pandas as pd
dateRange = list(range(1,32)) 
validMonthValues = list(range(1,13)) 
yearOfBirths = list(range(1924,2024))  


validDates = []
for date in dateRange:
    # relationship between date and number of sides = date = n-2, 
    # formula for an angle of a polynomial = (n-2)*180/(n), substituting for date, we get,
    # angle = (date*180)/(date+2)
    angle = (date*180)/(date+2)
    if ((date*180) % (date+2)) == 0: #angle is a whole number, no fractions
        angle = int(angle)
        for month in validMonthValues: # we are only going to be selective
            if ((angle % month == 0) ): # month divides completely angle, no fractions
                for year in yearOfBirths:
                    if year % angle == 0:
                        validDates.append((year, month, date, angle))

sortedDates = sorted(validDates, key=lambda tup: (tup[0], tup[1], tup[2]))
colNames = ["Year", "Month","Date","Angle"]
dfValidDates = pd.DataFrame(sortedDates, columns=colNames)
print(dfValidDates.to_string(index=False))
print("Len of valid dates found = {}".format(len(sortedDates)))

# Following code borrowed from CoWork
MIN_GAP = 13                             # youngest plausible parent age

from collections import defaultdict
from itertools import product

sols = []
'''
product(dates, repeat=4): This function takes your list or tuple of dates and generates 
all possible sequences of length 4. 
Because it allows repeats, the same date can appear multiple times in a single sequence.


from itertools import product

dates = ["Jan 1", "Jan 2"]

for jay, kay, elle, em in product(dates, repeat=4):
    print(jay, kay, elle, em)


Jan 1 Jan 1 Jan 1 Jan 1
Jan 1 Jan 1 Jan 1 Jan 2
Jan 1 Jan 1 Jan 2 Jan 1
... (13 more combinations) ...
Jan 2 Jan 2 Jan 2 Jan 2


'''
for jay, kay, elle, em in product(sortedDates, repeat=4):
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

#df = pd.DataFrame(data, columns=colNames)
#print(df.to_string(index=False))
