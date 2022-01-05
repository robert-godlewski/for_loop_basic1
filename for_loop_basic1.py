# Step 1) Basic
print('Printing all integers 0 to 150')
for i in range(0, 151):
    print(i)

# Step 2)
print('Printing all multiples of 5 from 5 to 1000')
# for i in range(5, 1000):
#     if i%5 == 0:
#         print(i)
for i in range(5, 1000, 5):
    print(i)

# Step 3)
print('Print integers 1 to 100 but the dojo way')
for i in range(1, 100):
    if i%10 == 0:
        print('Coding Dojo')
    elif i%5 == 0:
        print('Coding')
    else:
        print(i)

# Step 4)
print('Subtotal of odd integers from 0 to 500k is:')
sum = 0
for i in range(0, 500000):
    if i%2 != 0:
        sum += i
print(sum)

# Step 5)
print('Counting down by 4 from 2018')
for i in range(2018, 0, -4):
    print(i)

# Step 6)
print('Creating a flexible counter')
lowNum = 2
highNum = 20
mult = 4
for i in range(lowNum, highNum, mult):
    print(i)
