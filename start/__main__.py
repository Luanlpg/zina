from core import is_bouncy

def is_99_percent(num):
    '''=========================================================================
    Método que recebe um numero e determina se os 99% foram atingidos.
    ========================================================================='''
    bouncy = 0
    # para cada numero
    for i in range(num):
        # verifico se é bouncy
        if is_bouncy(i):
            # se for adc um em bouncy
            bouncy += 1
    # verifico pocentagem de bouncy
    percent = 100 - ((num - bouncy) / bouncy * 100)
    # se for maior ou igual a 99
    if percent >= 99:
        # retorno True
        return True, percent
    return False, percent

init = 21780
interval = 1000000
result = 0

# itero por 7 vezes para melhorar performance
for i in range(7):
    # itero com intervalos e numeros iniciais diferentes
    for i in range(init, 9999999999, interval):
        bool, percent = is_99_percent(i)
        # caso passe de 99%
        if bool == True:
            print(percent,'% - ', i)
            result = i
            # paro loop
            break
        print(percent,'% - ', i)
    # set variavel inicial e de intervalo
    init = result - interval
    interval = int(interval/10)
# retorno resultado
print('==============================================')
print(f'================={result}======================')
print('==============================================')
