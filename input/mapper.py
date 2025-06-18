
import sys

for line in sys.stdin:
    values = line.strip().split(",")
    for i, val in enumerate(values):
        print(f"coluna{i}\t1")
