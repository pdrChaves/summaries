# Operador lógico: "and"

senha_permitida = 123
entrada = input(
    '[E]ntrar ou [S]air?: '
                )
if entrada == 'e' or 'E' or 'entrar' or 'Entrar':
    senha_digitada= input(
        'Digite sua senha: '
                          )

if entrada == 'entrar'or 'e' or 'E' or 'Entrar' and int(senha_digitada) == senha_permitida:
    print(
        'Seja bem vindo. '
        )
    
elif entrada == 'sair':
    print(
        'Você saiu.'
        )

else:
    print(
        'Entrda não permitida.'
    )
