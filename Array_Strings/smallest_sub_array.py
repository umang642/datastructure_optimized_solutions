from typing import List

class SmallestSubArray:

    def get_smallest_sub_array(self, arr: List[int], target_number: int) -> int:
        window_start = 0
        window_sum = 0
        min_length = float('inf')
        
        for window_end in range(len(arr)):
            window_sum+= window_end

            while window_sum >= target_number:
                current_length = window_end - window_start + 1
                min_length = min(min_length, current_length)
                window_sum -= arr[window_start]
                window_start += 1
        
        return min_length
        
    

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    target = 8
    s = SmallestSubArray()
    print(s.get_smallest_sub_array(arr=arr, target_number=target))