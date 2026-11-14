'''

Puzzle:
Hidden PINs

Richard has opened a bank account. The bank has issued him with a telephone PIN
and a debit card PIN;
both are four-figure numbers. The telephone PIN is a perfect square; its 
square root can be obtained from the card PIN if the first two digits are 
deleted from the card PIN. The card PIN is composed of four different digits 
in decreasing order; none of these digits occur in the telephone PIN.

If I told you whether the telephone PIN has a repeat digit you would be able to find both PINs.

What is the debit card PIN?

'''

fourDigitValues = list(range(1000, 10000)) # 1000 to 9999

def digits(n):
    digitsArray = [] # reset
    digitsArray = [int(x) for x in str(n)] # cannot use the set as it 
                                            # does not honour order
    return digitsArray

def doesListContainCommonElements(lstA, lstB):
    rv = False
    bContinue = True
    for itemA in lstA:
        if bContinue :
            for itemB in lstB:
                if itemA == itemB :
                    rv = True
                    bContinue = False
                    break
        else:
            break
    return rv
    
validDigits = []
for dcPin in fourDigitValues:
    lstDigits = digits(dcPin)
    if (len(lstDigits)) == 4 : # we've got four unique numbers
        if (((lstDigits[0] ) > lstDigits[1]) and
            ((lstDigits[1] ) > lstDigits[2]) and
            ((lstDigits[2] ) > lstDigits[3])) :
                validDigits.append(lstDigits)



for val in validDigits:
    # Now remove the first two digits from the validDigits. 
    telPin = 10*val[2] + val[3]
    telPin = telPin ** 2 
    telPinList = digits(telPin)

    if (len(telPinList) == 4):
        # No digits in telPin can occur in val
        if (doesListContainCommonElements(val, telPinList) == False) : # Found our match
            print("Possible Matches Telphone PIN = {}, Card PIN = {}".format(telPin, val))

            # Simple Implementation
            # if (telPinList[0] == telPinList[1] or
            #    telPinList[1] == telPinList[2] or
            #    telPinList[2] == telPinList[3]) : # if common digits, set will remove digits

            pairs = zip(telPinList, telPinList[1:]) # create 3 pairs
            containsAdjacentSameDigits = [ x == y for x,y in pairs]
            if any(containsAdjacentSameDigits):
                print("Solution is  Telephone PIN = {}, Card PIN = {}".format(telPin, val))

        




