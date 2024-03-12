"""
Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. 
A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. 
For each query, the subarray sums are [12, 14, 12].
"""

def answer_queries(nums: list[int], queries: list[list[int]], limit: int) -> list[bool]:
    ans = []
    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)
    prefix_sum.pop(0)
    for i in range(len(queries)):
        ans.append(prefix_sum[queries[i][1]] - prefix_sum[queries[i][0]] + nums[queries[i][0]] < limit)
    return ans

print(answer_queries([1, 3, 2, 6, 3], [[0, 3], [1, 2], [0, 1], [3, 4]], 6))