class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        longest_common_prefix = ""

        strings_characters = list(zip(*strs))
        is_common_prefix = True
        e = 0

        while is_common_prefix and e < len(strings_characters):
            if all(strings_characters[e][0] == i for i in strings_characters[e]):
                longest_common_prefix += strings_characters[e][0]
                e += 1
            else:
                is_common_prefix = False

        return longest_common_prefix
