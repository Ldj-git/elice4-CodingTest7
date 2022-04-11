# 유사 딕셔너리
# 키가 존재하는 검사하는 코드와 0으로 초기화하는 코드가 필요없음
from collections import defaultdict


def solution(tickets):  # [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	
    answer = []
    routes = defaultdict(list)
    
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1]) # {"ICN":["JFK"]}
    
    for key in routes.keys():
        routes[key].sort(reverse=True)
        
    stack = ["ICN"]
    
    while stack:
        tmp = stack[-1]
        
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    
    answer.reverse()
    
    return answer