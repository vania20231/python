with open("arquivo.txt", "r")as f:
    txt = f.readline()
    print(txt)
    txt2 = f.readline()
    print(txt2)


def media (n1, n2, n3, n4):
    nota = n1 + n2 + n3 + n4
    m = nota /4
    return m
print ("media 1", media(1,8,3,7))
print ("media 2", media (7,5,6,4))
print ("media 3", media(10,9,3,2 ))
