def merge_sorted_lists(array1: list[int], array2: list[int]) -> list[int]:
    ptr1 = ptr2 = 0
    ans = []
    while ptr1 < len(array1) and ptr2 < len(array2):
        if array1[ptr1] <= array2[ptr2]:
            ans.append(array1[ptr1])
            ptr1 += 1
        else:
            ans.append(array2[ptr2])
            ptr2 += 1
    
    while ptr1 < len(array1):
        ans.append(array1[ptr1])
        ptr1 += 1

    while ptr2 < len(array2):
        ans.append(array2[ptr2])
        ptr2 += 1

    return ans

array1 = [1,4,6,7,8,8,32,143]
array2 = [5,5,7,9,33,142,156]
print(merge_sorted_lists(array1, array2))