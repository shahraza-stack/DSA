def rightRotate(nums, k):
    output_list = []
 
    # Will add values from n to the new list
    for item in range(len(nums) - k, len(nums)):
        output_list.append(nums[item])
 
    # Will add the values before
    # n to the end of new list
    for item in range(0, len(nums) - k):
        output_list.append(nums[item])
 
    return output_list
 
 
# Driver Code
rotate_k = 3
list_1 = [1,2,3,4,5,6,7]
 
print(rightRotate(list_1, rotate_k))