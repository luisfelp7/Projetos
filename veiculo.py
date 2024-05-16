qnt = int(input('quantidae de rodas do veiculo ?'))
if qnt == 2 :
 print ('categoria de 2 ou 3  rodas ')
if qnt == 4 :
 print ('categoria de 4 rodas ')
 
peso = int(input('qual e o peso bruto em quilogramas ?'))
if peso < 3500 :
 print('peso ate 3500 kg') 
elif  3500 <= peso <= 6000 :
 print('peso entre 3500 e 6000')
else:
 print('peso maior que 6000 quilos')

pessoas =int(input('quantidade de pessoas no veiculo '))
if pessoas < 9 :
 print ('acomoda ate 8 pessoas')
elif pessoas > 8 :
 print ('acomoda mais de 8 pessoas')
print(f'A quantidade de rodas são {qnt}, peso em quilogramas {peso}, total de pessoas {pessoas}')
# Mensagem inicial para escolher a categoria
mensagem = (
    "Escolha sua categoria\n"
    "A: Veículos com duas ou três rodas;\n"
    "B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;\n"
    "C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;\n"
    "D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;\n"
    "E: Veículos com quatro rodas ou mais e com mais de 6000 kg.\n"
)

# Recebe a entrada do usuário
result = input(mensagem).strip().upper()

# Processa a entrada do usuário com base na escolha
if result == "A":
    print("Você escolheu: Veículos com duas ou três rodas.")
elif result == "B":
    print("Você escolheu: Veículos com quatro rodas, acomodam até oito pessoas e peso até 3500 kg.")
elif result == "C":
    print("Você escolheu: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg.")
elif result == "D":
    print("Você escolheu: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas.")
elif result == "E":
    print("Você escolheu: Veículos com quatro rodas ou mais e com mais de 6000 kg.")
else:
  print("Escolha inválida. Por favor, selecione A, B, C, D, ou E.")   
    