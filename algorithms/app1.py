## Bubble sorting
l = eval(input("Enter your number list:"))
for i in range(0, len(l)):
    for j in range(0, len(l)-i -1):
        if l[j] > l[j+1]:
            l[j], l[j+1] =  l[j+1], l[j]
        else:
            continue
        print("\t",l)

print("Sorted list: ", l)