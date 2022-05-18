# Insertion sorting
l = eval(input("Enter your number list: "))
n = len(l)
for i in range(n):
    t = l[i]
    k = i - 1
    while k >=0 and l[k] > t:
        l[k + 1] = l[k]
        k = k- 1
    l[k + 1] = t
    print(l)

print("Sorted list: ", l)
