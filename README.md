# Elice4-CodingTest7

엘리스 4기 코딩테스트 스터디 7팀 레포지토리입니다.

---

## 🏃🏻 [참여자](https://github.com/Ldj-git/elice4-CodingTest7/graphs/contributors)

<table>
  <tr>
    <td align="center"><a href="https://github.com/Ldj-git"><img src="https://avatars.githubusercontent.com/u/68588092?v=4" width="100px;" alt=""/><br /><sub><b>Ldj-git</b></td>
    <td align="center"><a href="https://github.com/2taesung"><img src="https://avatars.githubusercontent.com/u/66891085?v=4" width="100px;" alt=""/><br /><sub><b>Taesung Lee</b></td>
    <td align="center"><a href="https://github.com/elizabethgim"><img src="https://avatars.githubusercontent.com/u/65852282?v=4" width="100px;" alt=""/><br /><sub><b>Yujin</b></td>
    <td align="center"><a href="https://github.com/eunna-lim"><img src="https://avatars.githubusercontent.com/u/63828084?v=4" width="100px;" alt=""/><br /><sub><b>eunna-lim</b></td>
    <td align="center"><a href="https://github.com/hyejineom-dev"><img src="https://avatars.githubusercontent.com/u/40953167?v=4" width="100px;" alt=""/><br /><sub><b>Hye-jin Eom</b></td>
    <td align="center"><a href="https://github.com/kminzy"><img src="https://avatars.githubusercontent.com/u/55342113?v=4" width="100px;" alt=""/><br /><sub><b>kminzy</b></td>
    <td align="center"><a href="https://github.com/nohnoori"><img src="https://avatars.githubusercontent.com/u/69712183?v=4" width="100px;" alt=""/><br /><sub><b>nohnoori</b></td>
    </tr>
</table>

---

## 🗓 진행 기간

2022년 4월 4일 ~ 2022년 5월 28일

---

## 📐 진행 방식

### 1️⃣ [프로그래머스 고득점 KIT](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) 문제 풀기

| 스터디 기간         | 이번 주 목표       | 미팅 날짜                |
| ------------------- | ------------------ | ------------------------ |
| 4월  4일 ~ 4월  9일 | 스터디 방식 논의, 깃허브 레포지토리 초대 | 4월 4일 |
| 4월 11일 ~ 4월 16일 | DFS/BFS | 4월 11일 |
| 4월 18일 ~ 4월 23일 | 이분탐색 | 4월 18일 |
| 5월  9일 ~ 5월 14일 | 그래프 | 5월 9일 |
| 5월 16일 ~ 5월 21일 | 백준이나 프로그래머스 문제 3~4개 | 5월 16일 |
| 5월 23일 ~ 5월 28일 | 백준이나 프로그래머스 문제 3~4개 | 5월 23일 |

### 2️⃣ commit 규칙
- 각자 이름으로 폴더를 만들어주세요. 
- 각자 폴더에 푼 문제별로 소스코드를 올리면 됩니다.
- 파일 이름은 적당히 구별하기 좋게 알잘딱 해주세요.
- commit 메세지: [문제 출처(플랫폼)] 문제이름 / 난이도 / 걸린시간
- 메시지 예시: 
```
[PGS] Hello World / 레벨 1 / 1분
```
- 플랫폼 작성법 통일: 
  * [BOJ] - 백준 
  * [PGS] - 프로그래머스

### 3️⃣ 매주 월요일 오후 9시에 모여서 문제 풀이 공유

- 관련 코테 문제 공유 환영!!!

---

## 📓 스터디 미팅 기록

### 🔸 4월 4일
#### 미팅 참여자
: 이동준 엄혜진 김유진 권민지 노누리 임은나 이태성
#### 미팅 내용
- 스터디 방식 논의
- 깃허브 레포지토리 초대

<br/>

### 🔸 4월 11일

#### 미팅 참여자

: 이동준 엄혜진 김유진 권민지 노누리 임은나 이태성

#### 미팅 내용

#### 이번 주 문제: 깊이/너비 우선 탐색(DFS/BFS)

- [43165번 타겟 넘버](https://programmers.co.kr/learn/courses/30/lessons/43165)

  - 다들 DFS나 BFS를 사용해 비슷하게 풀었습니다.
  - 조금 다른 방법으로 [비트마스킹으로도 할 수 있습니다.](https://github.com/Ldj-git/elice4-CodingTest7/blob/57e5d79d6e439c6e534666a9150027f65d2f9de5/%EC%9D%B4%EB%8F%99%EC%A4%80/2%EC%A3%BC%EC%B0%A8%20DFS%2CBFS/%5BPGS%5D%2043165.cpp#L46-L67)
  - [idx를 따로 저장하지 않고 numbers자체를 슬라이싱해서 하는 방법](https://github.com/Ldj-git/elice4-CodingTest7/blob/57e5d79d6e439c6e534666a9150027f65d2f9de5/%EC%97%84%ED%98%9C%EC%A7%84/DFS%2CBFS/targetNumber_43165.py#L17-L28)

- [43162번 네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)
  - 모든 노드에 대해 DFS/BFS를 돌려 방문하고 네트워크로 연결된 것들 카운팅, 다들 비슷하게 풀었으요..
- [43163번 단어 변환](https://programmers.co.kr/learn/courses/30/lessons/43163)

  - words의 단어 하나가 노드, 변환 가능 단어라면 엣지로 연결
  - 만약에 그래프로 나타낸다면 요런식

  <img src="https://media.discordapp.net/attachments/934288741047107628/963060643991261264/image.png" width="50%;" alt=""/>

  - 시작 단어에서 DFS/BFS 돌려서 타겟 도착하면 몇단계 거쳐 갔나 세서 반환
  - **단어간 변환 가능한지 확인하는 부분을 만드는게 핵심!**

- [43164번 여행경로](https://programmers.co.kr/learn/courses/30/lessons/43164)

  - 여러 경로가 나올수 있는데 그중 알파벳순으로 가장 먼저오는걸 반환해야함!

  <img src="https://i.ibb.co/ygY0H0j/Kakao-Talk-20220412-000743760.jpg" width="50%;" alt="Kakao-Talk-20220412-000743760" border="0">

  - 여러 방법 중 [하나](https://github.com/Ldj-git/elice4-CodingTest7/blob/57e5d79d6e439c6e534666a9150027f65d2f9de5/%EC%9D%B4%EB%8F%99%EC%A4%80/2%EC%A3%BC%EC%B0%A8%20DFS%2CBFS/%5BPGS%5D%2043164.cpp#L11-L40) DFS로 모든 가능한 경로들은 저장하고 알파벳순으로 정렬해서 가장 앞에 오는 경로를 반환

  - [두번째 방법](https://github.com/Ldj-git/elice4-CodingTest7/blob/57e5d79d6e439c6e534666a9150027f65d2f9de5/%EB%85%B8%EB%88%84%EB%A6%AC/2%EC%A3%BC%EC%B0%A8%20BFS%2CDFS/travel_routes.py#L1-L22) (코드는 dfs를 반복문으로 구현했네요) [비슷한 방법](https://github.com/Ldj-git/elice4-CodingTest7/blob/57e5d79d6e439c6e534666a9150027f65d2f9de5/%EA%B9%80%EC%9C%A0%EC%A7%84/2%EC%A3%BC%EC%B0%A8%20DFS%2C%20BFS/%5BPGS%5D%20%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C.py#L1-L28)

    - 누리님 설명

      > - dictionary를 이용하여 연결되는 노드를 표시해주었다.
      > - 다음 경로가 있는 공항은 마지막 경로에 도달할때까지 (다음 경로가 없는 공항에 도달할때까지) dictionary에서 값을 pop하여 stack에 추가해준다.
      > - 다음 경로가 없는 경우에는 answer 리스트에 값을 넣어주고 다시 돌아오면서 하나씩 answer에 값을 넣어준다.

    - 제가 이해한 내용..
      > - 티켓의 정보들을 딕셔너리로 바꿔주고
      > - **딕셔너리를 알파벳순으로 정렬하고**
      > - 마찬가지로 DFS를 돌리는데 딕셔너리에서 pop을 해서 방문여부를 봐주고
      > - **answer배열의 순서를 마지막에 뒤집어준다.** ~~약간 후위순회 느낌??~~

- 파이썬 팁

  - 파이썬 전역변수

    - 함수 안에 함수에서는 nonlocal
    - 아니면 global
    - [참고](https://juhi.tistory.com/6)

  - 파이썬에서 list는 뮤터블이다...(수정 가능)

    - [참고](https://wikidocs.net/32277)

  - 파이썬 zip
    - [공식문서](https://docs.python.org/3/library/functions.html#zip)
    - [한글](https://wikidocs.net/32#zip)

#### 다음 주 문제: 이분탐색

###### 어렵겠지만 할수있을껍니다 화이팅...
