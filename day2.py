# 1️⃣ Asks the user for name, age, and height
# 2️⃣ Converts age to integer and height to float
# 3️⃣ Prints a message like:
# Hello Alex, you are 18 years old and 5.8 feet tall!
# 4️⃣ Takes two numbers from the user and performs:

# Addition
# Subtraction
# Multiplication
# Integer Division
                                # Example Output:
                                # Enter your name: Alex  
                                # Enter your age: 18  
                                # Enter your height: 5.9  
                                # Hello Alex, you are 18 years old and 5.9 feet tall!  

                                # Enter first number: 10  
                                # Enter second number: 3  
                                # Addition: 13  
                                # Subtraction: 7  
                                # Multiplication: 30  
                                # Integer Division: 3 
name=input("Enter your name:")
age=int(input("Enter your age:"))
height=float(input("Enter your height(in feet):"))
print("Hello",name+", you  are",age,"years old and",height," feet tall")
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("Addition:",a+b)
print("Subtraction",a-b)
print("Multiplication:",a*b)
print("Integer Division:",a//b)