import array as arr
a = arr.array('i' , [4,3,2,1])
print(a)
b = arr.array('d', [2.3,1.4,5.6,3.4])
print(b)
for i in range (0,4):
    print(a[i], end =" ")
print()
a.insert(2,6)
print(a)
a.append(5)
print(a)