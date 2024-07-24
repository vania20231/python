with open("arquivo.txt", "w") as f:
    f.write ("text 1\h")
    f.write("text 2\h")



try:
    f=open("arquivo2.txt", "w")
    f.write("eu 1\n")
    f.write("eu 2\n")
finally:
    f.close()    
