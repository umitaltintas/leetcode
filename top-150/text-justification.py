class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:

        def addWordsToLine(words, spaces, isLastLine=False):
            """Utility function to format words to a given line width."""
            if isLastLine or len(words) == 1:
                return " ".join(words).ljust(maxWidth, " ")

            justified_line = []
            for i, word in enumerate(words):
                justified_line.append(word)
                if i < len(words) - 1:
                    justified_line.append(" " * spaces[i])
            return "".join(justified_line)

        # Group words into lines
        lines, line, line_length = [], [], 0
        for word in words:
            if line_length + len(word) + len(line) > maxWidth:
                lines.append((line, maxWidth - line_length))
                line, line_length = [], 0
            line.append(word)
            line_length += len(word)
        lines.append((line, maxWidth - line_length))

        # Justify the lines
        justified_lines = []
        for i, (line_words, spaces_left) in enumerate(lines):
            if i == len(lines) - 1 or len(line_words) == 1:
                justified_lines.append(addWordsToLine(line_words, [spaces_left], True))
            else:
                base_spaces = spaces_left // (len(line_words) - 1)
                extra_spaces = spaces_left % (len(line_words) - 1)
                spaces = [base_spaces + 1] * extra_spaces + [base_spaces] * (len(line_words) - 1 - extra_spaces)
                justified_lines.append(addWordsToLine(line_words, spaces))
        return justified_lines
    
    
import unittest

def run_tests():
    tests = [
        [["This", "is", "an", "example", "of", "text", "justification."], 16, ["This    is    an", "example  of text", "justification.  "]],
        [["What","must","be","acknowledgment","shall","be"], 16, ["What   must   be", "acknowledgment  ", "shall be        "]],
        [["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20, ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "]]
    ]
    sol = Solution()
    for test in tests:
        words, maxWidth, expected = test
        result = sol.fullJustify(words, maxWidth)
        assert result == expected

if __name__ == "__main__":
    unittest.main()