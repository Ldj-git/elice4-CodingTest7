# 30분 붙잡다가 모르겠어서 블로그 참고
# 해당 컴퓨터 연결 정보에 방문한 기록이 없으면 새로운 서브트리라고 인식하고, 그 컴퓨터의 모든 연결정보를 확인하는 방법

def solution(n, computers):
    answer = 0
    
    visited = [0 for _ in range(n)]

    def dfs(i):
        visited[i] = 1
        
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and not visited[j]:
                dfs(j)
                
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1
    
    return answer

# 출처: https://velog.io/@op032/프로그래머스-네트워크-python