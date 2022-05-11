s=int(input('enter decimal number '))
result=[]
while s>0:
    result.append(str(s%2))
    s//=2
result.reverse()
print("".join(result))

