class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        char_map = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in char_map:
                top_element = stack.pop() if stack else "#"
                if char_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
