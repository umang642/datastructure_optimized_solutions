import re

class FindExecptionWithCount:
    def get_exceptions_with_count(self, execption: str) -> dict:
        regex_pattern = r'\b\w+Exception\b'
        exception_dict = {}

        all_exceptions = re.findall(regex_pattern, execption)
        
        for exception in all_exceptions:
            exception_dict[exception] = exception_dict.get(exception, 0) + 1
        
        return exception_dict
    
if __name__ == '__main__':
    exception = '2024-03-12 ERROR NullPointerException at line 52 2024-03-12 ERROR IOException connection reset 2024-03-12 ERROR NullPointerException at line 612024-03-12 ERROR TimeoutException request timed out'

    s = FindExecptionWithCount()
    print(s.get_exceptions_with_count(execption=exception))