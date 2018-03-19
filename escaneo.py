mapa = [[3,3,3,3,3,3,3,3],
        [3,4,4,4,4,4,4,3],
        [3,4,0,1,4,4,4,3],
        [3,4,4,4,4,2,4,3],
        [3,4,4,2,4,4,4,3],
        [3,4,4,1,4,4,4,3],
        [3,4,4,4,4,4,4,3],
        [3,3,3,3,3,3,3,3]]




metas = []
muneco = []

for x in range (0,(len(mapa)),1):     
    for i in range (0,(len(mapa[x])),1):
        if mapa[x][i] == 2:
            metas.append([x,i])
        if mapa[x][i] == 0:
            muneco = [x,i]


print metas
print muneco
