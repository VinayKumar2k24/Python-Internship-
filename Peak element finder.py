def find_peak_element(arr):
  n = len(arr)
  if n == 1:
    return 0

  if arr[0] > arr[1]:
    return 0

  if arr[n - 1] > arr[n - 2]:
    return n - 1

  for i in range(1, n - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
      return i

  return -1
n = int(input())
arr = list(map(int, input().split()))
index = find_peak_element(arr)

if index != -1:
  print(index)
else:
  print("No peak element found.")
