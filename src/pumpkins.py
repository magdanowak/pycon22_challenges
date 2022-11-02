import os
from pathlib import Path

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
INPUT_PATH = Path(CUR_DIR) / ".." / "input" / "sample_input.txt"

def get_lines():
    with open(INPUT_PATH) as f:
        for line in f:
            yield line

def main():
    for line in get_lines():
        # your code goes here, feel free to edit anything here
        print(line, end='')
    print()

if __name__ == '__main__':
    main()