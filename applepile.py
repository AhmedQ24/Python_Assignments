apples1=(1,2,3,4,5)
apples2=(1,3,5,7)
pile1=0
pile2=0
for x in range(5):
    pile1=pile1+apples1[x]
for y in range(4):
    pile2=pile2+apples2[y]

print("Pile one contains:", pile1, "apples")
print("Pile two contains:", pile2, "apples")