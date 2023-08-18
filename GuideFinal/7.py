def sumTwoSmallestNums(nums):
    smallest1 = min(nums)
    nums.remove(smallest1)
    smallest2 = min(nums)
    return smallest1 + smallest2


numbers = [5, 3, 9, 1, 7]
result = sumTwoSmallestNums(numbers)
print("Sum of the two smallest numbers:", result)
