class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return Answer.answer(strs)

class Answer:
    def answer(strs: List[str]) -> List[List[str]]:
        # Group all strings that contain the exact same characters as the other strings
        # Group all strings whose character count is the same
        # Dict -> Keys cannot be lists but they can be tuples
            # {(tuple): [strings, strings2, strings2]}


        # Steps
            # Create tuple
            # Populate tuple
            # Check if tuple is in dict
                # If: append string to list
                # Else: Create new list with tuple as key
            # Iterate through dict vals & append them to a list
        tuple_dict = {}
        for s in strs:
            alphabet_list = [0 for i in range(26)]
            for c in range(len(s)):
                alph_to_index = ord(s[c]) - ord('a')
                alphabet_list[alph_to_index] += 1
            tuple_list = tuple(alphabet_list)
            if tuple_list in tuple_dict:
                tuple_dict[tuple_list].append(s)
            else:
                tuple_dict[tuple_list] = [s]
        return [tuple_dict[key] for key in tuple_dict]









        