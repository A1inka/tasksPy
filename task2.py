def timeOfWork(n):
    resTime = 2
    if n == 0:
        return 0
    if n == 1:
        return 2
    for i in range(2, n + 1):
        resTime = 2 * resTime + 2
    return resTime

print(timeOfWork(1))
print(timeOfWork(3))
print(timeOfWork(5))
    
