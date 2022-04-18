# 거리를 배열로 두고 이진탐색해야할거 같은데, 어떻게 해야할지 감이 안 옴.. 40분 고민하다가 블로그 참고
# mid보다 작으면 지울지 크면 지울지 혼란스러웠음...

def solution(distance, rocks, n):
    answer = 0
    
    # 최소 거리가 될 수 있는 것들을 배열로 만듦 -> left, right로 대신
    left, right = 0, distance
    
    rocks.sort()
    rocks.append(distance)
    
    while left <= right:
        mid = (left + right) // 2
        # print('범위', left, mid, right)
        
        current = 0
        remove_cnt = 0
        
        for rock in rocks:
            diff = rock - current
            if diff < mid:
                remove_cnt += 1
            else:
                current = rock
                
        if remove_cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
        
    return answer