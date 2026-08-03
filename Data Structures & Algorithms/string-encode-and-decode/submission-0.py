class Solution:

    def encode(self, strs: List[str]) -> str:

        # neet code love you
        #   neetcodelove youn
        # decode()
        # neet code love you 
        # string can contain any UTF character: numbers,
        # special characters, etc 

        # to encode each string I need to know the
        # criteria for decoding 
        # string = neetcodelov e!10
        # encoded = 11!neetcodelov4!e!10
            # how to decode :  10!neetcodelove!10
            # If i have length of each word, I know how
            # far to go back or forward to get my string
            # I need delimiter to denote the length as 
                # length of the string and not part 
                # of the string itself 
        encoded = []
        for s in strs: # neet
            delimiter = str(len(s)) + "!" # 4!
            encoded.append(delimiter) # [4!]
            encoded.append(s) #[4!, neet]
        return "".join(encoded)
             

    def decode(self, s: str) -> List[str]:


        # Iterate through each character until we see !
            # the numbers before ! are gonna be the length of the string

        # 4!neet
        temp = s
        p1 = 0
        length_count = []
        decoded = []
        while p1 < len(temp):
            length_count = []
            while p1 < len(temp) and temp[p1] != "!":
                length_count.append(temp[p1])
                p1 += 1
            l = int("".join(length_count))
            decoded.append(temp[p1+1:p1 + l + 1])
            p1 = p1 + l + 1
        return decoded 

            
            











