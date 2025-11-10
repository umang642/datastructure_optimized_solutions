class FindLongestSubStringWithoutRepeating:
    def get_longest_substring_length(self, primary_string: str) -> int:
        pointer_1 = 0
        n = len(primary_string)
        setts = set()
        length_sub_string = 0

        for pointer_2 in range(n):
            while primary_string[pointer_2] in setts:
                setts.remove(primary_string[pointer_1])
                pointer_1 += 1
            
            current_length = (pointer_2 - pointer_1) + 1
            length_sub_string = max(current_length, length_sub_string)
            setts.add(primary_string[pointer_2])
            print("SETSS", setts)
        
        return length_sub_string

if __name__ == '__main__':
    primary_string = 'abcdefabcpq'
    s = FindLongestSubStringWithoutRepeating()
    print(s.get_longest_substring_length(primary_string=primary_string))
