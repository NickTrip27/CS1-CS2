uppercase = ["A","B","C"]
lowercase = ["a","b","c"]

for upper in uppercase:
    print(upper)
for i in range (len(lowercase)):
    print(f"{uppercase[i]}{lowercase[i]}")
for i in range(4):
    print(i)
for lower in lowercase:
    print(f"{lower}{uppercase[lowercase.index(lower)]}")
