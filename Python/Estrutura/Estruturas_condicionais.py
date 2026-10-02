idade = int(input("digite sua idade"));

if(idade >= 18):
    print("Pode tirar a carta já");
elif(idade>=16 and idade <=18):
    print("Pode tirar a carta com supervisao dos pais");
else:
    print("Nao pode tirar")

status = "Pode tirar a carta" if idade > 18 else "Nao pode";
print(status);

verificao = 10 if idade >17 else 20;
print(verificao);
