# 정말 의식의 흐름대로 단순하게 풀이(1~3 통과, 나머지는 시간 초과) => 당연한 결과..
# def solution(n, times):
#     answer = 0
#     check = []
#     for time in times:
#         check += [time * i for i in range(1, n+1)]
#     check = sorted(check)
#     answer = check[n-1]
#     return answer


# while 조건 등호 여부와 if 조건에 따라서 테스크 결과가 달라짐(if, elif, else)로 나눴을 때는 틀리다고 나옴.
# 조건문 내 등호 바꾸다가 오랫동안 삽질 => 다른 풀이에서 되는 조건문 찾음
def solution(n, times):
    answer = 0
    bottom = 0
    top = max(times) * n
    
    while bottom <= top:
        mid = (bottom + top) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
        
        if cnt >= n:
            top = mid - 1
            answer = mid
        else:
            bottom = mid + 1
    
    print(answer)
    return answer