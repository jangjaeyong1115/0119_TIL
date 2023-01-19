alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

list = list(input())

result = 0

for i in list:
    for j in alphabet:

        if i in j:
            result += alphabet.index(j) + 3

print(result)