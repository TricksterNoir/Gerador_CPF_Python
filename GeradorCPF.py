import random

nove_digitos = ''
digito1 = 0
digito2 = 0
num_digitos_gerados = 0

while num_digitos_gerados < 9:
    nove_digitos += str(random.randrange(10))
    num_digitos_gerados += 1

def calcula_digito(nums, qtd_digitos):

    """
        Nessa classe se tem como parametro os 9 digitos criados anteriormente e a quantidade de dígitos
         uma vez que para calcular o primeiro dígito do CPF se multiplicam os números do CPF começando 
         no 10 até o 2 e para o segundo digito a multiplicação começa em 11.
    """

    resultado_soma = 0
    contador = int(qtd_digitos)
    for numero in nums:
        resultado_soma += int(numero) * contador
        contador -= 1
    resultado_soma = (resultado_soma * 10) % 11

    return resultado_soma

digito1 = calcula_digito(nove_digitos,10)
digito2 = calcula_digito(nove_digitos+str(digito1),11)

print(f'CPF Válido gerado: {nove_digitos}{digito1}{digito2}')