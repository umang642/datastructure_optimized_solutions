from typing import List

class MergeInterval:
    def get_merge_interval(self, intervals: List[List[int]]) -> List[int]: 
        # define new merged array 
        merged_array = []

        # Sort the interval firt
        intervals.sort(key= lambda intervals:intervals[0])

        # run the loop in interval and compare the number and append in merged array
        for interval in intervals:
            if not merged_array or merged_array[-1][1] < interval[0]:
                merged_array.append(interval)
            else:
                merged_array[-1] = [merged_array[-1][0], interval[1]]
        
        return merged_array
    
if __name__ == '__main__':
    intervals = [[1,3], [2,6], [8,10], [12,15]]
    s = MergeInterval()
    print(s.get_merge_interval(intervals=intervals))