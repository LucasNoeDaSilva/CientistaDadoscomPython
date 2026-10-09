def carro(nome,ano,/,montadora):
    print(nome,ano,montadora);

carro("gol",1998,"fiat");


nome="moto";
ano=2001;
def moto(*, nome,ano):
    nome ="lucas";
    print(nome,ano);
   
moto(nome=nome,ano=ano);

def somar(a,b):
    return a+b;

def exibir(a,b,funcao):
    resultado= funcao(a,b);
    print(resultado)

exibir(10,10,somar)