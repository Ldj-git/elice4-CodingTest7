import sys

def main():
    n, m = list(map(int, sys.stdin.readline().split()))
    arrows = []
    for i in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        arrows.append(row)
        
    start = list(map(int, sys.stdin.readline().split()))
    
    start = [start[0] - 1, start[1] - 1]
    stack = [start]
    visited = []
    
    result = 0
    
    while stack:
        pos = stack.pop()
        if pos not in visited:
            visited.append(pos)
            next_pos = []
            if arrows[pos[0]][pos[1]] == 1:
                next_pos = [pos[0]-1, pos[1]]
            elif arrows[pos[0]][pos[1]] == 2:
                next_pos = [pos[0], pos[1]-1]
            elif arrows[pos[0]][pos[1]] == 3:
                next_pos = [pos[0], pos[1]+1]
            elif arrows[pos[0]][pos[1]] == 4:
                next_pos = [pos[0]+1, pos[1]]
            
            if next_pos[0] < 0 or next_pos[0] >= n or next_pos[1] < 0 or next_pos[1] >= m:
                result = -1
                break
            stack.append(next_pos)
        else:
            idx = visited.index(pos)
            result = len(visited) - idx
            break
        
    print(result)
if __name__=="__main__":
    main()