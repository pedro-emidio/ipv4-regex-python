import re

# compiler para ler:
ip_reg_exp = re.compile(r'''
    ^ #começa com
        (?: # não sera salvo na memoria
            (?: # não sera salvo na memoria
                #ranges
                25[0-5]|
                2[0-4][0-9]|
                1[0-9]{2}|
                [1-9][0-9]|
                [0-9]
            )
            \.? # escapa o ponto e o deixa opicional
        ){4} # repete 4 vezes
        \b # borda para garantir que não exista um ponto no final, ja que é opcional
    $ # termina com 

''', flags=re.X)
# para cópia:
ip_reg_exp = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$')
for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(f'ip de teste: {ip}    |    ip valido: {ip_reg_exp.findall(ip)}')