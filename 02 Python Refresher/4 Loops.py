__author__ = 'Sergey Khrul'

#
# Fourth task of Section #2
#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_numbers(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens


def user_menu(choice):
    if choice == "a":
        return 'Add'
    elif choice == "q":
        return "Quit"

# choice = input("Input 'a' if you want to Add or 'q' if you want to Quit ")
# print("For choice {} your answer is {}".format(choice, user_menu(choice)))
# print(even_numbers(numbers))