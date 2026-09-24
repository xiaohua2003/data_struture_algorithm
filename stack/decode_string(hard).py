class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                cur_s = ""
                while stack and stack[-1] != "[":
                    cur_s = stack.pop() + cur_s
                stack.pop() #remove "["
                digits = ""
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits
                total_s = int(digits) * cur_s
                stack.append(total_s)
        return "".join(stack)

    
        
                    

        