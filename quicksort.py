def findPivotIndex(nums, left, right):
    # storing the pivot here 
    pivot = nums[right]
 
    # 3-steps:
    # step-1: Moving pivot element to its actual position 
    # step-2: Moving all smaller elements to left side of pivot 
    # step-3: Moving all greater elements to right side of pivot 
 
    # left = 4 
    # right = 9
    # [18, 10, 20, 15, 100, 90, 17]
    #  0   1    2   3   4   5    6
 
    # [10, 15, 18, 20, 100, 90, 17]
    # [10, 15, 17, 20, 100, 90, 18]
    position = left 
 
    # index --> 0 1 2 3 4 5 
    for index in range(left, right):
        if nums[index] < pivot:
            temp = nums[position]
            nums[position] = nums[index]
            nums[index] = temp 
            position += 1 
 
    temp = nums[right]
    nums[right] = nums[position]
    nums[position] = temp 
    return position
 
 
def performQuickSort(nums, left, right):
    # left = 0    right = 7 
    if left >= right:
        # whenever there are single length arrays, they are already sorted
        return 
    # [18, 10, 20, 15, 100, 90, 17]
    #  0   1    2   3   4   5    6
    pivotIndex = findPivotIndex(nums, left, right)
    # [10, 15, 17, 20, 100, 90, 18]
 
    performQuickSort(nums, left, pivotIndex - 1)
    performQuickSort(nums, pivotIndex + 1, right)
 
n = int(input())
nums = list(map(int, input().split()))
performQuickSort(nums, 0, n - 1)

for i in range(n):
    print(nums[i],end=" ")
