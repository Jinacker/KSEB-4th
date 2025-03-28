# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

# 둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다. 
# 각 방법은 세 정수 i j k로 이루어져 있으며, i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다. 
# 예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다. (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)

# 도현이는 입력으로 주어진 순서대로 공을 넣는다.

n, m = map(int, input().split()) # n: 바구니 개수 / m: 몇번 공 넣을건지

basket = [ 0 for _ in range(n)] # 바구니 생성

while (m):
    i,j,k = map(int, input().split()) # i: 번 바구니부터 j: 까지 k: 번 공을 넣어라
    for idx in range(i,j+1):
        basket[idx-1] = k
    m-=1 # m 만큼 반복
    
for item in basket:
    print(item, end=" ")