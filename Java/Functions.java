public class Functions {
    public boolean isPalindrome(String string) {
        if (string.length() == 0) {
            return false;
        }
        int left = 0, right = string.length() - 1;
        while (left < right) {
            if (string.charAt(left) != string.charAt(right)) 
                return false;
            left++;
            right--;
        }
        return true;
    }

    // Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
    public boolean isSumExists(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        while (right > left) {
            if (numbers[left] + numbers[right] == target)
                return true;
            if (numbers[left] + numbers[right] > target)
                right--;
            else
                left++;
        }
        return false;
    }
}
