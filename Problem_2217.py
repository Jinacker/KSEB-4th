#여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. 
#k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

#각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오. 
# 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.


N = int(input())
ropes = [int(input()) for _ in range(N)] # 로프가 버틸 수 있는 무게

# 내림차순 정렬
ropes.sort(reverse=True)

max_weight = 0
for i in range(N):
    weight = ropes[i] * (i + 1)  # i번째 로프부터 i+1개 사용
    max_weight = max(max_weight, weight)

print(max_weight)
