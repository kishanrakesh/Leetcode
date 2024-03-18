#You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

#For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".

def distinct_characters(s: str, k: int) -> int:
	ans = left = 0
	count = {}
	for right in range(len(s)):
		if s[right] in count:
			count[s[right]] += 1
		else:
			count[s[right]] = 1
		while len(count) > k:
			if s[left] not in count:
				print(s[left])
				raise Exception("Sorry, left is not in counter")
			if count[s[left]] == 1:
				del(count[s[left]])
			else:
				count[s[left]] -= 1
			left += 1
		ans = max(ans, right - left + 1)
		print(s[left: right + 1])
	return ans

print(distinct_characters("abcbcadcbadbax", 3))