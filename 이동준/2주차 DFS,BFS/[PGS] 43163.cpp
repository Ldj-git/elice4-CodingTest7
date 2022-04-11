#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

//[PGS] 43163. 단어 변환 / 레벨 3 / 31분

//방문 가능 확인용 한글자만 차이나야 참 아니면 거짓
bool cmp(string a, string b){
    int size=a.size();
    for(int i=0;i<a.size();i++){
        if(a[i]==b[i])
            size--;
    }
    if(size==1)
        return true;
    else
        return false;
}

//h의 visited 값을 리턴 해줌 (begin단어는 visited에 없어서 예외 처리 해주려고 따로 함수로 만듬)
//단어 몇개 안돼서 큰 차이는 없지만 굳이 이렇게 안써도 될듯.. 
//그냥 현재 단어가 begin 이랑 같은지만 판별해주면 밑에 함수 따로 안써도됨
int depth(string h,vector<string>words,vector<int>visited){
    for(int i=0;i<words.size();i++){
        if(h==words[i])
            return visited[i];
    }
    return 0;
}

int solution(string begin, string target, vector<string> words) {    
    //bfs 비스무리하게
    vector<int> visited(words.size(),0); //0으로 초기화, 해당 단어까지 몇단계 걸쳐 왔는지도 기록
    queue<string>q;
    q.push(begin);
    while(!q.empty()){
        string here=q.front();
        q.pop();
        for(int i=0;i<words.size();i++){
            if(cmp(here,words[i])&&visited[i]==0){ //한글자 차이나고 방문한적이 없으면 큐에 추가
                q.push(words[i]);
                visited[i]=depth(here,words,visited)+1;
                if(words[i]==target){
                    return visited[i];
                }
            }
        }
    }
    return 0;
}