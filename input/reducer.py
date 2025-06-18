
import sys

current_col = None
count = 0

for line in sys.stdin:
    col, _ = line.strip().split("\t")
    if col != current_col:
        if current_col:
            print(f"{current_col}\t{count}")
        current_col = col
        count = 1
    else:
        count += 1

if current_col:
    print(f"{current_col}\t{count}")
