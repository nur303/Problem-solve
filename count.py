
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 6

    for i in range(n):
        index = arr[i] // exp
        count[index % 6] += 1

    for i in range(1, 6):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 6] - 1] = arr[i]
        count[index % 6] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)
    exp = 1

    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

ids = [123456, 987654, 567890, 432109, 789012]
radix_sort(ids)
print(ids)