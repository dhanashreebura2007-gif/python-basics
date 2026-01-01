# PROGRAM 1 : PRINT NUMBERS FROM 1 TO 10
for i in range(1, 11):
    print(i)
  
# PROGRAM 2 : PRINT EVEN NUMBERS FROM 1 TO 20
for i in range(2, 21, 2):
    print(i)
  
# PROGRAM 3 : SUM OF FIRST N NATURAL NUMBERS
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i

print("Sum is:", total)

# PROGRAM 4 : MULTIPLICATION TABLE
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
  
# PROGRAM 5 : COUNT DIGITS IN A NUMBER 
num = input("Enter a number: ")
count = 0

for i in num:
    count += 1

print("Number of digits:", count)
