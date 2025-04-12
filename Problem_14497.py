# # https://www.acmicpc.net/problem/14497

# 첫째 줄에 주난이가 위치한 교실의 크기 N, M이 주어진다. (1 ≤ N, M ≤ 300)

# 둘째 줄에 주난이의 위치 x1, y1과 범인의 위치 x2, y2가 주어진다. (1 ≤ x1, x2 ≤ N, 1 ≤ y1, y2 ≤ M)

# 이후 N×M 크기의 교실 정보가 주어진다. 0은 빈 공간, 1은 친구, *는 주난, #는 범인을 뜻한다.
'''''
5 7
3 4 1 2
1#10111
1101001
001*111
1101111
0011001
'''''

N, M = map(int,input().split()) # 교실 위치 N과 M

x1,y1,x2,y2 = map(int,input().split()) # 주난이 위치: x1 y1 // 범인 위치: x2 y2

# 행렬과 인덱스 맞춰주기
x1 -= 1 # 행
y1 -= 1 # 열
x2 -= 1
y2 -= 1

# NxM 교실 정보 받기 완료

ClassRoom = [0 for _ in range(N)] 

for i in range (N): # N 열 만큼
    ClassRoom[i] = list(input().strip())  # 이렇게 list에 strip() 써야 하나씩 받을수있다.
    
# 주난이 위치: 3,4를 입력으로 받음.
print(ClassRoom[2][3])

# 주난이가 범인 찾을떄까지 반복
# 주난이의 파동은 상하좌우 4방향으로 친구들을 쓰러뜨릴(?) 때 까지 계속해서 퍼져나간다. 
# 다르게 표현해서, 한 번의 점프는 한 겹의 친구들을 쓰러뜨린다. 다음의 예를 보자.


count = 0 # 범인 잡기까지의 횟수

while (1):
    count += 1
    
    # 일단 첫번째 주난이의 난 페이즈 구현
    
    # 이렇게 탐색 해야함.
    
    # y 열 부분
    # ClassRoom[y1-1][x1] ~ ClassRoom[y1+1][x1]
    
    for i in range(x1-1,x1+2): # 인덱스 y-1 ~ y+1 2=> 1
        if ClassRoom[i][y1] == "*": # 만약 주난이면 스킵
            continue
        elif ClassRoom[i][y1] == "#": # 만약 범인이면 !!! 잡았다 요놈
            ClassRoom[i][y1] = "X"
            print(count) # 카운트 출력.
            break
        
        # 장애물들 깎아내기. 0으로
        ClassRoom[i][y1] = "0" 
        
    # x 행 부분
    # ClassRoom[x1-1][y1] ~ ClassRoom[x1+1][y1]
    
    for j in range(y1-1,y1+2): # 인덱스 y-1 ~ y+1
        if ClassRoom[x1][j] == "*": # 만약 주난이면 스킵
            continue
        elif ClassRoom[x1][j] == "#": # 만약 범인이면 !!! 잡았다 요놈
            ClassRoom[x1][j] = "X"
            print(count)
            break
        
        # 장애물들 깎아내기. 0으로
        ClassRoom[x1][j] = "0" 
        
    break
    
    # 자 일단 첫번째 페이즈는 구현 완료
    

# 확인용 배열 출력 코드
    
for i in range(N):
    print(i,"번째 열: ", ClassRoom[i])