from funcao import *
raio, lado, area, opcao = 0, 0, 0, 0

while opcao not in (1, 2, 3):
    txt_introcucao()
    opcao = opcao_f()

    if opcao not in (1, 2, 3):
        opcao_invalida()

if opcao == 1:
    area = receber_lado()

elif opcao == 2:
    area = receber_raio()
else:
    area = receber_triangulo()

massage_exit(area)
