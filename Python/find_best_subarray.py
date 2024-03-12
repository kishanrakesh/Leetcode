def find_best_subarray(nums: list[int], k: int):
    subarray_sum =  0
    for i in range(k):
        subarray_sum += nums[i]
    ans = subarray_sum
    for i in range(k, len(nums)):
        subarray_sum += nums[i] - nums[i - k]
        ans = max(ans, subarray_sum)
    return ans

print(find_best_subarray([1, 4, 6, 4, 22, 5, 24, 4, 54], 3))