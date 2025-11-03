class CountStringInDict:
    def getDictWithCharCount(self, input_string: str) -> dict:
        output_dict = {}
        for char in input_string:
            if char not in output_dict:
                output_dict[char] = 1
            else:
                output_dict[char] += 1
        return output_dict

if __name__ == "__main__":
    input_string = 'aaaassssbbbbwwwwwwaaaaddbbbbsssoooo'
    page_object = CountStringInDict()
    print(page_object.getDictWithCharCount(input_string=input_string))