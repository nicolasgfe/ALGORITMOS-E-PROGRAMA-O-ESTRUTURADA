from math import pi


def txt_introcucao():
    print("Escolha uma opção para calcular a área:\n1 - Quadrado \n2 - Círculo \n3 - Triângulo")


def receber_lado() -> float:
    lado = float(input('Informe o lado do quadrado: '))
    return lado ** 2


def receber_raio() -> float:
    raio = float(input('Informe o raio do círculo: '))
    area = pi * raio ** 2
    return area


def receber_triangulo() -> float:
    base = float(input('Informe a base do triângulo: '))
    altura = float(input('Informe a altura do triângulo: '))
    area = (base * altura) / 2
    return area


def opcao_f() -> int:
    opcao = int(input('--> '))
    return opcao


def opcao_invalida() -> str:
    print('** Opção inválida **')


def massage_exit(area: float):
    print(f"A área é: {area:.2f}",)