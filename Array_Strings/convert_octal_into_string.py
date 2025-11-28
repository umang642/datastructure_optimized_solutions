# 110145154154157

class ConvertOctalIntoString:
    def conver_to_string(self, s: str) -> str:
        result_arr = []

        for i in range(0, len(s), 3):
            result_arr.append(s[i:i+3])
        
        new_string = str("\\" + "\\".join(result_arr))
        return new_string
        



if __name__ == '__main__':
    string = "110145154154157"
    s = ConvertOctalIntoString()
    print(s.conver_to_string(s=string))



