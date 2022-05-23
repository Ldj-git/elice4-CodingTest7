import sys

def main():
    n = int(sys.stdin.readline())
    result = 0
    
    stones = list(map(int, sys.stdin.readline().split()))
    
    grip_stones = []
    left, right = 0, 0
    
    for i in range(1, n-1):
        for j in range(i+3, n-1):
            left = stones[i-1] + stones[i] + stones[i+1]
            right = stones[j-1] + stones[j] + stones[j+1]
            result = max(result, left + right)
    
    print(result)

if __name__=="__main__":
    main()