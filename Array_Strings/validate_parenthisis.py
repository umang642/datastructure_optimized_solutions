class ValidateParenthisis:

    def is_valid_parenthisis(self, input_string: str) -> bool:
        data = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        parenthis_arr = []
        
        if len(input_string) == 0: return False

        for char in input_string:
            if char not in data:
                parenthis_arr.append(char)
            else: 
                val = parenthis_arr.pop()
                if val != data[char]:
                    return False
        
        return len(parenthis_arr) == 0

if __name__ == '__main__':
    input_string = "({[({))]})"
    s = ValidateParenthisis()
    print(s.is_valid_parenthisis(input_string=input_string))
