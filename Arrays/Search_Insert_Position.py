class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)-1                  #get the mid index for floor division giving only integer values

        while left <= right:
            mid = (left+right)//2       #infinite loop until the left index is less than or equal to the right index

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:           #check right
                left = mid + 1
        
            elif nums[mid] > target:           #check left or you could just use else statement here
                right = mid - 1
                
        return left             
    
        