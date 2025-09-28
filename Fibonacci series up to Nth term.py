def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    seq = fibonacci(n-1)
    seq.append(seq[-1] + seq[-2])
    return seq

print(fibonacci(7))  