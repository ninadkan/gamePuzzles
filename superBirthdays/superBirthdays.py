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
Jay_Month_Valid_Values = list(range(3,13)) # +2 for Elle, -2 for Em, Kay
Year_Of_Births = list(range(1924,2024))  


validDates = []

for date in dateRange:
    # relationship between date and number of sides = date = n-2, 
    # formula for an angle of a polynomial = (n-2)*180/(n), substituting for date, we get,
    # angle = (date*180)/(date+2)
    angle = (date*180)/(date+2)
    if ((date*180) % (date+2)) == 0: #angle is a whole number, no fractions
        for month in Jay_Month_Valid_Values: # we are only going to be selective
            if ((angle % month == 0) and (angle % (month-2) == 0) and (angle % (month+2) == 0)): # month divides completely angle, no fractions
                for year in Year_Of_Births:
                    if year % angle == 0:
                        validDates.append((date, month, month-2, month+2, year, round(angle,2)))
    
sortedDates = sorted(validDates, key=lambda tup: (tup[4], tup[1], tup[0]))
colNames = ["Date", "Month","Month minus-2","add+2","Year","Angle"]

dfValidDates = pd.DataFrame(sortedDates, columns=colNames)
print(dfValidDates.to_string(index=False))



#df = pd.DataFrame(data, columns=colNames)
#print(df.to_string(index=False))
