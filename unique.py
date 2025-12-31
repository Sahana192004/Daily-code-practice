i=[1,3,3,4,4,5,6,7,7]
unique=[]
for x in i:
    if x not in unique:
        unique.append(x)
print(unique)
print(i)