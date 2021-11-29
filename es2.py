def calculateAvgNorm(low_tres=0, upper_tres=1, *list):
    print(f"list: {list}")
    print(f"tresholds: {low_tres,upper_tres}")
    b=[]
    for a in range(len(list)):
        b.append(a)
    for i, elem in enumerate(list):
        b[i]=(elem-min(list))/(max(list)-min(list))
    print(f"normalized list: {b}")
    for i2, elem2 in enumerate(b):
        if elem2<low_tres or elem2>upper_tres:
            b.pop(i2)
    print(f"result output: {b}")
    summ = 0
    for i3 in b:
            summ += i3
    res=round(summ/len(b),2)
    print(f"Avg from normalized and filtered values: {res}")

calculateAvgNorm(0.5, 1, 3,5,6,4,7,8,9)