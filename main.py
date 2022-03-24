def valid(choice):
    global num

    while True:
        try:
            num = int(input(choice))
            if num != 1 and num != 2 and num != 3:
                print('Opção inválida.')
            else:
                break
        except ValueError:
            print('Opção inválida.')
    return num


def criaarquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'wt+')
        a.close()
    except:
        print('Ops! Algo deu errado...')
    else:
        print('Arquivo {} criado com sucesso \n'.format(nomearquivo))


def verarquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cadastrarjogo(nomearquivo, exame, mes, animal):
    try:
        a = open(nomearquivo, 'at')
    except:
        print('Ops! Algo deu errado...')
    else:
        a.write('Tipo de Exame: {}               Mês: {}             Paciente: {}\n'.format(exame, mes, animal))
    finally:
        a.close()


def lerjogo(nomearquivo):
    try:
        a = open(nomearquivo, 'rt')
    except:
        print('Ops! Algo deu errado...')
    else:
        print(a.read())
    finally:
        a.close()


# programa principal
arquivo = 'exames.txt'
if verarquivo(arquivo):
    print('Arquivo {} localizado...'.format(arquivo))
else:
    print('Arquivo não encontrado...')
    criaarquivo(arquivo)

while True:
    print('*-------------------------------------------------------------------------------------------*')
    print('|                                           MENU                                            |')
    print('*-------------------------------------------------------------------------------------------*')
    print('1 -> Cadastrar novo exame')
    print('2 -> Ver exames')
    print('3 -> Sair')
    print(' ')

    valid('Selecione a opção desejada: ')
    print('')
    choice = num

    if choice == 1:
        print('Cadastrando novo exame... \n')
        exame = input('Tipo de Exame: ')
        mes = input('Mês: ')
        nomepaciente = input('Nome do paciente: ')
        cadastrarjogo(arquivo, exame, mes, nomepaciente)

    elif choice == 2:
        print('Acessando exames realizados... \n')
        print(lerjogo(arquivo))


    elif choice == 3:
        print('Encerrando o programa...')
        break
