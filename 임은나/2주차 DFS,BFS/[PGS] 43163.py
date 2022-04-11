# def solution(begin, target, words):
#     answer = 0
#     if target not in words:
#         return 0
    
#     begin_divide = begin.split()
    
#     # 각 문자를 가지고 있는 단어의 위치를 dictionary로 저장
#     chars = dict()
#     for i, word in enumerate(words):
#         for j, char in enumerate(words[i]):
#             chars[char] = chars.get(char, []) + [(i,j)]
            
#     print(chars)
    
#     return answer

# 질문하기 코드 참고 -> https://programmers.co.kr/questions/18764
import heapq

def possible(A,B):
    count = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            count += 1
    return count

def solution(begin, target, words):

    if not(target in words):
        return 0

    words.append(begin)

    network_dic = dict()

    for i in range(len(words)):
        network_dic[words[i]] = []
        for j in range(len(words)):
            if possible(words[i],words[j]) == len(begin) - 1:
                network_dic[words[i]].append(words[j])

    queue = [(0,begin)]

    while queue:

        length, node = heapq.heappop(queue)
        if node == target:
            return length
        if len(network_dic[node]) == 0:
            pass
        else :
            for i in network_dic[node]:
                if i != begin:
                    alt = length + 1
                    heapq.heappush(queue,(alt,i))