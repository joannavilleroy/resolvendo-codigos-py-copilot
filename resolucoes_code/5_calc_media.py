# Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

media = (nota1+nota2+nota3)/3

if media < 5:
    print("Sua média foi {:.2f}, está REPROVADO".format(media))
elif media < 9.9:
    print("Sua média foi {:.2f}, está APROVADO".format(media))
else:
    print("PARABÉNS! Sua média foi {:.2f}, está APROVADO".format(media))