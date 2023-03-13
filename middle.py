from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3:
            return []
        
        out = set()
        nums.sort()
        
        for i in range(0, len(nums)-2):
            
            left, right = i+1, len(nums)-1
            
            while left < right:
                
                sum_nums = nums[i] + nums[left] + nums[right]
                
                if sum_nums < 0:
                    left +=1 
                elif sum_nums > 0:
                    right -= 1
                else:
                    out.add((nums[i], nums[left], nums[right]))
                    
                    left += 1
                    right -= 1
                    
        return out