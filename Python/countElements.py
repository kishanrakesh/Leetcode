class Solution:
    def countElements(self, arr: List[int]) -> int:
        exists = set(arr)
        ans = []
        for x in arr:
            if x + 1 in exists:
                ans.append(x)
        return len(ans)