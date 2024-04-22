def PerformBubblesort(nums):
    n=len(nums)
    for fixthisindex in range(n-1,0,-1):
        for index in range(fixthisindex):
            if nums[index]>nums[index+1]:
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp
        print(nums)
nums=[12,2,34,20,56,43,45,100,89,50]
print("before sorting")
print(nums)
#logic for performing 

PerformBubblesort(nums)

print("After sorting")
print(nums)
