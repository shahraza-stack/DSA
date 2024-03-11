# Single Number
# link to leet code ==> https://leetcode.com/problems/single-number/


def singleNumber(nums):
        # num_list = list(set(nums))

        for i in range(len(nums)):
            count = nums.count(nums[i])
            if count == 1:
                return nums[i]
            
# num = [1,2,4,5,5,4,2,1]
num = [1,2,4,5,4,2,1]
print(singleNumber(num))

       
        # if len(nums) == 1:
        #     return nums[0]
        # for i in range(len(nums)):
                
        #     if nums[i] != nums[i+1]:
        #         return nums[i]