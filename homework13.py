try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible for a driving license.")
        if age % 2 == 0:
            print("Your age is even.")
    else:
        print("You are not eligible for a driving license.")
    
except ValueError:
    print("Invalid input. Please enter a valid age.")