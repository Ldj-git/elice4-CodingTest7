# # 테스트케이스 6, 9번 제외 모두 실패
# def solution(distance, rocks, n):
#     answer = 0
#     rocks = sorted(rocks)
#     gaps = [rocks[0]]
#     gaps += [rocks[i+1] - rocks[i] for i in range(len(rocks)-1)]
#     gaps.append(distance - rocks[-1])
#     for i in range(n):
#         tmp = min(gaps)
#         idx = gaps.index(tmp)
#         if idx == len(gaps) - 1:
#             cal = gaps.pop(-1) + gaps.pop(-1)
#         else:
#             cal = gaps.pop(idx) + gaps.pop(idx)
#         gaps.insert(idx, cal)
#     answer = min(gaps)
#     return answer


# 위 풀이에서의 반례 찾음 -> https://programmers.co.kr/questions/15485

def solution(distance, rocks, n):
    answer = 0
    rocks = sorted(rocks + [distance])
    bottom = 1
    top = distance
    cnt = 0
    
    while bottom <= top:
        # 거리를 체크하는 기준
        mid = (bottom + top) // 2
        
        # 맨 처음 시작점 의미
        prev = 0
        
        # 제거하는 돌의 개수 (이것을 n과 비교!)
        removeCnt = 0
        
        for rock in rocks:
            if rock - prev < mid:
                removeCnt += 1
            else:
                prev = rock
                
        if removeCnt > n:
            top = mid - 1
        else:
            bottom = mid + 1
            answer = mid
    
    return answer