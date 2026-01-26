 #1️⃣ Prints numbers from 1 to 10 using a for loop

# 2️⃣ Prints even numbers from 1 to 20 using a while loop

# 3️⃣ Uses a for loop and break to stop at 5
        # Expected Output:
        # 1 
        # 2
        # 3
        # 4
# (Loop stops at 5)
# 4️⃣ Uses a for loop and continue to skip number 3
        # Expected Output:
        # 1
        # 2
        # 4
        # 5

############1#########
for i in range(1, 11):  # Start from 1 and go up to 10
    print(i)

############2#########
n = 1
while n < 21:
    if n % 2 == 0:
        print(n)
    n += 1

##########3##########
for i in range(1, 11):  # Start from 1
    if i == 5:
        break
    print(i)

############4###########
for i in range(1, 6):  # Start from 1
    if i == 3:
        continue
    print(i)