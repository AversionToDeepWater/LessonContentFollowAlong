# pictures = int(input("How many art prints do I have in my room? "))
#
# if pictures == 14:
#     print("You're right! How did you guess that?")
# else:
#     print("No hehe")


# pets = input("Do you prefer cats or dogs? ").lower()
#
# if pets == "dogs":
#     print("Dogs are great!")
# elif pets == "cats":
#     print("I love cats!")
# else:
#     print("Hmmm I didn't ask that")

# Instructions:
#
# 1. Create a Python program that asks the user to enter a username and a password.
#
# 2. If the user enters the correct username and password, print a welcome message.
#
# 3. If the username is correct but the password is wrong, print "Incorrect password."
#
# 4. If the username is incorrect, print "Unknown user."
#
# 5. Add an extra condition to check if the user is an admin, and if they are, give a special "Welcome, Admin!" message.
# """

user_test = "user1"
password_test = "password"

user_name1 = str(input("Please input a username: "))
user_password1 = str(input("Please input a password: "))

if user_name1 != user_test:
    print("Unknown user")
elif user_name1 == user_test and user_password1 != password_test:
    print("Incorrect password")
elif user_name1 == user_test and user_password1 == password_test:
    print("Correct")


