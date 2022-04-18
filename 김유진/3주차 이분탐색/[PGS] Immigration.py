# 6명 [7, 10] => 28분
# 6명 [3, 4, 5] => 9분 
# 2명 [2, 5] => 4분

def solution(n, times):
    answer = 0
    low = 1
    high = times[-1] * n

    while low < high:
        mid = (low + high) // 2
        canDo = 0
        for i in range(len(times)):
            canDo += mid // times[i]

        if canDo >= n:
            high = mid
        else:
            low = mid +1
    
    answer = low

    return answer

if __name__ == "__main__":
    case1 = solution(6, [7, 10]) # 28
    print(case1)
    case2 = solution(6, [3, 4, 5])
    print(case2)
    case3 = solution(2, [2, 5])
    print(case3)