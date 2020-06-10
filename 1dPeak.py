def findPeakElement(nums):
    if len(nums) <= 1:
            return 0

    left = 0
    right = len(nums) - 1
    mid = int(len(nums)/2)
    while left < right:
        if (right == 1 and left == 0) or (right == len(nums) - 1 and left == len(nums) - 2):
            return nums.index(max(nums[left], nums[right]))
        elif nums[mid-1] < nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] < nums[mid-1]:
            right = mid
            mid = int((left+right)/2)
        elif nums[mid] < nums[mid+1]:
            left = mid
            mid = int((left+right)/2)
        else:
            break
    return 0

print(findPeakElement([1,2,3,1]))
print(findPeakElement([1,2,1,3,5,6,4]))
print(findPeakElement([1]))
print(findPeakElement([1, 2]))
print(findPeakElement([1, 2, 3]))
print(findPeakElement([2, 1, 2]))