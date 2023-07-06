#even fibonacci number sum
def fiboEvenSum(n):
    f = 1
    s = 2
    sum = 2
    i = 2
    while s <= n:
        f, s = s, f+s
        if s % 2 == 0:
            sum += s
        i += 1
    return sum

if __name__ == "__main__":
    print(fiboEvenSum(10))
    print(fiboEvenSum(34))