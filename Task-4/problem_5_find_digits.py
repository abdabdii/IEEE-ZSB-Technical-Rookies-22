def findDigits(n):
    literableInt = str(n)
    divisors = 0
    for number in literableInt:
        if int(number) != 0 and n % int(number) == 0:
            divisors = divisors + 1
    return divisors


# Can be tested at https://www.hackerrank.com/challenges/find-digits/problem
