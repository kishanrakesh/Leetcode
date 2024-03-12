def find_length(s: str) -> int:
    left = number_of_zeroes = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            number_of_zeroes += 1
        while number_of_zeroes > 1:
            if s[left] == "0":
                number_of_zeroes -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

print(find_length("11011001110111"))