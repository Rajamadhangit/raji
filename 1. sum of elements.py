# 1. sum of numbers in the list

"""
Analysis:
========
        Functional Analysis:
        -------------------
            1. Get the list
            2. Add the numbers which is present in the list
            3. print the sum
        Technical Analysis:
        ------------------
            operator        DM          loops
            +,=                          for

State: list of numbers
Behaviour:  initially sum = 0
            add the numbers to the sum
            print it


"""

# State:

lst = [14,25,63,79,46]
sum = 0

for i in lst:
    sum = sum + i
print(f"sum of number in the list : {sum}")




# Create a list contains user input

new_l = []
x = int(input("Enter the number that how many item u need in a list:  "))
for i in range(1, x+1):
    a = int(input(f"Enter {i} the number to add in a list:  "))
    new_l = new_l+[a]
print(f"this is the new list : {new_l}")