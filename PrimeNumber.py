n = int(input("what is your number? "))
def prime_checker(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
    if is_prime == True:
        print(f'{number} is a prime number!')
    else:
        print(f'{number} is not a prime number.')



prime_checker(number=n)