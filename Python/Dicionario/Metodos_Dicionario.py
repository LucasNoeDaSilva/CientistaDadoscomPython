contatos2 = {
    "lucas@gmail.com":{"nome":"lucas", "idade":25},
    "julia@gmail.com":{"nome":"julia", "idade":20},
    "felipe@gmail.com":{"nome":"felipe", "idade":18}};
contatos = contatos2.copy();
for chave, valor in contatos2.items():
    print(chave,valor);
contatos2.clear();
for chave, valor in contatos2.items():
    print(chave,valor);
contatos["paulo@gmail.com"]= {"nome":"paulo", "idade":20};

for chave , valor in contatos.items():
    print(chave, valor);

print(contatos.get("lucas@gmail.com",{}));
print(contatos.get("nome",{}));
print(contatos.keys());
print(contatos.pop("paulo@gmail.com","nao encontrado"));
print(contatos.pop("paulo@gmail.com","nao encontrado"));
contatos.setdefault("endereco",{"nome":"vazio", " idade":20});
for chave , valor in contatos.items():
    print(chave, valor);

print("lucas@gmail.com" in contatos);
print("idade" in contatos["lucas@gmail.com"])
print(contatos.values());
del contatos["felipe@gmail.com"];
for chave, valor in contatos.items():
    print(chave,valor);