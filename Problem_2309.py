# 일곱 난쟁이

# 7명 키 다 합쳐서 100 되는거 오름 차순 정렬

dwarf = []

for i in range(9): 
    dwarf.append(int(input())) # 이렇게도 인풋이 되구나
    
# dwarf 두개 순회하면서 이 두개 뺀 나머지 합이 100인지 체크 => 아니라면 빼버리기

spy = sum(dwarf) - 100 # 드워프 키 다 합산 - 100 => 40 둘이 합쳤을때 40되는 애들 찾기

# 생각해보니까 둘이 합쳐서 40이 된다고 해서.. 나머지 애들 다 더했을때 100이 된다는 보장이 없다.
# 이거에 관한 조건문도 추가해줌.

backup = dwarf # del 됐을때 백업용
flag = 0

for i in range (len(dwarf)): 
    if flag == 1:
        break
    
    for j in range(len(dwarf)): # 자기 자신을 제외한 모두와 조합을 맞춰봐야함.
        if i == j:
            continue
        
        total_sum = dwarf[i] + dwarf[j]
        
        if ( total_sum == spy):
            a= dwarf[i]
            b=dwarf[j]
            dwarf.remove(a)
            dwarf.remove(b) # 해당 배열 
            
            if sum(dwarf) == 100: # 남은 놈들 합 100인지 체크
                flag = 1
                break
            
        dwarf = backup.copy() # 아니면 다시 원상복구 시켜줌.
        

dwarf.sort()

for i in dwarf:
    print(i)