def sieve_of_eratosthenes(number_list):

    primes = []
    while number_list:
        current_prime = number_list.pop(0)
        primes.append(current_prime)
        number_list = [number for number in number_list if number % current_prime != 0]

    return primes


number_list = [2, 3,4, 5, 7, 8, 9,10, 11,12, 13, 17,18, 19, 23]
print(sieve_of_eratosthenes(number_list))
