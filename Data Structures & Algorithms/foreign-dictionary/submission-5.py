class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Need to create an adjacency list where each key is a letter 
        # and the values are the list of letters that are smaller than it

        # The letter with no values less than it is the smallest letter and 
        # therefore the first letter in the language

        # This language can have disconnected components and can also 
        # have cycles
            # also if a word is a substring of another word, there can be
            # no answer: 'six', 'sixo' <- we do not know where 'o' belongs
        
        # So if this graph has a cycle, or disconnected componenets, or the
        # last constrait, we return ""
    
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

        # This should create a dictionary where
            # {h: [r,c]
            # r: [g, i]
            # i: []
            # g: [o]
            # c: [g]
            #}
        # from here we just do a topological sort
        ans = []
        visited = set()
        top_sorted = set() # these are the values that are already placed in ans

        
        def dfs(node):
            if node in visited: # there is a cycle
                return False
            if node in top_sorted:
                return True 
            visited.add(node)
            for edge in d[node]:
                if not dfs(edge):
                    return False
            ans.append(node)
            top_sorted.add(node)
            visited.remove(node)
            d[node] = set()
            return True 

        for k in d.keys():
            if not dfs(k):
                return ''
        return ''.join(ans) 








    

        