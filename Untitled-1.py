#Calculadora de IMC corporal
peso = float(input("Introduzca su peso en kgs: "))
altura = float(input("Introduzca su altura en m: "))
IMC = peso / altura ** 2
imc = round(IMC, 1)

if imc <= 18.5:
  print("Bajo peso")
elif imc <= 25:
  print("Peso normal")
elif imc <= 30:
  print("Sobrepeso")
else:
  print("Obesidad")
imc = str(imc)
print("Su IMC es " + imc)
