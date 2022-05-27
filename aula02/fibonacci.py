def fibonacci(n):
    res = []

    if n >= 0:
        res = [0] + [1] * min(n, 1)

        while len(res) < n + 1:
            res.append(res[-1] + res[-2])

    return res