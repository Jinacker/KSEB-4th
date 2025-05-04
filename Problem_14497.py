from collections import deque  # BFS 돌릴 때 큐 써야 돼서 가져옴

# 교실 크기 입력 받음
N, M = map(int, input().split())

# 주난이랑 범인 위치 받음
x1, y1, x2, y2 = map(int, input().split())

# 1부터 시작하는 좌표니까 파이썬 인덱스에 맞게 -1 해줌
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

# 교실 상태 입력받기 (문자 하나하나 리스트에 쪼개서 2차원 배열로 넣음)
room = [list(input().strip()) for _ in range(N)]

# 방향 설정 (상하좌우) — 인접한 곳만 퍼질 수 있음
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 여부 체크 배열 (중복 방문 막기용)
visited = [[False] * M for _ in range(N)]

# 시작 위치 큐에 넣고 방문 처리
queue = deque()
queue.append((x1, y1))
visited[x1][y1] = True

# 파동 횟수 카운트
count = 0

# 본격적으로 BFS 시작
while True:
    count += 1  # 파동 한 번 더 씀 (턴 하나 추가됨)

    next_queue = deque()  # 이번에 못 갔던 친구들 → 다음 턴에 갈 때 쓸 큐

    # 지금 턴에서 갈 수 있는 곳들 하나씩 꺼내서 처리
    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 상하좌우로 한 칸씩 움직여봄
            nx = x + dx[i]
            ny = y + dy[i]

            # 교실 밖이면 스킵
            if not (0 <= nx < N and 0 <= ny < M):
                continue

            # 이미 갔던 곳이면 스킵
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True  # 방문 처리

            if room[nx][ny] == '#':  # 범인 만나면 끝
                print(count)
                exit()

            if room[nx][ny] == '0':  # 빈칸은 바로 이동 가능
                queue.append((nx, ny))
            elif room[nx][ny] == '1':  # 친구는 지금 못 가고 다음 턴에
                next_queue.append((nx, ny))

    # 이번 턴 끝났으면 다음 턴 큐로 넘겨줌
    queue = next_queue
