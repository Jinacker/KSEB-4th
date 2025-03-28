# “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”

# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 
# 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

# 입력 => case의 수 / => 2 => k: 몇층 n: 몇호

# k층 n호에 살려면 k-1층 1호~n호까지 사는 사람의 수를 다 합친만큼 사람이 있어야함.
# 0층의 i호에는 i명이 산다.

# 일단 0층 사는 사람
# n = 14호까지 있음 => 공실없음

cases = int(input()) # 케이스 몇개 받을지

results = []

while (cases):
    
    floor = int(input()) # 층
    room = int(input()) # 호
    arr = [[0]*room for _ in range(floor+1)] # 아파트 만들기

    arr[0] = [ i for i in range(1,room+1)] # 몇 호 까지 0번 방 채우기
    summer = 0 # 합산용 카운터

    for i in range(1,floor+1): # 2층
        for j in range(room): # 3호까지
            for k in range(j+1): # 호 전까지 인덱싱
                summer += arr[i-1][k]  # 자기 밑의 층의 0 1 2까지의 합 = 자기층의 3호 = 3
            arr[i][j] = summer
            summer=0
        
    results.append(arr[floor][room-1]) # 결과 저장

    cases -= 1 # 다 돌아서 0되면 while문 종료

for item in results:
    print(item)


#  1층 3호 => 0 1 2 3 4+= 6
#  2층 3호 => 0 1 3 6 10+= 10 
#  3층 3호 => 0 1 4 10 += 15