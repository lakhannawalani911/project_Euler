# Problem 4: Largest palindrome product
def largestPalindromeProduct(n):
    max_num = (10**n)-1
    value = []
    while max_num > 0:
        j = max_num
        while j > 0 and j>(10**(n-1)):
            val = max_num * j
            if str(val) == str(val)[::-1]:
                value.append(val)
                break
            j -= 1
        max_num -= 1
    return max(value)
if __name__ =="__main__":
    print(largestPalindromeProduct(2))
    print(largestPalindromeProduct(3))
