valor = input("digite o seu nome");
VOGAIS = "AEIOU"
encontrou = False;
# for com interavel
for i in valor:
    
    if(i.upper() in VOGAIS):
        print("Essa sao as vogais do seu nome: ", i);
        encontrou = True;

if not encontrou:
    print("Nao encontramos nenhuma vogal");

# for com build in
numero = 10;
for numero in range(numero,50,2):
    print(numero, end=" ")
