def calculadora(num1, num2, opcao_calculo):
  if opcao_calculo == 1:
    return num1 + num2
  elif opcao_calculo == 2:
    return num1 - num2
  elif opcao_calculo == 3:
    return num1 * num2
  elif opcao_calculo == 4 and num2 !=0:
    return num1 / num2
  else:
    return 0
executar = True
while (executar == True):
  print("Hello")
  print("Este é o algorítimo de uma calculadora")
  print("Essas são as opções de operações:")
  print("1 - Soma")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")
  print("0 - Sair")
  opcao_calculo = int(input("Digite a opção desejada:"))
  if opcao_calculo < 0 or opcao_calculo > 4:
    print("Opção inválida")
  elif opcao_calculo == 0:
    executar = False
    print("Obrigado por usar a calculadora")
  else:
    num1 = int(input("Digite o primeiro número do cálculo:"))
    num2 = int(input("Digite o segundo número do cálculo:"))
    print(calculadora(num1, num2, opcao_calculo))