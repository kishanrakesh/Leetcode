def is_palindrome(string: str) -> bool:

    #If string is empty, return false
    if len(string) == 0:
        return False

    #initialize two pointers
    left, right = 0, len(string) - 1

    #check if left and right values are different, if they are, then return false.
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    
    #if there is no difference return true
    return True

if __name__ == '__main__':
    number_of_interations = int(input("Enter Number of Strings to Be Checked: "))
    for i in range(number_of_interations):
        string = str(input("Enter the String: "))
        print(is_palindrome(string))
        print()