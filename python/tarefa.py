# tarefa 1
#ola="Ola mundo!"
#print(ola)
#---------------------------------------------
# tarefa 2
#nome = "marco"
#cidade = "Uberlândia"
#idade="15"
#print(nome)
#print(idade)
#print(cidade)
#---------------------------------------------
# tarefa 3
#nome =  (input("Digite seu nome"))
#print (nome)
#---------------------------------------------
# tarefa 4
#idade = int(input("Digite sua idade"))
#print (idade)
#---------------------------------------------
# tarefa 5
#numero1 = int(input("Digite um numero"))
#numero2 = int(input("Digite um numero"))
#print(numero1 + numero2)
#---------------------------------------------
# tarefa 6
#numero1 =int(input("Digite um numero"))
#numero2 = int(input("Digite um numero"))
#print(numero1 - numero2)
#print(numero1 + numero2)
#print(numero1 * numero2)
#---------------------------------------------
# tarefa 7
#numero1 = int(input("Digite um numero"))
#print(numero1 * 2)
#---------------------------------------------
# tarefa 8
#numero1  = int (input("Digite um numero"))
#print(numero1*3)
#print(numero1/2)
#---------------------------------------------
# tarefa 9
#nome1 = (input("Digite seu primeiro nome"))
#nome2 = (input("Digite seu segundo nome"))
#print(nome1+nome2)
#---------------------------------------------
# tarefa 10
#ano = int(input("Qua o ano que você naceu"))
#print(2026-ano)
#---------------------------------------------
# tarefa 11
#metros = float(input("Digite o valor em metros: "))
#print(f"{metros}m equivalem a  {metros * 100}cm e {metros * 1000}mm")
#---------------------------------------------
# tarefa 12
#minutos = float(input("Digite um valor em minutos"))
#print(f"{minutos}m equivalente a {minutos * 60} s ")
#---------------------------------------------
# tarefa 13
#horas = float(input("Digite um valor em horas "))
#print(f"{horas}h equivalem a {horas * 60}s")
#---------------------------------------------
# tarefa 14
#grausc = float(input("Digite um valor em graus celsius"))
#fanhreit = grausc  * 9 / 5 + 32
#print(f"{grausc}c equivalente a {fanhreit :.1f}f")
#---------------------------------------------
# tarefa 15
#valorreais = float(input("Digite o valor em reais (R$)"))
#cotacaodolar = 5.00
#valordolar = valorreais / cotacaodolar
#print(f"Com R$ {valorreais:.2f}, você pode comprar US$ {valordolar:.2f}.")
#---------------------------------------------
# tarefa 16
#lado = float(input("Digite o valor de um dos lados"))
#area = lado**2
#print(f"A área de um quadrado com lado = {lado} é {area:.2f}.")
#---------------------------------------------
# tarefa 17
#b = float(input("Digite a largura"))
#h = float(input("Digite a altura"))
#area = b * h 
#print (f"A área de um retângulo com base = {b} e altura = {h} é {area:.2f}.") 
#---------------------------------------------
# tarefa 18
#b = float(input("Digite a largura"))
#h = float(input("Digite a altura"))
#area = (b * h)/2
#print (f"A área de um triangulo com base  = {b} e altura = {h} é {area:.2f}.")
#---------------------------------------------
# tarefa 19
#raio =float(input("Digite o valor do raio de um circulo")) 
#pi = 3.14
#area = pi * (raio **2)
#print (f"A área de um círculo com raio  = {raio} é {area:.2f}.")
#---------------------------------------------
# tarefa 20
#b = float(input("Digite a largura"))
#h = float(input("Digite a altura"))
#perimetro = b*2 + h*2
#print(f"O perimetro de um retangulo com a base ={b} e altura = {h} é{perimetro:.2f}. ")
#---------------------------------------------
# tarefa 21
#nota1 = float(input("Digite uma nota"))
#nota2 = float(input("Digite uma nota"))
#nota3 = float(input("Digite uma nota"))
#media = (nota1 +nota2 +nota3 ) / 3
#print(f"A média aritmética é: {media:.2f}")
#---------------------------------------------
# tarefa 22
#s = float(input("Digite o salario por hora"))
#h = float(input("Digite as horas trabalhadas no mes"))
#sb = s * h 
#print(f"O seu salário bruto este mês é: R$ {sb:.2f}") 
#---------------------------------------------
# tarefa 23
#s = float(input("Digite o salario"))
#aumento = s * 0.10
#novoS = s + aumento
#print(f"salario atual = {s:.2f}")
#print(f" aumento de 10% = {aumento:.2f}")
#print(f"salario com o aumento = {novoS:.2f}")
#---------------------------------------------
# tarefa 24
#precooriginal = float(input("Digite o preço do produto R$ "))
#vd = precooriginal * 0.15
#pf = precooriginal - vd
#print(f"Valor do desconto (15%) R$ {vd:.2f}")
#print(f"Preço final com desconto R$ {pf:.2f}")
#---------------------------------------------
# tarefa 25
#vt = float(input("Digite o valor total da compra R$ "))
#tp = int(input("Digite a quantidade de parcelas "))
#vp = vt / tp
#print(f"Sua compra de R$ {vt:.2f} parcelada em {tp}x fica em")
#print(f"Valor de cada parcela R$ {vp:.2f} sem juros")
#---------------------------------------------
# tarefa 26
#p = float(input("Digite o seu peso (kg) "))
#al = float(input("Digite a sua altura (m) "))
#imc = p / (al ** 2)
#print(f"O seu IMC é = {imc:.2f}")
#---------------------------------------------
# tarefa 27
#nota1 = float(input("Digite a primeira nota (peso 2) "))
#nota2 = float(input("Digite a segunda nota (peso 3) "))
#peso1 = 2
#peso2 = 3
#mp = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
#print(f"A média ponderada é = {mp:.2f}")
#---------------------------------------------
# tarefa 28
#num1 = int(input("Digite o primeiro número inteiro (dividendo) "))
#num2 = int(input("Digite o segundo número inteiro (divisor) "))
#quociente = num1 // num2
#resto = num1 % num2
#print(f"Quociente da divisão inteira = {quociente}")
#print(f"Resto da divisão = {resto}")
#---------------------------------------------
# tarefa 29
# Solicita um número inteiro ao usuário
#numero = int(input("Digite um número inteiro"))
#antecessor = numero - 1
#sucessor = numero + 1
#print(f"O antecessor de {numero} é {antecessor}")
#print(f"O sucessor de {numero} é {sucessor}")
#---------------------------------------------
# tarefa 30
#base = float(input("Digite o valor da base"))
#expoente = float(input("Digite o valor do expoente"))
#resultado = base ** expoente
#print(f"O resultado de {base} elevado a {expoente} é {resultado}")
#---------------------------------------------
# tarefa 31
#numero = float(input("Digite um número "))
#if numero > 0:
#print("O número é positivo.")
#elif numero < 0:
#print("O número é negativo.")
#else:
 #print("O número é igual a zero.")
# tarefa 32
# tarefa 33
# tarefa 34
# tarefa 35
# tarefa 36
# tarefa 37
# tarefa 38
# tarefa 39
# tarefa 40
# tarefa 41
# tarefa 42
# tarefa 43
# tarefa 44
# tarefa 45
# tarefa 46
# tarefa 47
# tarefa 48
# tarefa 49
# tarefa 50
# tarefa 51
# tarefa 52
# tarefa 53
# tarefa 54
# tarefa 55
# tarefa 56
# tarefa 57
# tarefa 58
# tarefa 59
# tarefa 60
# tarefa 61
# tarefa 62
# tarefa 63
# tarefa 64
# tarefa 65
# tarefa 66
# tarefa 67
# tarefa 68
# tarefa 69
# tarefa 70
# tarefa 71
# tarefa 72
# tarefa 73
# tarefa 74
# tarefa 75
# tarefa 76
# tarefa 77
# tarefa 78
# tarefa 79
# tarefa 80
# tarefa 81
# tarefa 82
# tarefa 83
# tarefa 84
# tarefa 85
# tarefa 86
# tarefa 87
# tarefa 88
# tarefa 89
# tarefa 90
# tarefa 91
# tarefa 92
# tarefa 93
# tarefa 94
# tarefa 95
# tarefa 96
# tarefa 97
# tarefa 98
# tarefa 99
# tarefa 100
# tarefa 101
# tarefa 102
# tarefa 103
# tarefa 104
# tarefa 105
# tarefa 106
# tarefa 107
# tarefa 108
# tarefa 109
# tarefa 110
# tarefa 111
# tarefa 112
# tarefa 113
# tarefa 114
# tarefa 115
# tarefa 116
# tarefa 117
# tarefa 118
# tarefa 119
# tarefa 120
# tarefa 121
# tarefa 122
# tarefa 123
# tarefa 124
# tarefa 125
# tarefa 126
# tarefa 127
# tarefa 128
# tarefa 129
# tarefa 130
# tarefa 131
# tarefa 132
# tarefa 133
# tarefa 134
# tarefa 135
