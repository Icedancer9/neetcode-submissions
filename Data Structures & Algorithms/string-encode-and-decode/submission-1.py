class Solution:

    def encode(self, strs: List[str]) -> str:

        # "5HELLO5WORLD
        # ['hello','44','5world]
        # 
        #  5;hello2;446;5world
        # delimiter that i can easily distinguish from the ASCII value
        encoded_string = []
        for string in strs:
            encoded_string.append(str(len(string)) + ";")
            encoded_string.append(string)
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:

        # starting at 0, go until you hit first semi-colon
        # Keep track of the numbers you pass through until you
        # hit the semi-colon
        decoded_string = []
        count = 0
        while count < len(s):
            len_of_string = []
            while s[count] != ';' and count < len(s):
                len_of_string.append(s[count])
                count += 1
            count += 1
            len_of_string = int("".join(len_of_string))
            new_count = len_of_string + count
            decoded_string.append(s[count:new_count])
            count = new_count 
        return decoded_string





        
