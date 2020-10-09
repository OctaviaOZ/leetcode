from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                        
        if (len(nums) < 2)|(len(nums) > 1e5):
            return []
        
        if (target < -1e9)|(target > 1e9):
            return []
        
        filter_dict = {}
        for i, num in enumerate(nums):
            
                if (num < -1e9)|(num > 1e9):
                    return []
                
                num_seek = target - num
                if num_seek in filter_dict:
                    idx = filter_dict.get(num_seek)
                    return [idx, i]
                
                if not num in filter_dict:
                    filter_dict[num] = i
         
        return []      