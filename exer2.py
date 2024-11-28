
n1= input("Digite um numero: ")
n2= input("Digite um numero: ")
n3= input("Digite um numero: ")

maior = n1
menor =n1

if maior>n2:
    menor = n2
if menor>n3:
    menor = n3
if n2>maior:
    maior = n2
if n3<menor:
    menor = n3
if n3>maior:
    maior = n3
if menor>n2:
    menor = n2
print(f"Maior = {maior}",)
print(f"Menor = {menor}")
    
