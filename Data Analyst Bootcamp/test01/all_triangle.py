lines = input("Please enter how many line of * do you want for your star triangle: ")
count = int(lines) + 1
k = 1
n = count
while k < count:
    for i in range(1, n):
        print(" ", end = '')
    for j in range(1, k + 1):
        print(f"{k} ", end = '')
    print("\n")
    k = k + 1
    n = n - 1





