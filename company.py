N = int(input())
members_in_company = {}

for i in range(N):
    a, b = map(str,input().split())
    if b == 'enter':
        members_in_company[a] = 'work'
    else :
        del members_in_company[a]

members_in_company = sorted(members_in_company.keys(),reverse=True) # 내림차순 정렬
for i in members_in_company:
    print(i)