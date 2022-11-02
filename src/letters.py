import os
from pathlib import Path

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
INPUT_PATH = Path(CUR_DIR) / ".." / "input" / "letter_game.txt"

def verify(names):
    # 1st check: if all names are unique
    assert len(set(names)) == len(list(names))
    # 2nd check: if all names are in the file
    with open(INPUT_PATH) as f:
        words = set(w.strip().lower() for w in f.readlines() if w.strip())
        assert all(n.lower() in words for n in names)
    # 3rd check: if rules are preserved
    last = None
    c = 0
    for name in names:
        name = name.lower()
        if last is not None and last != name[0]:
            return c, False
        else:
            c += 1
        last = name[-1]
    return c, True

# example:
# print(verify(['Wolfram', 'Matsumoto', 'Odersky']))
# which gives output:
# (3, True)
