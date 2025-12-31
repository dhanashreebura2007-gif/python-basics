# PROGRAM 1 : EVEN OR ODD  
num = int(input("Enter a number: "))
if num % 2 == 0:
  print("Even number")
else:
  print("Odd number")

# PROGRAM 2 : POSITIVE / NEGATIVE / ZERO
num = int(input("Enter a number: "))
if num > 0:
  print("Positive")
elif num < 0:
  print("Negative")
else:
  print("Zero")

# PROGRAM 3 : LARGEST OF TWO NUMBER
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("a is greater")
else:
    print("b is greater")

# PROGRAM 4 : PASS OR FAIL 
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")
