
name = "frank"
for i in name:
    print(i)

hashtie = dict.fromkeys(name, 0)
print(hashtie)
for i in name:
    hashtie[i] += 1

print(hashtie)