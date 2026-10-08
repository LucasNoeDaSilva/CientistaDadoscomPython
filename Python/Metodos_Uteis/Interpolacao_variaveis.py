nome = "lucas";
profissao = "analista";
idade =25;
print("ola me chamo %s tenho %d anos e sou %s" %(nome,idade,profissao));
print("ola me chamo {} tenho {} anos e sou {}" .format(nome,idade,profissao));
print("ola me chamo {2} tenho {1} anos e sou {0}" .format(profissao,idade,nome));
print("ola me chamo {nome} tenho {idade} anos e sou {profissao}" .format(profissao=profissao,idade=idade,nome=nome));
print(f"ola me chamo {nome} tenho {idade} anos e sou {profissao}");
print("ola me chamo",nome, "tenho", idade, "anos e sou", profissao);