import os
import re
from pathlib import Path

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
INPUT_PATH = Path(CUR_DIR) / ".." / "input" / "sample_input.txt"

def get_lines():
    with open(INPUT_PATH) as f:
        for line in f:
            yield line

def main():
    word = "PUMPKIN"
    first_syllable_len = 4
    
    word_reversed = word[::-1]
    word_split = ".*?".join(word)
    regexp = fr"[^{word}]({word}|{word_reversed})[^{word}]|{word_split}"
    
    pumpkins = 0
    prev_line = ""
    
    for line in get_lines():
        line_pumpkins = len(re.findall(regexp, line))
        
        line_part = prev_line.strip()[-first_syllable_len:] + line[:len(word) - first_syllable_len]
        interline_pumpkins = int(line_part == word or line_part == word_reversed)
        
        pumpkins += line_pumpkins + interline_pumpkins
        prev_line = line
        
    print(f"Found {pumpkins} pumpkins.")
    
if __name__ == '__main__':
    main()
