def bfs(begin, target, words, visited):
    stack = [(begin, 0)]    # (current word, depth)
    while stack:
        cur, depth = stack.pop()
        if cur == target:
            return depth
        
        for i in range(len(words)):
            if visited[i] == True: # 이미 방문한 노드
                continue           # skip

            cnt = 0
            
            ''' 
                글자 비교
                "h" "h"
                "i" "o"
                "t" "t" 
            '''
            for word1, word2 in zip(cur, words[i]):
                if word1 != word2:
                    cnt += 1
                
            if cnt == 1:
                visited[i] = True
                stack.append((words[i], depth+1))
                
            

def solution(begin, target, words):
    answer = 0

    if target not in words: # 규칙 2. words에 있는 단어로만 변환할 수 있습니다.
        return 0

    visited = [False]*(len(words))  # [0 for _ in range(len(words))]

    answer = bfs(begin, target, words, visited)

    return answer

if __name__ == "__main__":
    result = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    print(result)

'''
FROM:
    https://hongcoding.tistory.com/53
'''