class Solution:
    def canConstruct(self, ransomNote, magazine):
        mag_chars = {}
        for char in magazine:
            mag_chars[char] = magazine.count(char)
        
        note_chars = {}
        for char in ransomNote:
            note_chars[char] = ransomNote.count(char)

        print(mag_chars)
        print(note_chars)

        result = False

        for key in note_chars:
            if key in mag_chars:
                if mag_chars[key] >= note_chars[key]:
                    result = True
                else:
                    result = False
                    return result
            else:
                result = False
        print(result)
        return result

solution = Solution()
solution.canConstruct("bcb", "cjjajdfaaeegig")