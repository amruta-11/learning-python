def check_if_even(num):
    remainder = num % 2
    if (remainder == 0):
        return True
    else:
        return False

isEven = check_if_even(10)
print(isEven)
