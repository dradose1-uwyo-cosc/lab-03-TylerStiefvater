names=['colter','colton','tyler','colin','braxton']
print(names)

names.remove("tyler")
print(names)

names.append("emmanuel")
print(names)

for name in names:
    print(f"{name} is at my table")
 
names.reverse()
print(names)
names.sort(reverse=True)
print(names)