class RemoveDupString:

    def get_non_duplicate_string(self, input_string: str) -> str:
        pointer = 0
        elements = []

        while pointer < len(input_string):
            elements.append(input_string[pointer])
            pointer += 1
        
        print("Converted into Array --", elements)

        removed_duplicate_string_array = set(elements)
        output_string = ' '.join(removed_duplicate_string_array)

        return output_string

if __name__ == "__main__":
    input_string = 'Hello how are you doing today'
    s = RemoveDupString()
    print(s.get_non_duplicate_string(input_string=input_string))
