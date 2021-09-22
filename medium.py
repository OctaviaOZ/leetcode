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
    
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict_list = {n:[] for n in set(groupSizes)}
        for i, n in enumerate(groupSizes): dict_list[n].append(i)
        out = []
        for key, item in dict_list.items():
            for n in range(0, len(item)//key):
                out.append(item[n*key: key*(n+1)])
        return out
    
     def arrayNesting(self, nums: List[int]) -> int:
        r, inn = 0, set()
        for i in range(len(nums)):
            out, idx = 0, set()
            if i not in inn:
                while True:
                    if i in idx: break
                    idx.add(i)
                    inn.add(i)
                    i = nums[i]
                    out+=1
                    r = max(out, r)  
        return r 
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        l_arr = nums[:mid]
        r_arr = nums[mid:]
        self.sortArray(l_arr)
        self.sortArray(r_arr)
        self.merge(l_arr, r_arr, nums)
        return nums


    def merge(self, l_arr, r_arr, arr):
        i = j = k = 0
        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] < r_arr[j]:
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1
        
        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1
