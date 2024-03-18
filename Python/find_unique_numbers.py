#Given an integer array nums, find all the unique numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.


def find_unique_numbers(nums: List[int]):
	seen = set()
	ans = set()
	is_valid = lambda x : (x + 1) not in seen and (x - 1) not in seen
	for x in nums:
		seen.add(x)
	for x in nums:
		if is_valid(x):
			ans.add(x)
	return list(ans)

print(find_unique_numbers([2, 1, 6, 4, 7, 2, 1, 0, -4]))