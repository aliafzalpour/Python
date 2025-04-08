number = 0

while True:
    user_number = input("What is your number: ")
    if user_number.isnumeric() == False:
        print("Please give me a number!")
    elif user_number == '0':
        print(f'sum of your number is {number} ')
        break
    else:
        number += int(user_number)
