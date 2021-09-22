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
                idx = filter_dict.get(num_seek, None)
                if idx is not None:
                    return [idx, i]
                
                if not num in filter_dict:
                    filter_dict[num] = i
         
        return []
    
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = win_sum = sum(nums[0:k])
        for i in range(0, len(nums)-k):
            win_sum += nums[i+k] - nums[i]
            if max_sum < win_sum:
                max_sum = win_sum
        return max_sum / k   
    
    
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i]) for i in range(1, len(nums)+1)]
    
    
    #Runtime less. Doesn't use sum build-in function
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        out_append = out.append
        out_append(nums[0])
        for i in range(1, len(nums)):
            out_append(nums[i] + out[i-1])
        return out  

    
    def checkIfExist(self, arr: List[int]) -> bool:
        dict_n = {}
        for i, n in enumerate(arr):
            if (n*2 in dict_n) or (n/2 in dict_n): 
                return True
            else:
                dict_n[n] = i
        return False 
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = -1
        while(m > 0 and n > 0):
            if(nums1[m-1] > nums2[n-1]):
                nums1[i] = nums1[m-1]
                m -= 1
            else:
                nums1[i] = nums2[n-1]
                n -= 1
            i -= 1
            
        while(n > 0):
            nums1[i] = nums2[n-1]
            n -= 1
            i -= 1
    
    
    def validMountainArray(self, arr: List[int]) -> bool:
        incr, last_i = 1, len(arr) - 1
        for i, n in enumerate(arr):
            if i == last_i:
                break
            if ( (incr == 1) and (n < arr[i+1]) ) or ( (incr == -1) and (n > arr[i+1]) ): 
                continue
            elif (incr == 1) and (n > arr[i+1]) and (i != 0):
                incr = -1
            else:    
                return False  
         
        return True if incr == -1 else False
