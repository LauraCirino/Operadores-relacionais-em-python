peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

imc = peso/(altura ** 2)

if imc < 18.5:
    print("Você esta abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Você esta no peso ideal")
else:
    print("Você esta acima do peso")