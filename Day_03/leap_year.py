print("Welcome to Leap Year identifier")

year = int(input("Enter a year without AD/BS : "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


# Wrong first approach
# if ((year % 4 == 0) & (year % 100 != 0) & (year % 400 == 0)):
#     print("Leap year.")
# else:
#     print("Not leap year.")

# Wrong second approach
# if (year % 4 != 0):
#     print("Not leap year.")
# elif (year % 100 == 0):
#     if (year % 400 == 0):
#         print("Leap year.")
#     else:
#         print("Not leap year.")




