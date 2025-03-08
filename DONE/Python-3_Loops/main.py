favorite_foods = ['Pizza', 'Chicken', 'Ice Cream', 'Carbonara', 'Lasagna']

print("Here are my favorite foods:")
for food in favorite_foods:
    print(f"- {food}")  

print("\n")  

try:
    starting_number = int(input("Enter a positive number to start the countdown: "))

    if starting_number <= 0:
        print("Invalid input: Please enter a number greater than zero.")
    else:
        print("Countdown:")
        while starting_number > 0:
            print(starting_number)  
            starting_number -= 1   

        print("Countdown complete!")  

except ValueError:
    print("Invalid input: Please enter a valid number.")