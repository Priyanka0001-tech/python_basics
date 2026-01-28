# Create a Python file day6.py in VS Code and write a program that:

# 1️⃣ Creates a list of 5 fruits and prints the second fruit.

# 2️⃣ Adds a new fruit to the list and removes one fruit.

# 3️⃣ Sorts the list in alphabetical order and prints it.

# 4️⃣ Uses list comprehension to create a list of squares from 1 to 10.

fruits=["mango","apple","banana","dragon fruit","star fruit"]
print(fruits[1])
fruits.append("grapes")
fruits.remove("apple")
fruits.sort()
print(fruits.count)
print(fruits)
square_list=[x*x for x in range(1,11)]
print(square_list)