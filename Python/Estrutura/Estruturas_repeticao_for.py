valor = input("digite o seu nome");
VOGAIS = "AEIOU"

# for com interavel
for i in valor:
    if(i.upper() in VOGAIS):
        print("Essa sao as vogais do seu nome: ", i);
else:
    print("nao foi possivel verificar")

# for com build in
numero = 10;
for numero in range(numero,50,2):
    print(numero, end=" ")
