'''
Squaring Up
Farmer Giles had a square-shaped field, 
which he divided into nine paddocks by building four straight fences in 
symmetrical fashion, as shown in the diagram (not to scale). 
The fence from the SW corner meets the northern edge of the field a 
two-digit whole number of feet from the NW corner and a three-digit whole 
number of feet from the NE corner, these two numbers having no common factors.
The area of the central paddock divided by the area of the field was a 
fraction with a perfect square numerator and a perfect fourth power denominator.
'''


import math

a_values = list(range(10, 100))
b_values = list(range(100,1000))

# max number that we can get is 99*999 = 98091

squares = [x**2 for x in range(1000)]
quads = [x**4 for x in range(50)]

coprimes = []

for a in a_values:
    for b in b_values:
        if math.gcd(a,b) == 1: # common denominator is only 1
            # Area of middle paddlock = b*b/((a*a) + (a+b)**2)
            numerator = b*b
            # Surely the below statement can be dropped as always true
            if numerator in squares: 
                denominator = (a*a) + ((a+b)**2)
                if denominator in quads:
                    coprimes.append((a,b))

print("number of co primes = {}".format(len(coprimes)))
print("Co Primes = {}".format(coprimes))


