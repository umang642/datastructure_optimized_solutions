from typing import List

class FibonacciSeries:
    def is_fibonacci_series(self, nums: List[int]) -> bool:
        i = 0
        j = 1
        
        while j + 1 < len(nums) - 1:
            if nums[i] + nums[j] != nums[j + 1]:
                return False
            
            i += 1
            j += 1

        return True

if __name__ == '__main__':
    nums = [1,2,3,5,8,13,21]
    s = FibonacciSeries()
    print(s.is_fibonacci_series(nums=nums))
