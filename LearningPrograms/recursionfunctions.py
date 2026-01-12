#Recursion in python

#Countdown
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)

countdown(5)

#Sum of numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

print(sum_n(5))

#Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

#String character count
def count_char(text, ch, i = 0):
    if i == len(text):
        return 0
        return (1 if text [i] == ch else 0) + ( text, ch, i + 1)

print(count_char("recursion", "r"))

#Number to binary
def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n%2)

print(to_binary(13))
