while True:
    print("[1]-Sacar \n [2]-Deposito \n [0]-Sair" );
    valor = int(input("digite a opcao desejada:"));
    if(valor == 1):
        print("Sacando valor");
    elif(valor == 2):
        print("Depositando valor");
    elif(valor == 0):
        print("Obrigado por sar nosso sistema");
        break;
