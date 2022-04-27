print("Please enter the price of items: ")

sum = 0
while (True):
    UserInput = input("Enter the item number: ")
    if (UserInput != "q"):
        sum = sum + int(UserInput)
        print(sum)
    else:
        print("-------Thanks for using our program:------")
        print("Your total bill is ", sum)
        break
