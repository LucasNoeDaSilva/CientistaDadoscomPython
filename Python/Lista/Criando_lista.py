carro =["camaro","onix","fusca"];
oleo =[];
quantidade =list(range(10));
especificao = ["montadora","ano de fabricacao", "ano de lancamento", "valor"];
nome =list("camaro");
nome2 = ['camaro'];
print(carro);
print(quantidade);
print(especificao);
print(nome);
print(nome2);
print(especificao[0]);
print(nome[:2]);
print(nome[0:3]);
print(nome[0::2]);
print(nome[0:3:2]);
print(nome[::]);
print(nome[::-1]);

for detalhe in especificao:
    print(detalhe);

for i,car in enumerate(carro):
    print({i},{car});

numeros = [0,1,2,3,4,5,6,7,8,9,10];
pares =[];

for i in numeros:
    if(i % 2 ==0):
        pares.append(i);

print(pares);
numeros2 =[10,11,12,13,14,15,16,17,18,19,20];
pares2=[i for i in numeros2 if i % 2==0];
quadrado=[i**2 for i in numeros2];
print(pares2);
print(quadrado);

    