def is_positive(num):
    '''=========================================================================
    Método que recebe um numero e determina se é positivo.
    ========================================================================='''
    if num >= 0:
        return True
    return False

def is_growing(num):
    '''=========================================================================
    Método que recebe um nomero e determina se é um numero crescente.
    ========================================================================='''
    # converto em uma string
    string = str(num)
    # itero sobre string
    for i in range(len(string)-1):
        # verifico se o proximo é crescente
        if string[i+1] < string[i]:
            # se não for retorno False
            return False
    return True

def is_decreasing(num):
    '''=========================================================================
    Método re recebe um numero e determina se é decrescente.
    ========================================================================='''
    # converto em uma string
    string = str(num)
    # itero sobre string
    for i in range(len(string)-1):
        # verifico se o proximo é decrescente
        if string[i+1] > string[i]:
            # se não for retorno False
            return False
    return True

def is_bouncy(num):
    '''=========================================================================
    Método que recebe um numero e determina se é saltitante.
    ========================================================================='''
    # caso não seja nem crescente e em descrescente
    if not is_growing(num) and not is_decreasing(num):
        # retornoi True
        return True
    return False
