n = input("输入一个5位数字: ")
j = -1
f = 1 #标志变量
for i in range(5):
    if n[i]  != n[j]:
        f = 0
    j = j - 1

if f == 1:
    print("{}不是素数".format(n))
else:
    print("{}是素数".format(n))
