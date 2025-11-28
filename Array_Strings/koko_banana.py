from typing import List
import math

class KokoBanana:
    def get_banana_per_hours(self, pills: List[int], h: int) -> int:
        left = 1
        right = max(pills)

        while left < right:
            middle = (left + right) // 2
            total_hours = 0

            for pill in pills:
                total_hours += math.ceil(pill / middle)
            
            if total_hours <= h:
                right = middle
            else:
                left = middle + 1
            
        
        return right

if __name__ == '__main__':
    pills = [1,3,2,5,3,4]
    h = 9
    k = KokoBanana()
    print(k.get_banana_per_hours(pills=pills, h=h))