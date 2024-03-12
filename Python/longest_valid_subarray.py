def longest_valid_subarray(nums: list[int], k: int) -> list[int]:
    subarray_sum = left = 0
    ans = (0, -1)
    for right in range(len(nums)):
        subarray_sum += nums[right]
        while subarray_sum > k:
            subarray_sum -= nums[left]
            left += 1
        if (right - left) > (ans[1] - ans[0]):
            ans = (left, right)
    
    return nums[ans[0]: ans[1] + 1]

print(longest_valid_subarray([1, 3, 1, 2, 1, 6, 2, 3, 1], 4))