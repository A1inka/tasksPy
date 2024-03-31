def sort(a, b):
    res = a + b
    for i in range (len(res)):
        for j in range (len(res) - i - 1):
            if (res[j] > res[j + 1]):
                res[j], res[j + 1] = res[j + 1], res[j]
    return res
    # return list(set(res)) если нужно без повторений

print(sort([3, 8, 12, 17, 25, 31, 39, 42, 48, 50], [7, 14, 22, 25, 36, 40, 45, 51, 55, 60]))
print(sort([1, 3, 5, 7], [1, 3, 5, 7]))           
            
