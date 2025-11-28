from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
class MeetingConflict:
    def is_conflict(self, intervals: List[Interval]) -> bool:
        # get the length 
        n = len(intervals)

        # run the loop for intervals
        for i in range(n):
            for j in range(i+1,n):
                if min(intervals[i].end, intervals[j].end) > max(intervals[i].start, intervals[j].start):
                    return False
                
        return True


if __name__ == '__main__':
    intervals = [(0,30),(5,10),(15,20)]
    s = MeetingConflict()
    s.is_conflict(intervals=intervals)