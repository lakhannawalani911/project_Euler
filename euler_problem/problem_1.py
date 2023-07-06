def multiplesof3and5(n):
    s = 0
    for i in range(n):
        s += i if i%3==0 or i%5==0 else 0
    return s

if __name__ == "__main__":
    print(multiplesof3and5(10))
    print(multiplesof3and5(49))
    print(multiplesof3and5(1000))
    print(multiplesof3and5(8456))
    print(multiplesof3and5(19564))