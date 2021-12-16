

def minvalue(nums):
    min=nums[0]
    for i in range(len(nums)):
        if nums[i]<min:
            min=nums[i]
    print(min)



nums=[23,22,34,233,12,14,13]
minvalue(nums)
print("bye")
