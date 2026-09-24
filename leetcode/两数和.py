from typing import List
# 暴力解决
class Solution:
    def twoSum(self,nums:List[int],target:int) ->List[int]:
        for i in range(len(nums)):
            for j in range(i+1 ,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

# 哈希表
class Solution:
    def twoSum(self,nums:List[int],target:int) ->List[int]:
        seen = {}
        for i,j in enumerate(nums):
            need = target - j
            if need in seen:
                return [seen[need],i]
            seen[j] = i