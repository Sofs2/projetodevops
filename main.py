from conversor import *
from utils import e_float

print("=== Conversor de Temperatura ===")
print("Teste de alerta no Discord funcionando!")
print("1. Celsius para Fahrenheit e Kelvin")
print("2. Fahrenheit para Celsius e Kelvin")
menu = input("Escolha a opção (1 ou 2): ")

if menu == "1":
    valor = input("Digite a temperatura em Celsius: ")
    if e_float(valor):
        celsius = float(valor)
        print(f"Fahrenheit: {celsius_para_fahrenheit(celsius):.2f}")
        print(f"Kelvin: {celsius_para_kelvin(celsius):.2f}")
    else:
        print("Entrada inválida. Digite um número.")
elif menu == "2":
    valor = input("Digite a temperatura em Fahrenheit: ")
    if e_float(valor):
        fahrenheit = float(valor)
        print(f"Celsius: {fahrenheit_para_celsius(fahrenheit):.2f}")
        print(f"Kelvin: {fahrenheit_para_kelvin(fahrenheit):.2f}")
    else:
        print("Entrada inválida. Digite um número.")
else:
    print("Opção inválida. Escolha 1 ou 2.")
