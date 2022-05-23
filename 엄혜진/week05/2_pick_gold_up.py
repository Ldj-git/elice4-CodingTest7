# 왜 꼬아서 풀었는가... 할 수 있다면 단순하게 가자!

def main():
    # N = int(input())
    # golds = list(map(int, input().split()))
    
    # result = 0
    # for i in range(2):
    #     total_max = 0
    #     idx = 0
    #     for i in range(len(golds) - 3):
    #         three_in_row = golds[i] + golds[i + 1] + golds[i + 2]
    #         if three_in_row > total_max:
    #             total_max = three_in_row
    #             idx = i
                
    #     fore = golds[:idx] if idx > 2 else []
    #     rear = golds[idx+3:] if N - idx + 3 > 2 else []
    #     golds = fore + rear
    #     # print(golds)
    #     result += total_max
    
    # print(result)

    n = int(input())
    golds = list(map(int, input().split()))

    max = 0
    for i in range(n - 2):
        left = golds[i] + golds[i + 1] + golds[i + 2]
        for j in range(n - 2):
            right = golds[j] + golds[j + 1] + golds[j + 2]
            if left + right > max and (i  - j > 2 or j - i > 2):
                max = left + right
    
    print(max)


if __name__=="__main__":
    main()