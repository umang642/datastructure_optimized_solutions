from typing import List

class LenghtOfPaperCitation:
    def get_length_of_paper_citation(self, nums: List[int]) -> int:
        
        n = len(nums)
        paper_count = [0] * (n+1)
        
        for ci in nums:
            paper_count[min(ci, n)] += 1
        
        h = n
        papers = paper_count[n]

        while papers < h:
            h -= 1
            papers += 1
    

        return h
    

if __name__ == '__main__':
    nums = [3,0,6,1,5]
    s = LenghtOfPaperCitation()
    print(s.get_length_of_paper_citation(nums=nums))
