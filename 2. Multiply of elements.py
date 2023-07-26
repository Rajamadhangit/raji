# 2. Multiply the elements

"""
Analysis:
========
        Functional Analysis:
        -------------------
                1. Get the list of values
                2. multiply each value which is present in the list
                3. print it
        Technical Analysis:
        ------------------
                operators       DM        Loops
                    *, =                   for

State: List of values(int)
Behaviour: initially multiply = 1
            multiply the value
            print it
"""

# State: list of numbers

lst = [1,2,3,4,5,6]
mul = 1

# Behaviour: multiply the value

for i in lst:
    mul = mul * i
print(f"The result is {mul}")