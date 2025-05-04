# https://www.acmicpc.net/problem/3896

# 연속한 소수 p와 p+n이 있을 때, 그 사이에 있는 n-1개의 합성수(소수나 1이 아닌 양의 정수)는 길이가 n인 소수 사이 수열라고 부른다.

# 양의 정수 k가 주어졌을 때, k를 포함하는 소수 사이 수열의 길이를 구하는 프로그램을 작성하시오. k를 포함하는 소수 사이 수열이 없을 때는 길이가 0이다.

# 예를 들어, 소수 23과 29의 소수 사이 수열은 {24, 25, 26, 27, 28}이고, 길이는 6이다.

# 1. 소수 미리 구하기 (에라토스테네스의 체)
MAX = 1299710
is_prime = [True] * MAX
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX, i):
            is_prime[j] = False

# 2. 입력 받기
T = int(input())
ks = [int(input()) for _ in range(T)]

# 3. 각 케이스 처리
for k in ks:
    if is_prime[k]:
        print(0)
    else:
        left = k - 1
        while left >= 2 and not is_prime[left]:
            left -= 1
        right = k + 1
        while right < MAX and not is_prime[right]:
            right += 1
        print(right - left)
