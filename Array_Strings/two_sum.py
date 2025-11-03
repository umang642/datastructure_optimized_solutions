from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target: 
                    return [i,j]
        return []

    def withHashMap(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i


if __name__ == "__main__":
    input_num = [1,2,3,4]
    target = 3
    s = Solution()
    print(s.withHashMap(nums=input_num, target=target))
