from collections import deque


def solution(begin, target, words):
    answer = 0

    q = deque()
    q.append((begin, 0))
    visited = [0 for _ in range(len(words))]

    while q:
        word, cnt = q.popleft()

        if word == target:
            answer = cnt
            break

        for i in range(len(words)):
            arr = []
            if visited[i] == 0:  # 방문하지 않은 단어일 때
                for j in range(len(words[i])):
                    if word[j] != words[i][j]:
                        arr.append(False)
                if len(arr) == 1:  # 다른 알파벳이 1개일 때만 큐에 넣어주고 방문처리
                    q.append((words[i], cnt + 1))
                    visited[i] = 1

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
