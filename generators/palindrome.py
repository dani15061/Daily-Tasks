def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(start):
    num = start + 1
    while True:
        if is_palindrome(num):
            yield num
        num += 1
n = int(input("Input a number: "))
palindrome_gen = next_palindrome(n)
next_palindrome_num = next(palindrome_gen)
print("Next palindrome number after", n, "is:", next_palindrome_num)