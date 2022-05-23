import sys

def main():
    n, m, k = list(map(int, sys.stdin.readline().split()))
    
    rows = []
    cols = []
    for i in range(k):
        row, col = list(map(int, sys.stdin.readline().split()))
        rows.append(row)
        cols.append(col)
        
    print(((max(rows) - min(rows) + 2) + (max(cols) - min(cols) + 2)) * 2)

if __name__=="__main__":
    main()