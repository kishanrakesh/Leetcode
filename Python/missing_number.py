#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
	def missingNumberSlow(self, nums: list[int]) ->:
		exists = set(nums)
	for i in range(0, n + 1):
		if i not in exists:
			return i

	def missingNumber(self, nums: list[int]):
		nums_sum = sum(nums)
		return n * (n + 1) / 2 - nums_sum

