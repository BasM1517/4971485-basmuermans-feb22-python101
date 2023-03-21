def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("false")
            return
    print("true")

prime_number = int(input("what number do you want to know about a prime number"))

is_prime(prime_number)