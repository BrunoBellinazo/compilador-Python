#SIMPLE TO SML (TRABALHO DE COPILADORES);

#Feito por Bruno Lopes Bellinazo - 1912082041

#variaveis globais
constantes = []
variaveis = []
sml = {}

#Le o arquivo e transforma em um dicionario e conta as variaveis, operacoes e instrucoes, fazendo a primeira passagem ;
def ler_txt(codigo_simple) -> dict:
    linhas_codigo = {}
    global constantes
    global variaveis
    global sml
    ordem = 0
    
    try:
        with open(codigo_simple, mode='r', encoding='utf8') as arquivo:

            for linha in arquivo:
                linha = linha.strip()

                partes = linha.split(' ',1)
                instrucao = int(partes[0])
                codigo = partes[1]

                linhas_codigo[instrucao] = codigo
                codigo_dividido = codigo.split(' ', 1)
                primeira_palavra = codigo_dividido[0]

                if primeira_palavra == 'rem':
                    continue

                elif primeira_palavra == 'input':

                    if codigo_dividido[1] not in variaveis :
                        variaveis.append(codigo_dividido[1])

                    codigo_convertido = '+10'
                    sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                    ordem += 1

                elif primeira_palavra == 'let':

                    partes = codigo_dividido[1].split(' = ')

                    codigo_convertido = '+20'
                    sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                    ordem += 1
                    
                    if partes[0] not in variaveis :  #add a variavel
                        variaveis.append(partes[0])

                    if partes[1].isdigit() or (partes[1].startswith('-') and partes[1][1:].isdigit()) :  #verifica se e um numero

                        if partes[1] not in constantes :
                            constantes.append(partes[1])

                        codigo_convertido = '+21'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                    elif any(op in partes[1] for op in ('+', '-', '*', '/', '%')):  #verifica se e uma exprecao

                        verifica = partes[1].split(' ', 1)

                        if verifica[0].isdigit() or (verifica[0].startswith('-') and verifica[0][1:].isdigit()) :
                            
                            if verifica[0] not in constantes :
                                constantes.append(verifica[0])

                        if verifica[1].strip()[-1].isdigit():

                            cons = verifica[1].strip()[-1]
                            if cons not in constantes :
                                constantes.append(cons)

                        if ' + ' in partes[1] :
                            codigo_convertido = '+30'
                            sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                            ordem += 1

                            codigo_convertido = '+21'
                            sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                            ordem += 1

                        elif ' - ' in partes[1] :
                            codigo_convertido = '+31'
                            sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                            ordem += 1

                            codigo_convertido = '+21'
                            sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                            ordem += 1

                        elif ' / ' in partes[1] :
                            codigo_convertido = '+32'
                            sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                            ordem += 1

                            codigo_convertido = '+21'
                            sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                            ordem += 1

                        elif ' * ' in partes[1] :
                            codigo_convertido = '+33'
                            sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                            ordem += 1

                            codigo_convertido = '+21'
                            sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                            ordem += 1

                        elif ' % ' in partes[1] :
                            codigo_convertido = '+34'
                            sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                            ordem += 1

                            codigo_convertido = '+21'
                            sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                            ordem += 1

                    else : #e uma variavel

                        codigo_convertido = '+21'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                elif primeira_palavra == 'print':

                    codigo_convertido = '+11'
                    sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                    ordem += 1

                elif primeira_palavra == 'goto':

                    codigo_convertido = '+40'
                    sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                    ordem += 1

                elif primeira_palavra == 'if':

                    verifica_se_num = codigo_dividido[1].split('goto')
                    antes_do_goto = verifica_se_num[0].split()[-1]
                    #print(f'Verifica se num:{verifica_se_num}')
                    #print(f'ANTES DO GOTO:{antes_do_goto}')
                    #print(type(antes_do_goto))
                    
                    if antes_do_goto.isdigit():

                        if antes_do_goto not in constantes:

                            constantes.append(antes_do_goto)


                    if '!=' in codigo_dividido[1]:

                        codigo_convertido = '+20'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                        if antes_do_goto != '0':

                            codigo_convertido = '+34'
                            sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                            ordem += 1

                        codigo_convertido = '+42'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                        codigo_convertido = '+40'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                    elif '==' in codigo_dividido[1]:

                        codigo_convertido = '+20'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                        if antes_do_goto != '0':

                            codigo_convertido = '+34'
                            sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                            ordem += 1

                        codigo_convertido = '+42'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                    elif '>=' in codigo_dividido[1] or '<=' in codigo_dividido[1]:

                        codigo_convertido = '+20'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                        codigo_convertido = '+31'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                        codigo_convertido = '+41'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                        codigo_convertido = '+42'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1    
                                        
                    elif '>' in codigo_dividido[1] or '<' in codigo_dividido[1]:

                        codigo_convertido = '+20'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                        codigo_convertido = '+31'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                        codigo_convertido = '+41'
                        sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                        ordem += 1

                elif primeira_palavra == 'end':

                    codigo_convertido = '+43'
                    sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                    ordem += 1

            for item in variaveis: #adiciona as variavei

                codigo_convertido = '+0000'
                instrucao = item
                sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                ordem += 1

            for item in constantes:

                instrucao = item

                if item.startswith('-'):

                    item_int = int(item[1:])

                    codigo_convertido = f'-{item_int:04}'
                    sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                    ordem += 1

                else:
                    item_int = int(item)

                    codigo_convertido = f'+{item_int:04}'
                    sml[ordem] = {'codigo': codigo_convertido, 'anterior': instrucao}
                    ordem += 1

    except FileNotFoundError:
        print(f"O arquivo {codigo_simple} nao foi encontrado.")

    except Exception as excepition:
        print(f"Ocorreu um erro: {excepition}")

    return linhas_codigo

def aloca_variavel(linhas_codigo):

    global sml

    try:

        for key, linha in linhas_codigo.items():
            #print(f'linha:{linha}')
            #print(f'key:{key}')

            codigo_dividido = linha.split(' ', 1)
            #print(f'codigo[0]:{codigo_dividido[0]}')
            #print(f'codigo[1]:{codigo_dividido[1]}')

            primeira_palavra = codigo_dividido[0]

            if primeira_palavra == 'rem':
                continue

            if primeira_palavra == 'input':

                procura_variavel = codigo_dividido[1]
                #print(f'codigo_dividido[1]:{codigo_dividido[1]}')
                
                for chave, valor in sml.items():
                    if valor['anterior'] == procura_variavel:
                        #print(f'procura:{procura_variavel}')
                        #print(f'chave e essa:{chave}')
                        #print(f'valor e esse:{valor}')

                        for end, val in sml.items():
                            if val['anterior'] == key:

                                chave = str(chave).zfill(2)
                                #print(f'endereco e esse:{chave}')
                                val['codigo'] += chave

            elif primeira_palavra == 'let':

                partes = codigo_dividido[1].split(' = ')

                #print(f'partes[0]:{partes[0]}')
                #print(f'partes[1]:{partes[1]}')

                if partes[1].isdigit() or (partes[1].startswith('-') and partes[1][1:].isdigit()) :  #verifica se e um numero

                    #print('ENTROU')
                    procura_var_cons0 = partes[0]
                    procura_var_cons = partes[1]

                    for chave, valor in sml.items():
                        if valor['anterior'] == procura_var_cons:
                            #print(f'procura:{procura_var_cons}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+20':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave

                    for chave, valor in sml.items():
                        if valor['anterior'] == procura_var_cons0:
                            #print(f'procura:{procura_var_cons}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+21':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave

                elif any(op in partes[1] for op in ('+', '-', '*', '/', '%')):  #verifica se e uma exprecao

                    #print('ENTROU @@')

                    separa = partes[1].split(' ', 1)
                    #print(f'separa[0]:{separa[0]}')
                    #print(f'separa[1]:{separa[1]}')
                    
                    procura_var_cons0 = partes[0]
                    procura_var_cons = separa[0]

                    for chave, valor in sml.items():
                        if valor['anterior'] == procura_var_cons:
                            #print(f'procura:{procura_var_cons}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+20':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave

                    for chave, valor in sml.items():
                        if valor['anterior'] == procura_var_cons0:
                            #print(f'procura:{procura_var_cons}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+21':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave

                    if '+ ' in separa[1] :
                        ultimo = separa[1].split()[-1]
                        #print(f'ultimo:{ultimo}')

                        for chave, valor in sml.items():
                            if valor['anterior'] == ultimo:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+30':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                    elif '- ' in separa[1] :
                        ultimo = separa[1].split()[-1]
                        #print(f'ultimo:{ultimo}')

                        for chave, valor in sml.items():
                            if valor['anterior'] == ultimo:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+31':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                    elif '/ ' in separa[1] :
                        ultimo = separa[1].split()[-1]
                        #print(f'ultimo:{ultimo}')

                        for chave, valor in sml.items():
                            if valor['anterior'] == ultimo:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+32':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                    elif '* ' in separa[1] :
                        ultimo = separa[1].split()[-1]
                        #print(f'ultimo:{ultimo}')

                        for chave, valor in sml.items():
                            if valor['anterior'] == ultimo:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+33':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                    elif '% ' in separa[1] :
                        ultimo = separa[1].split()[-1]
                        #print(f'ultimo:{ultimo}')

                        for chave, valor in sml.items():
                            if valor['anterior'] == ultimo:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+34':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                else : #e uma variavel

                    procura_var_cons0 = partes[0]
                    procura_var_cons = partes[1]

                    for chave, valor in sml.items():
                        if valor['anterior'] == procura_var_cons:
                            #print(f'procura:{procura_var_cons}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+20':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave

                    for chave, valor in sml.items():
                        if valor['anterior'] == procura_var_cons0:
                            #print(f'procura:{procura_var_cons}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+21':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave

            elif primeira_palavra == 'print':

                procura_variavel = codigo_dividido[1]

                for chave, valor in sml.items():
                    if valor['anterior'] == procura_variavel:
                        #print(f'procura:{procura_variavel}')
                        #print(f'chave e essa:{chave}')
                        #print(f'valor e esse:{valor}')

                        for end, val in sml.items():
                            if val['anterior'] == key:

                                chave = str(chave).zfill(2)
                                #print(f'endereco e esse:{chave}')
                                val['codigo'] += chave

            elif primeira_palavra == 'goto':

                procura_numero = int(codigo_dividido[1])
                #print(f'codigo:{codigo_dividido[1]}')

                for chave, valor in sml.items():
                    #print(f'Valor:{valor}')
                    #print(type(valor['anterior']))
                    if valor['anterior'] == procura_numero:
                        #print(f'procura:{procura_numero}')
                        #print(f'chave e essa:{chave}')
                        #print(f'valor e esse:{valor}')

                        for end, val in sml.items():
                            if val['anterior'] == key:

                                chave = str(chave).zfill(2)
                                #print(f'endereco e esse:{chave}')
                                val['codigo'] += chave

                        break

            elif primeira_palavra == 'if':

                if '!=' in codigo_dividido[1]:

                    var_num = codigo_dividido[1].split(' != ')
                    #print(f'var_num[0]:{var_num[0]}')
                    #print(f'var_num[1]:{var_num[1]}')
                    endereco = int(var_num[1].split()[-1])
                    #print(f'endereco:{endereco}')
                    num_var = var_num[1].split()[0]
                    #print(f'numero:{num_var}')
                    #print(type(num_var))

                    for chave, valor in sml.items():
                        if valor['anterior'] == var_num[0]:
                            #print(f'procura:{procura_var_cons}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+20':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave

                    if num_var != '0':

                        for chave, valor in sml.items():
                            if valor['anterior'] == num_var:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+34':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                    for chave, valor in sml.items():
                    #print(f'Valor:{valor}')
                    #print(type(valor['anterior']))
                        if valor['anterior'] == key and valor['codigo'] == '+42':
                            soma_end = chave + 2
                            soma_end = str(soma_end).zfill(2)
                            valor['codigo'] += soma_end

                    for chave, valor in sml.items():
                    #print(f'Valor:{valor}')
                    #print(type(valor['anterior']))
                        if valor['anterior'] == endereco:
                            #print(f'procura:{procura_numero}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+40':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave

                            break

                elif '==' in codigo_dividido[1]:

                    var_num = codigo_dividido[1].split(' == ')
                    #print(f'var_num[0]:{var_num[0]}')
                    #print(f'var_num[1]:{var_num[1]}')
                    endereco = int(var_num[1].split()[-1])
                    #print(f'endereco:{endereco}')
                    num_var = var_num[1].split()[0]
                    #print(f'numero:{num_var}')
                    #print(type(num_var))

                    for chave, valor in sml.items():
                        if valor['anterior'] == var_num[0]:
                            #print(f'procura:{procura_var_cons}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+20':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave

                    if num_var != '0':
                    
                        for chave, valor in sml.items():
                            if valor['anterior'] == num_var:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+34':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                    for chave, valor in sml.items():
                    #print(f'Valor:{valor}')
                    #print(type(valor['anterior']))
                        if valor['anterior'] == endereco:
                            #print(f'procura:{procura_numero}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+42':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave

                            break

                elif '>=' in codigo_dividido[1] or '<=' in codigo_dividido[1]:

                    if '>=' in codigo_dividido[1]:

                        var_num = codigo_dividido[1].split(' >= ')
                        #print(f'var_num[0]:{var_num[0]}')
                        #print(f'var_num[1]:{var_num[1]}')
                        endereco = int(var_num[1].split()[-1])
                        #print(f'endereco:{endereco}')
                        num_var = var_num[1].split()[0]
                        #print(f'num_var:{num_var}')

                        for chave, valor in sml.items():
                            if valor['anterior'] == num_var:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+20':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                        for chave, valor in sml.items():
                            if valor['anterior'] == var_num[0]:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+31':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave


                    elif '<=' in codigo_dividido[1]:

                        var_num = codigo_dividido[1].split(' <= ')
                        #print(f'var_num[0]:{var_num[0]}')
                        #print(f'var_num[1]:{var_num[1]}')
                        endereco = int(var_num[1].split()[-1])
                        #print(f'endereco:{endereco}')
                        num_var = var_num[1].split()[0]
                        #print(f'num_var:{num_var}')

                        for chave, valor in sml.items():
                            if valor['anterior'] == var_num[0]:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+20':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                        for chave, valor in sml.items():
                            if valor['anterior'] == num_var:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+31':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                    for chave, valor in sml.items():
                    #print(f'Valor:{valor}')
                    #print(type(valor['anterior']))
                        if valor['anterior'] == endereco:
                            #print(f'procura:{procura_numero}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+41':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave

                    for chave, valor in sml.items():
                    #print(f'Valor:{valor}')
                    #print(type(valor['anterior']))
                        if valor['anterior'] == endereco:
                            #print(f'procura:{procura_numero}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+42':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave
                                    
                elif '>' in codigo_dividido[1] or '<' in codigo_dividido[1]:

                    if '>' in codigo_dividido[1]:

                        var_num = codigo_dividido[1].split(' > ')
                        #print(f'var_num[0]:{var_num[0]}')
                        #print(f'var_num[1]:{var_num[1]}')
                        endereco = int(var_num[1].split()[-1])
                        #print(f'endereco:{endereco}')
                        num_var = var_num[1].split()[0]
                        #print(f'num_var:{num_var}')

                        for chave, valor in sml.items():
                            if valor['anterior'] == num_var:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+20':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                        for chave, valor in sml.items():
                            if valor['anterior'] == var_num[0]:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+31':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave


                    elif '<' in codigo_dividido[1]:

                        var_num = codigo_dividido[1].split(' < ')
                        #print(f'var_num[0]:{var_num[0]}')
                        #print(f'var_num[1]:{var_num[1]}')
                        endereco = int(var_num[1].split()[-1])
                        #print(f'endereco:{endereco}')
                        num_var = var_num[1].split()[0]
                        #print(f'num_var:{num_var}')

                        for chave, valor in sml.items():
                            if valor['anterior'] == var_num[0]:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+20':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                        for chave, valor in sml.items():
                            if valor['anterior'] == num_var:
                                #print(f'procura:{procura_var_cons}')
                                #print(f'chave e essa:{chave}')
                                #print(f'valor e esse:{valor}')

                                for end, val in sml.items():
                                    if val['anterior'] == key and val['codigo'] == '+31':

                                        chave = str(chave).zfill(2)
                                        #print(f'endereco e esse:{chave}')
                                        val['codigo'] += chave

                    for chave, valor in sml.items():
                    #print(f'Valor:{valor}')
                    #print(type(valor['anterior']))
                        if valor['anterior'] == endereco:
                            #print(f'procura:{procura_numero}')
                            #print(f'chave e essa:{chave}')
                            #print(f'valor e esse:{valor}')

                            for end, val in sml.items():
                                if val['anterior'] == key and val['codigo'] == '+41':

                                    chave = str(chave).zfill(2)
                                    #print(f'endereco e esse:{chave}')
                                    val['codigo'] += chave

            elif primeira_palavra == 'end':

                for end, val in sml.items():
                    if val['codigo'] == '+43':

                        val['codigo'] += '00'

    except Exception as excepition:
        print(f"Ocorreu um erro: {excepition}")

    return

linhas_codigo = ler_txt('codigo_simple1.txt')
#print(linhas_codigo)
#print(type(linhas_codigo))
aloca_variavel(linhas_codigo)

arquivo_txt = "codigos.txt"

# Extrair os códigos e salvar no arquivo
with open(arquivo_txt, 'w') as arquivo:
    for item in sml.values():
        arquivo.write(f"{item['codigo']}\n")

'''for key, value in sml.items():
    print(f"{key}: {value}")

print(f'Variaveis:{variaveis}')
print(f'Constantes:{constantes}')'''