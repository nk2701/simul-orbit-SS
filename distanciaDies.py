#dades calendari
diesMes = [31,28,31,30,31,30,31,31,30,31,30,31]
diesMesAcum0 = [0,31,59,90,120,151,181,212,243,273,304,334,365]
diesMesAcum1 = [0,31,60,91,121,152,182,213,244,274,305,335,366]
inicialDia = 1
inicialMes = 1
inicialAny = 2000
controlDia = 0
controlMes = 0
controlAny = 0
sumatoriDies = 0

def anytraspas(x):
    if x%4 != 0:
        return 0
    elif x%100 != 0:
        return 1
    elif x%400 != 0:
        return 0
    else:
        return 1

#càlcul dels dies de l'època

print("Data final? (ddmmaaaa)")
data = int(input())
dataDia = int(data/1000000)
dataMes = int(data/10000)-dataDia*100
dataAny = data-dataDia*1000000-dataMes*10000

#if inicialAny < dataAny:

difAny = dataAny-inicialAny
x = inicialAny
while difAny > controlAny:
    if anytraspas(x) == 1:
        sumatoriDies +=366
    else:
        sumatoriDies+=365
    x+=1
    controlAny+=1

print(f"Dies dels anys: {sumatoriDies}")

difMes = dataMes-inicialMes
if anytraspas(dataAny) == 1:
    sumatoriDies += diesMesAcum1[difMes]
else:
    sumatoriDies += diesMesAcum0[difMes]

print(f"Dies dels mesos i anys: {sumatoriDies}")
    
sumatoriDies+=dataDia-1
print(f"Total dies: {sumatoriDies}")
