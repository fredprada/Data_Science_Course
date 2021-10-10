'''
Informações sobre o como fazer a atividade:

* O script deverá ter o formato: seunome_sobrenome.py (sem espaços)
  Para pessoas com multiplos sobrenomes, colocar apenas o ultimo.
  Caracteres com acentos devem ser substituidos pelo equivalente sem acento.
  
* Não adicione nada no script fora dos locais onde está escrito :
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    
'''

### Seu código inicia aqui ###

nome = 'frederico_loiola_prada' # # coloque aqui o nome completo sem espaços (colocar '_' entre as palavras e.g. gustavo_voltani_von_atzingen) no formato de uma string
CPF = '38691747811' # Coloque seu RG no formato int (sem pontos, traços ou espaços) ex: Se '123.456.789.7':  CPF = 1234567897
data_nascimento = '24/12/1996' # Coloque sua data de nascimento no formato 'dd/mm/aaaa' (string)

### Seu código termina aqui ###


def progressao_aritmetica(a1, r, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão aritmética r 
    e um número inteiro n > 1 e retorna uma lista com os n primeiros termos da progressão aritmética
    
    PA: https://pt.wikipedia.org/wiki/Progress%C3%A3o_aritm%C3%A9tica 
    
    Test
    -----------
    >>> soma_pa(1, 2, 4)
    [1, 3, 5, 7]
    ''' 
    lista_pa = []
    ### Seu código inicia aqui ###	
    lista_pa.append(a1)
    for i in range(n-1):
        lista_pa.append(lista_pa[-1]+r)
    ### Seu código termina aqui ###
    return lista_pa

def soma_pa(a1, r, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão aritmética r 
    e um número inteiro n > 1 e retorna a soma dos n primeiros termos da progressão aritmética
    
    PA: https://pt.wikipedia.org/wiki/Progress%C3%A3o_aritm%C3%A9tica 
    
    Return
    -----------
    soma: int
    
    Test
    -----------
    >>> soma_pa(1, 2, 4)
    16
    '''
    soma = 0
    ### Seu código inicia aqui ###
    lista_pa_soma = []	
    lista_pa_soma.append(a1)
    for i in range(n-1):
        lista_pa_soma.append(lista_pa_soma[-1]+r)
        soma = ((n/2)*(a1+lista_pa_soma[-1]))
    ### Seu código termina aqui ###
    return soma

def progressao_geometrica(a1, q, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão geométrica q 
    e um número inteiro n e retorna uma lista com os n primeiros termos da progressão geométrica
    
    https://pt.wikipedia.org/wiki/Progress%C3%A3o_geom%C3%A9trica 
    
    Test
    -----------
    >>> progressao_geometrica(1, 2, 4)
    [1, 2, 4, 8]
    >>> progressao_geometrica(1, 2, 3)
    [1, 2, 4]
    '''
    pg = []
    ### Seu código inicia aqui ###	
    pg.append(a1)
    for i in range(n-1):
        pg.append(pg[-1]*q)
    ### Seu código termina aqui ###
    return pg

def soma_pg(a1, q, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão geométrica q > 1
    e um número inteiro n e retorna a soma dos n primeiros termos da progressão geométrica
    
    https://pt.wikipedia.org/wiki/Progress%C3%A3o_geom%C3%A9trica
    
    Test
    -----------
    >>> soma_pg(1, 2, 3)
    7
    >>> soma_pg(1, 2, 4)
    15
    '''
    soma_pg = 0
    ### Seu código inicia aqui ###	
    for i in range(n-1):
        soma_pg = (a1 * ((q**n)-1))/(q-1)
    ### Seu código termina aqui ###
    return soma_pg

def fibonacci(n):
    '''
    Crie uma função que recebe um número inteiro n e retorna uma lista com os n primeiros termos da sequência de Fibonacci
    
    https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci  0, 1, 1, 2, 3, 5, 8, ...
    
    Test
    -----------
    >>> fibonacci(4)
    [0, 1, 1, 2]
    >>> fibonacci(2)
    [0, 1]
    '''
    fib = []
    ### Seu código inicia aqui ###
    # N+1 = N + N-1 -> (fib) = (proximo) + (anterior)
    anterior = 0
    proximo = 1
    fib.append(0)
    for i in range (n-1):
        fib.append(proximo + anterior)
        anterior = proximo
        proximo = fib[-1]
    ### Seu código termina aqui ###
    return fib

def soma_fibonacci(n):
    '''
    Crie uma função que recebe um número inteiro n e retorna a soma dos n primeiros termos da sequência de Fibonacci
    
    https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci 0, 1, 1, 2, 3, 5, 8, ...
    
    Test
    -----------
    >>> soma_fibonacci(4)
    4
    >>> soma_fibonacci(5)
    7
    >>> soma_fibonacci(1)
    0
    >>> soma_fibonacci(2)
    1
    '''
    soma = 0
    ### Seu código inicia aqui ###	
    fib=[]
    anterior = 0
    proximo = 1
    fib.append(0)
    for i in range (n-1):
        fib.append(proximo + anterior)
        anterior = proximo
        proximo = fib[-1]
        soma = sum(fib)
    ### Seu código termina aqui ###
    return soma

def primo(n):
    '''
    Crie uma função que recebe um número inteiro n e retorna True se ele é primo e False caso contrário
    Test
    -----------
    >>> primo(7)
    True
    >>> primo(8)
    False
    '''
    resultado = False
    ### Seu código inicia aqui ###	
    a = 2
    if n < a:
        return resultado
    else:
        for i in (a , n):
            if n % a == 0:
                return resultado
                break
            a = a + 1
        else:
            return not resultado

    ### Seu código termina aqui ###
    return resultado

def fit_linear(x, y):
    '''
    Crie uma função que recebe duas listas de números x e y e retorna uma lista com os coeficientes da 
    equação linear [A, B], considerando que y = A + B*x
    
    Test
    -----------
    >>> fit_linear([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    [0, 1]
    
    >>> fit_linear([1, 2, 3, 4, 5], [11, 21, 31, 41, 51])
    [1, 10]
    '''
    A, B = 0, 0
    ### Seu código inicia aqui ###	
    import math
    B = ((y[-1]-y[0])/(x[-1]-x[0]))
    ### Seu código termina aqui ###
    return A, B

if __name__ == '__main__':
    print(progressao_aritmetica(1,2,4))
    print(soma_pa(1,2,4))
    print(progressao_geometrica(1,2,3))
    print(soma_pg(1,2,3))
    print(fibonacci(7))
    print(soma_fibonacci(7))
    print(primo(13))
    print(fit_linear([1,2,3,4,5],[11,21,31,41,51]))