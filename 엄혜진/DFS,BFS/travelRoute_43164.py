# 40분 넘게 붙잡고, 다른 사람 코드를 읽어봤지만 감이 안온다...
# 어떻게 DFS or BFS 로 풀 생각을 할 수 있는 걸까...

def solution(tickets):
    answer = []
    
    sorted(tickets, key=lambda x : x[0])
    
    for a, b in tickets:
        if not a in answer:
            answer.append(a)
            
        if not b in answer:
            index = answer.index(a)
            answer.insert(index + 1, b)
        print(answer)
    return answer