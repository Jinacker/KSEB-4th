# 첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 
# 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

N = int(input()) # 사람 수
T = list(map(int, input().split())) # 각 시간

T.sort() # 이거 사실상 그냥 오름차순으로 더하면 최소 시간 나옴.

result = 0 # 총 인출 시간
temp = [] # 초기값

# 1 + 3 + 6 + 9 + 13 = 32

sum = 0
sum_list = []

for i in T:
    sum+=i
    sum_list.append(sum)
    
result = 0

for j in sum_list:
    result += j
    
print(result)
