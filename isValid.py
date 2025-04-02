class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for i in s:
            if i == "[" or i == "(" or i == "{":
                arr.append(i)
            else:
                temp = arr.pop()
                if (temp == "[" and i != "]") or (temp == "(" and i != ")") or (temp == "{" and i != "}"):
                    return False
        if len(arr) == 0:
            return True
        return False
