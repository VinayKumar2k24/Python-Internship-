def max_subarray_sum(nums):
    max_so_far = nums[0]
    curr_max = nums[0]

    for num in nums[1:]:
        curr_max = max(num, curr_max + num)
        max_so_far = max(max_so_far, curr_max)

    return max_so_far
n = int(input())
nums = list(map(int, input().split()))
max_sum = max_subarray_sum(nums)
print(max_sum)
