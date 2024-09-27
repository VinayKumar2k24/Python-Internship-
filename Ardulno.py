def find_farthest_coordinate(arr):
  current_position = 0
  max_distance = 0

  for i in range(len(arr)):
    current_position += arr[i]
    max_distance = max(max_distance, abs(current_position))

  return max_distance
arr = list(map(int,input(). split()))
result = find_farthest_coordinate(arr)
print(result)
