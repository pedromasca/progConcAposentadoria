# Programa de Concessão de Aposentadoria
# Desenvolvedor: L. Pedro R Mascarenhas

idade = input("Digite sua idade: ")
sexo = input("Digite seu sexo (M para masculino e F para feminino): ")

if sexo.upper() == "M" :
    # Código para o sexo Masc
    if int(idade) >= 65:
        print("Parabéns, sua aposentedoria foi concedida!")
    else:
        print(f"Sua vez ainda não chegou! Aguarde mais {65 - int(idade)} ano(s).")

elif sexo.upper() == "F":
    # Código para o sexo Fem
    if int(idade) >= 60:
        print("Parabéns, sua aposentadoria foi concedida!")
    else:
        print(f"Sua vez ainda não chegou! Aguarde mais {60 -int(idade)} ano(s).")

else:

    print("Opção Inválida, tente novamente!")