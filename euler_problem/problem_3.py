def largestPrimeFactor(number):
    max_prime = 0
    if number ==2 or number == 3:
        return number
    for i in range(2, number+1):
        if number % i==0 and isprime(i) and i>max_prime:
            max_prime = i
    return max_prime

def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(largestPrimeFactor(2))
    print(largestPrimeFactor(3))
    print(largestPrimeFactor(5))
    print(largestPrimeFactor(7))
    print(largestPrimeFactor(8))
    print(largestPrimeFactor(13195))
    print(largestPrimeFactor(60051475143))