class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # input: 
            #[string1,string2,string3,...string100]
                # len(string1) <= 100
            # each string is sorted lexicographically based on the rules of 
                #the language 
            
        # output:
            # order of the letters in the language 
            # return any valid order of letters
        
        # a < b if 
            # theres a letter in a < b
            # or 
            # no i s.t a[i] !=[b] and a.length < b.length 

        # tracker:
            # n < f
            # h < e
            # r < n 
            # e < r
        # So we first get the relationships and then sort them in order.
            # We need to start at h 

            # [r n f h e]
            # 
        # [hrn, hrf]
        # hr == hr, but we know n < f
        # [hrn, er] 
            # since len(hrn) !< len(er), we assume h < e
        # 
        if len(words) == 1:
            return words[0]

        # First create an adj list of all the unique letters in words
        d = defaultdict(list)
        for word in words:
            for char in word:
                d[char] = set()
        # key is the character and values are the letters that are smaller than it 
        # if a d[key] == [] then that key is the smallest letter 

        # How do I prevent cycles/ continuous checking 
        # now we populate this dictionary 
        for i in range(len(words) - 1):
            curr_word = words[i]
            next_word = words[i + 1]
            solved = False
            # compare the two words and see where they differ
            min_len = min(len(curr_word), len(next_word))
            if len(curr_word) > len(next_word) and curr_word[:min_len] == next_word[:min_len]:
                return ""
            for c in range(min_len):
                curr_char = curr_word[c]
                next_char = next_word[c]
                if curr_char != next_char:
                    d[next_char].add(curr_char) 
                    break 

            
        
        # Now to do topological sort
        explored = set()
        top_sorted = set()
        ans = []

        # Recursion
            # Base case: When do we stop
                # If our class is a cycle or if our class has already been placed in ans
        def dfs(curr_class):

            if curr_class in explored:
                return False
            if curr_class in top_sorted:
                return True 

            explored.add(curr_class)
            for preq in d[curr_class]:
                if not dfs(preq):
                    return False 
            top_sorted.add(curr_class)
            ans.append(curr_class)
            d[curr_class] = []
            explored.remove(curr_class)

            return True 

            
            # We can take care of the case where d[class] == []
        
        for k in d.keys():
            if not dfs(k):
                return ""
        return "".join(ans)



        
        







    
        