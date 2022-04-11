# 30분 정도 풀어보다가 감이 안와서 블로그 참고
# 다른 코드를 보니, idx를 따로 저장하지 않고 numbers자체를 슬라이싱해서 하는 방법도 있었음

def dfs(currentValue, numbers, currentIdx, target):
    if currentIdx >= len(numbers): # 리프노드에 도달한 경우
        if currentValue == target: # 타겟 넘버를 만들 수 있는 경우
            return 1
        else:
            return 0

    answer = 0
    answer += dfs(currentValue + numbers[currentIdx], numbers, currentIdx + 1, target) # +부호를 붙이는 경우
    answer += dfs(currentValue - numbers[currentIdx] , numbers, currentIdx + 1, target) # -부호를 붙이는 경우
    
    return answer

def dfs_with_slicing(currentValue, numbers, target):
    if len(numbers) <= 0:
        if currentValue == target:
            return 1
        else:
            return 0

    answer = 0
    answer += dfs_with_slicing(currentValue + numbers[0] , numbers[1:], target)
    answer += dfs_with_slicing(currentValue - numbers[0] , numbers[1:], target)
    
    return answer

def solution(numbers, target):
    answer = 0
    
    # answer += dfs(0, numbers, 0, target)
    answer += dfs_with_slicing(0, numbers, target)
    
    return answer