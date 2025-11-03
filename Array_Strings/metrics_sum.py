from typing import List

class MetricsSum: 
    def get_the_metric_sum(self, metric1: List[int], metric2: List[int]) -> List:
        pointer1 = 0
        pointer2 = 0
        carry = 0
        result_array = []

        while pointer1 < len(metric1) and pointer2 < len(metric2):
            result_int = metric1[pointer1] + metric2[pointer2] + carry
            carry = result_int // 10
            result_array.append(result_int % 10)
            pointer1 += 1
            pointer2 += 1
        
        while pointer1 < len(metric1):
            result_int = carry + metric1[pointer1]
            carry = result_int // 10
            result_array.append(result_int % 10)
            pointer1 += 1
        
        while pointer2 < len(metric2):
            result_int = carry + metric2[pointer2]
            carry = result_int // 10
            result_array.append(result_int % 10)
            pointer2 += 1
        
        return result_array

if __name__ == "__main__":
    metric1 = [1,4]
    metric2 = [5,6,7,8]
    s = MetricsSum()
    print(s.get_the_metric_sum(metric1=metric1, metric2=metric2))
