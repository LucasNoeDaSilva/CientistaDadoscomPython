pessoa = {"nome": "lucas", "idade": 25};
pessoa2 = dict(nome="Julia", idade=18);
pessoa["telefone"]= "11 111111111";
print(pessoa['nome']);
pessoa['nome']= 'Lucas Noe';
print(pessoa)

contatos = {
    "lucas@gmail.com":{"nome":"lucas", "idade":25},
    "julia@gmail.com":{"nome":"julia", "idade":20},
    "felipe@gmail.com":{"nome":"felipe", "idade":18}};

print(contatos["lucas@gmail.com"]["nome"]);

for chave in contatos:
    print(chave, contatos[chave]);

for chave, valor in contatos.items():
    print(chave, valor);