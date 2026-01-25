1️⃣ Asks the user for their age and prints:

# "You are a minor." (if age < 18)
# "You just became an adult!" (if age == 18)
# "You are an adult." (if age > 18)
# 2️⃣ Asks the user for a number and prints:

# "The number is positive." (if num > 0)
# "The number is negative." (if num < 0)
# "The number is zero." (if num == 0)
#         Example Output:
#             Enter your age: 20  
#             You are an adult.  2
#             Enter a number: -5  
#             The number is negative.
age=int(input("Enter the age: "))
if (age<18):
    print("You are minor.")
elif (age==18):
    print("You just become an adult!")
else:
    print("You are an adult.")
num=int(input("Enter a number: "))
if (num>0):
    print("The number is positive.")
elif(num==0):
    print("The number is zero.")
else:
    print("The number is negative.")