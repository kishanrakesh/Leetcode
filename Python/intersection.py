#Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        seen = set(nums[0])
        for i in range(1, len(nums)):
            seen = seen.intersection(set(nums[i]))
        return sorted(list(seen))
	

	#counts = Counter([i for num in nums for i in num])
        #return sorted([k for k, v in counts.items() if v == len(nums)])

