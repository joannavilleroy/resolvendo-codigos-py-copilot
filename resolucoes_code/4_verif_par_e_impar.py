# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

num = int(input("Digite um número: "))

if num % 2 == 0:
    print("O número {} é par".format(num))
else:
    print("O número {} é ímpar".format(num))