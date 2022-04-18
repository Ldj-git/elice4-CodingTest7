# 어떻게 이진탐색으로 풀어야할지 감이 오질 않는다
# 30분 정도 고민하다가 블로그 참고
# 최단 심사 시간을 구해야하므로, 0에서 최장의 심사 시간까지 담은 배열로 이진탐색
# 배열을 대신할 수 있게 left, right 값만 가지고 계산

def solution(n, times):
    answer = 0
    
    # 0, 최장 심사 시간
    left, right = 0, max(times) * n 
    
    while left <= right: # 왜? 이진트리의 가장 마지막 레벨의 노드도 확인하기 위해서, left == right 때도 확인
        mid = (left + right) // 2
        people = 0 
        for time in times:
            people += mid // time # 심사는 병렬적으로 진행되므로, 각 심사관이 심사할 수 있는 인원수를 모두 합침

            if people >= n: # 왜? 입국심사를 모두 받은 경우이기 때문에 더 계산할 필요가 없다
                break 

        if people >= n: # 심사할 사람 <= 심사한 사람 == 시간을 줄일 수 있다
            answer = mid # 왜? 최단 시간인지는 확실하지 않지만, 일단 답이 될 수 있는 시간이다. 
            right = mid - 1 # (왼쪽)
        else: # 심사할 사람 > 심사한 사람 == 시간이 더 필요하다
            left = mid + 1 # (오른쪽)
    
    return answer