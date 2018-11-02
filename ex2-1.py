#e1.3TempConvert.py
Tempstr = input("请输入带有符号的温度值:")
if Tempstr[-1] in ['F','f']:
    C = (eval(Tempstr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}c".format(C))
elif Tempstr[-1] in ['C','c']:
    F=1.8*eval(Tempstr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入错误格式")
    
