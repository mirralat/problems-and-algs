from typing import List


class Solution:
    def reverseString(self, s: List[str]) ->  List:
        i = 0
        j = len(s)-1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s


sol = Solution()
print(sol.reverseString(["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ",
                         "a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]))