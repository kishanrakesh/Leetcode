#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

#A subarray is a contiguous non-empty sequence of elements within an array.


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = curr = 0
        count = defaultdict(int)
        count[0] += 1
        for i in range(len(nums)):
            curr += nums[i]
            if curr - k in count:
                ans += count[curr - k]
            count[curr] += 1
        return ans