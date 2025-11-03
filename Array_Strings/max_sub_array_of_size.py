### arr = [1,2,3,4,5,6]
### sliding window

from typing import List

class MaxSubArrayOfSize:
    def get_max_sub_array_size(self, arr: List[int], target_number: int) -> int:
        window_start = 0
        window_sum = 0
        result = []

        for window_end in range(len(arr)):
            window_sum += arr[window_end]

            if window_end >= target_number - 1:
                result.append(window_sum)
                window_sum -= arr[window_start]
                window_start += 1
        
        return max(result)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    k = 3
    max_sum = MaxSubArrayOfSize()
    print(max_sum.get_max_sub_array_size(arr = arr, target_number=k))


