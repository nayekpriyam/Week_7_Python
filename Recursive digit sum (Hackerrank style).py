def super_digit(n):
    if n < 10:
        return n
    return super_digit(sum(int(digit) for digit in str(n)))

print(super_digit(9875)) 