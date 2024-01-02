tempoi=50
chico= int(input("Chico calçou a botina? \n 1- sim\n 2- não" ))
if chico == 1:
    tempoi = 40
teobaldo= int(input("Chico veio montado no teobaldo?\n 1- sim\n 2- não"))
if teobaldo== 1:
    tempoi = 30
riacho = int(input("Chico parou no riacho?\n 1- sim \n 2-não"))
if riacho == 1:
    tempoi = tempoi + 40
goiaba = int(input("Chico comeu goiabas? \n 1- sim \n 2- não"))
if goiaba == 1:
    tempoi= tempoi + 20
rosa = int(input("Chico encontrou Rosinha? \n 1- sim \n 2- não"))
if rosa == 1:
    pit = int(input("Quantas pitialinas chico trocou com Rosinha?"))
    tempoi = tempoi + pit*10
onca = int(input("Chico foi surpreendido pela onça? \n 1- sim \n 2- não"))
if onca == 1:
    tempoi = tempoi - 30
print(" O Tempo gasto por chico foi ", tempoi, "minutos")