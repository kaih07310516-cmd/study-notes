class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # 异或全部数字
        a = 0
        for num in nums:
            a ^=num
        return a