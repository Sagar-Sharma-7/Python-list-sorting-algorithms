# Selection sorting
l = eval(input("Enter your number list: "))
n = len(l)
for i in range(0, n):
    min = i
    f = False
    for j in range(i + 1, n):
        if l[j] < l[min]:
            min = j
            f = True
    if f == True:
        l[i], l[min] = l[min], l[i]
        print(l)
         