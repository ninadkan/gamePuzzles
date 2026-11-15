'''
Teaser 3345
Locked Together

Our sports centre has lockers numbered from 100 to 400. 
My locker number is a multiple of three. 
If you list all the three-figure numbers that use the same digits as my 
locker number, then you find that they are all the sum of two primes and 
two-thirds of them are the difference of two squares.

My wife’s locker number is one less than mine. If you  list all the 
three-figure numbers that use the same digits as her locker number, 
then her list also has those two properties.

What is my locker number?
'''

def isPrime(n):
    prime = True
    for i in range(2, n-1):
        if (n % i == 0):
            prime = False
            break
    return prime

lstAllPrimeNumbers = [ x for x in range(2,1000) if (isPrime(x))]


condition = lambda x: ((x> 99) and (x < 1000))

lstSumOfAllPrimeNumbers = []

for idx, p  in enumerate(lstAllPrimeNumbers):
    for idxy, q in enumerate(lstAllPrimeNumbers, start=idx+1):
        sumPrime = p+q
        if condition(sumPrime):
            lstSumOfAllPrimeNumbers.append(p+q)

# drop duplicates
lstSumOfAllPrimeNumbers = list(set(lstSumOfAllPrimeNumbers))
print("Sum of all primes = {}".format(lstSumOfAllPrimeNumbers))

lstAllSquares = [x**2 for x in range(1, 400)]

lstDiffOfAllSquares = []
for idx,p in (enumerate(lstAllSquares)):
    for idxy, q in enumerate(lstAllSquares, start=idx+1):
        # Difference of two squares need to be in 3 digits. 
        # so it needs to be greater than 99 and less than 1000
        diff = abs(q-p)
        if condition(diff):
            lstDiffOfAllSquares.append(diff)

# drop duplicates
lstDiffOfAllSquares = list(set(lstDiffOfAllSquares))
print("Difference of all squares = {}".format(lstDiffOfAllSquares))

'''
function digits(n)
given a number, returns a list containing all the digits that form that number
'''
def digits(n):
    digitsArray = [] # reset
    digitsArray = [int(x) for x in str(n)] # cannot use the set as it
                                            # does not honour order
    return digitsArray

def areConditionsSatisfied(m):
    rv = False

    lkDigits = digits(m)
    # the three combinations are
    allCombinations =   [100*lkDigits[0] + 10*lkDigits[1]+ lkDigits[2], 
                         100*lkDigits[0] + 10*lkDigits[2]+ lkDigits[1],
                         100*lkDigits[1] + 10*lkDigits[0]+ lkDigits[2],
                         100*lkDigits[1] + 10*lkDigits[2]+ lkDigits[0],
                         100*lkDigits[2] + 10*lkDigits[0]+ lkDigits[1],
                         100*lkDigits[2] + 10*lkDigits[1]+ lkDigits[0]]
    #print(allCombinations)
    allTrueCombinations = [x for x in allCombinations if condition(x)]
    #dropDuplicates
    allTrueCombinations = list(set(allTrueCombinations))

    print("Digits = {}, All Combinations = {}".format(lkDigits,allTrueCombinations))

    noOfCombinations = len(allTrueCombinations)
    twoThirdOfCombinations = round(2*noOfCombinations/3,0)
    match = True
    for item in allTrueCombinations:
        primeMatchCount = 0
        squareMatchCount = 0
        if item in lstSumOfAllPrimeNumbers:
            primeMatchCount += 1
        else:
            match = False
            break

        if match and item in lstDiffOfAllSquares:
            squareMatchCount += 1
        else:
            match = False
            break

    if match:
       if noOfCombinations == primeMatchCount :
           if twoThirdOfCombinations == squareMatchCount :
               # EUREKA
               print("Solution Found = {}".format(m))
               rv = True
    return rv
            
        

lockerNumbers = [x for x in list(range(100, 401))]
for m in lockerNumbers:  # m represents wife's locker number
    if (areConditionsSatisfied(m) and areConditionsSatisfied(m+1)):
        if (m+1) % 3 == 0: # husband # is divisible by 3
            print("The Final Solution is {}, {}".format(m, m+1))
    

