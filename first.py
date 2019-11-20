def count(n):
    a = [0 for i in range(n + 1)]
    a[0] = 1
    for i in range(3, n + 1):
        a[i] += a[i - 3]
    for i in range(5, n + 1):
        a[i] += a[i - 5]
    for i in range(10, n + 1):
        a[i] += a[i - 10]

    return a[n]
n = 20
print('No of Possible ways is', count(n))

