file = open('plik.txt', 'r')

tabz = []
tabf = []
e = 0
s = 0
text = file.read()

for a in range(len(text)):
    if text[a] == ';':
        tabz.append(text[e:a])
        s = a + 2
    elif text[a] == '\n':
        e = a + 1
        tabf.append(text[s:a])

tabf.append(text[s:])

odp = []
for i in range(len(tabz)):
    word = tabz[i]
    s = tabf[i]
    x = 0
    z = 0

    for a in range(len(word)):
        if word[a] == s[z]:
            z += 1
            if z == len(s):
                x += 1
                z = 0
        else:
            z = 0
    odp.append(x)

print(odp)
