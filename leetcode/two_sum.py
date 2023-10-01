"""
https://leetcode.com/problems/two-sum/
"""
class TwoSum:
    def tow_sum(self, nums: list[int], target: int) -> list[int]:
        prev_map = {}  # val : index
        for i, n in enumerate(nums):
            dif = target-n
            if dif in prev_map:
                return prev_map[dif], i
            prev_map[n] = i
        return




