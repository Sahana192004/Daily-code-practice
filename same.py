i=[2,3,4,4,6,6,6,2,5,3,1]
seen=[]
for x in i:
    if x in seen:
        print(x)
        break
    else:
        seen.append(x)
print(seen)
    