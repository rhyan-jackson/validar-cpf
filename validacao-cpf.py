from random import randint

def validarCPF(cpf):
    # Transformando CPF em somente numérico.
    cpf = str(cpf)
    cpf_formatado = ''.join(c for c in cpf if c.isnumeric())
    if len(cpf_formatado) != 11:
        print('CPF inválido. Insira um CPF com 11 dígitos numéricos exatamente.')
    else:
        
        # Multiplicação dos dígitos pelos seus respectivos pesos(fórmula).
        
        cpf9digitos = cpf_formatado[:9]
        cpf10digitos = cpf_formatado[:10]
        cpf2digitos = cpf_formatado[9:]
        somaformula = 0
        for x, digito in enumerate(cpf9digitos):
            multiplicacao_com_digito = (x+1) * int(digito)
            somaformula += multiplicacao_com_digito
            
        # Descobrindo o primeiro digito pelo resto da somaformula por 11.
        
        digito1 = somaformula % 11
        if digito1 == 10: # Se o resto é 10 usa-se o 0 como indicador.
            digito1 = 0
        
        # Multiplicação dos dígitos pelos seus respectivos pesos(fórmula).
        
        somaformula = 0
        for x, digito in enumerate(cpf10digitos):
            multiplicacao_com_digito = (x) * int(digito)
            somaformula += multiplicacao_com_digito
            
        # Descobrindo o segundo digito pelo resto da somaformula por 11.
        
        digito2 = somaformula % 11
        if digito2 == 10: # Se o resto é 10 usa-se o 0 como indicador.
            digito2 = 0        
            
        # Finalizando e indicando o resultado da validação.
        c = cpf_formatado
        print(f'O CPF indicado é: {c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}.')
        if str(digito1) == cpf2digitos[0] and str(digito2) == cpf2digitos[1]:
            print('Esse CPF é válido.')
            return True
        else:
            print('Esse CPF não é válido de acordo com a fórmula-geral.')
            return False
        
        
def gerarCPF():
    cpf = f'{randint(100, 999)}{randint(100, 999)}{randint(100, 999)}'
    
    # Calculando os números de verficação.
    
    somaformula = 0
    for x, digito in enumerate(cpf):
        multiplicacao_com_digito = (x+1) * int(digito)
        somaformula += multiplicacao_com_digito
        
    # Descobrindo o primeiro digito pelo resto da somaformula por 11.
    
    digito1 = somaformula % 11
    if digito1 == 10: # Se o resto é 10 usa-se o 0 como indicador.
        digito1 = 0
    
    # Multiplicação dos dígitos pelos seus respectivos pesos(fórmula).
    
    somaformula = 0
    cpf_maisdigito1 = cpf + str(digito1)
    for x, digito in enumerate(cpf_maisdigito1):
        multiplicacao_com_digito = (x) * int(digito)
        somaformula += multiplicacao_com_digito
        
    # Descobrindo o segundo digito pelo resto da somaformula por 11.
    
    digito2 = somaformula % 11
    if digito2 == 10: # Se o resto é 10 usa-se o 0 como indicador.
        digito2 = 0      
    
    c = cpf_maisdigito1 + str(digito2)
    print(f'O CPF gerado é: {c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}.')
    return c
    
            
if __name__ == '__main__':
    cpf = gerarCPF()
    validarCPF(cpf)