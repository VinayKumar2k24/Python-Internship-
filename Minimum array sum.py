def min_sum(arr):
    arr.sort(reverse=True)
    total = arr[0]
    avg = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < avg:
            break
        total += arr[i]
        avg = (total) / (i + 1)
    
    return total

n = int(input())
arr = list(map(int, input().split()))

result = min_sum(arr)
print(result)
