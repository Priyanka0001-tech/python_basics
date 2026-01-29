# Create a Python file day7.py in VS Code and write a program that:

# 1️⃣ Creates a tuple with 5 colors and prints the third color.

# 2️⃣ Finds the index of a specific color in the tuple.

# 3️⃣ Counts how many times a specific color appears in the tuple.

# 4️⃣ Attempts to change a tuple value (it should give an error).

color=("blue","red","green","black","red")
print(color[2])
print("index of blue",color.index("blue"))
print("red appears",color.count("red"),"times in the tuple")
# color[1]="lime"      #shows error