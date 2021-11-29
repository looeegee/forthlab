def calculateAvgFromList(*list):
    sum=0
    for elem in list:
        sum+=elem
    return round(sum/len(list),2)

avg=calculateAvgFromList(2,3,4,3,4,5,2,1,7,7,5)
print(f"mean value: {avg}")

def calculateAvgFromListK(**lists):
    if len(lists) == 0:
        return "N/C"
    sum = 0
    for key, list in lists.items():
        print(key, list)
        sum += list
    return round(sum/len(lists), 2)

print("DOUBLE STAR **")
avg2=calculateAvgFromListK(elem1= 3, elem2= 4, elem3= 5)
print(f"mean value 2: {avg2}")