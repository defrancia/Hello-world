
age = input("How old are you ")
if int(age) <= 0:
    print("Enter a value greater than zero")
elif int(age) >= 18:
    print("You are old enough to enter")
else:
    print("you are not old enough to enter")
