for i in range (1, 100):
    print (i)
i = 0
c = True
while c :
    i = i +1 
    print(i)
    if i < 99 :
        c = False

with open("arquivo.txt", "w") as f:
    f.write ("text 1/h")
    f.write("text 2/h")
