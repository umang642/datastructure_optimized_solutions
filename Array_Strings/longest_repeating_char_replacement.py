class LongestRepeatingCharReplacement:
    def get_length_longest_repeating_char_replacement(self, complete_string: str, k: int) -> int:
        l = 0
        longest_length = 0
        count = [0] * 26

        for r in range(len(complete_string)):
            count[ord(complete_string[r]) - 65] += 1
            while (r-l+1) - max(count) > k:
                count[ord(complete_string[l]) - 65] -= 1
                l += 1
            
            longest_length = max(longest_length, (r-l+1))
        
        return longest_length


if __name__ == '__main__':
    complete_string = 'AAABBADDBBBDAAA'
    k = 4
    s = LongestRepeatingCharReplacement()
    print(s.get_length_longest_repeating_char_replacement(complete_string=complete_string, k=k))