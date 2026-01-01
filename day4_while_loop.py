# PROGRAM 1 : PRINT NUMBERS FROM 1 TO 10 
i = 1                              
while i <= 10:
    print(i)
    i += 1 
  
# PROGRAM 2 : PRINT EVEN NUMBERS FROM 1 TO 10
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# PROGRAM 3 : PASSWORD CHECK (USING BREAK)
password = "python123"
while True:
    user = input("Enter password: ")
    if user == password:
        print("Access Granted")
        break
    else:
        print("Try again")

# PROGRAM 4 : SKIP NUMBER 5 (USING CONTINUE)  
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
