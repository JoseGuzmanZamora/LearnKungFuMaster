import pickle

with open("./ganancias.txt","r") as f:
    value = f.readlines()

contador = 0
ganancias = []
for i in value:
    if "." in i:
        contador += 1
        ganancias.append(float(i))

pickle.dump(ganancias,open("./rewards.txt","wb"))

