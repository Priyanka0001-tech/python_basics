# 1️⃣ Defines a function greet_user(name) that prints "Hello, [name]!"

            # Example Input: greet_user("John")
            # Output: "Hello, John!"
# 2️⃣ Defines a function multiply(a, b) that returns the multiplication of two numbers.

            # Example Input: multiply(4, 5)
            # Output: 20
# 3️⃣ Creates a lambda function to find the square of a number.

            # Example Input: square(6)
            # Output: 36
def greet_user(name):
    print("Hello,",name)
name=input("Enter the name: ")
greet_user(name)

def multiply(a,b):
    return a*b
result=multiply(5,9)
print(result)
square=lambda x:x*x
print(square(9))

