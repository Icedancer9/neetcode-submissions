class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        r = 0
        d = {} #{'char':'ind'} == {y:2, a:0, x:1, }
        prev_removed_ind = -1
        while r < len(s):
            char = s[r]
            if char not in d:
                d[char] = r
            else:
                # if it is in the dict we check if we have already removed it or if we need to remove it 
                if prev_removed_ind < d[char]:
                    prev_removed_ind = d[char]
                    l = prev_removed_ind + 1
                    #print(prev_removed_ind)
                d[char] = r
            ans = max(ans, r - l + 1)
            #print(d)
            #print(s[l:r+1])
            r += 1
        return ans 
                     

        

        # axyzyaxb


        