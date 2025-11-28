from typing import List

class EncodeDecodeString:

    def encode_string(self, string_array: List[str]) -> str:
        res = ''

        for word in string_array:
            res += str(len(word)) + '#' + word
        
        return res
    
    def decode_string(self, s: str) -> List[str]:
        result_arr = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            j += 1

            word = s[j:j+length]
            result_arr.append(word)
            
            i = j + length
        
        return result_arr
    

if __name__ == '__main__':
    input_string = ['umang', 'is', 'working', 'from', 'home']
    s = EncodeDecodeString()
    encoded_result = s.encode_string(string_array=input_string)
    print('Encoded String will be -- ', encoded_result)
    decoded_result = s.decode_string(s=encoded_result)
    print('Decode Array will be -- ', decoded_result)
