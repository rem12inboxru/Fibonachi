N = int(input('Введите число для фибоначчи: '))
B = 1
C = 0
count = 1
if N == 0:
    print (0)

if N == 1:
    print (B)

if N >1:
    while N > count:
        F = B
        B = B + C
        C = F
        count +=1
    print (B)





