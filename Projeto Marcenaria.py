# SISTEMA PARA ORÇAMENTO MARCENARIA.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from time import sleep
import os
from progress.bar import Bar

# CORES
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
branco = "\033[1;97;1m"


with Bar('Carregando Sistema:', fill=CYAN+'■'+RESET, suffix='%(percent)d%%') as bar:
    for i in range(100):
        sleep(0.06)
        bar.next()
os.system('cls||clear') 

cont = 0
s = 0
while True:
    print('\033[1;30;107m* \033[m'*30)
    print('{:^73}'.format('\033[1;32;40;1m ORÇAMENTO FÁCIL MARCENARIA\033[m '))
    print('\033[1;30;107m* \033[m'*30)
    print('\n\n{:=^75}' .format(' \033[1;33;40;1mMENU PRINCIPAL\033[m '))

    print('''\n\033[;1mCADASTRO DE CLIENTES:\033[m \033[1;30m
[0] - CADASTRAR CLIENTE:
[1] - CONSULTAR CLIENTE CADASTRADO:
[2] - EXCLUIR CADASTRO:
[3] - ENVIAR ORÇAMENTO POR EMAIL:\033[m
	
\033[;1mOPÇÕES DE ORÇAMENTO:\033[m \033[1;30m
[4] - ORÇAMENTO POR M²: 
[5] - PREÇO MATERIAL x 2:
[6] - MATERIAL x 3:
[7] - CALCULADORA DE TAXAS E PRAZOS:	
[8] - AJUDA [DICAS IMPORTANTES]
[9] - SAIR\033[m''')
    print('='*60)
    opção = int(input(branco+'Sua Opção: '+RESET))
    os.system('cls||clear')
    sleep(0.4)

# ENVIAR ARQUIVOS POR EMAIL:
    if opção == 3:
        print('{:=^75}' .format(
            ' \033[1;33;40;1mENVIAR ORÇAMENTO POR E-MAIL\033[m '))
        try:
            fromaddr = ("mauro.mn@hotmail.com")
            print(GREEN + '\nEmail do cliente:' + RESET)
            toaddr = input("")
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Orçamento marcenaria"
            body = "\nTeste Envio de Email Com Python"
            msg.attach(MIMEText(body, 'plain'))
            filename = 'Orçamento.txt'
            attachment = open('Orçamento9.txt', 'rb')
            part = MIMEBase('application', "txt", Name=filename)
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            "attachment; filename= %s" % filename)
            msg.attach(part)
            attachment.close()
            server = smtplib.SMTP('smtp.outlook.com', 587)
            server.starttls()
            server.login(fromaddr, "ISIS2015")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
            print(GREEN + '\nE-MAIL ENVIADO COM SUCESSO!' + RESET)
        except:
            print(RED + "\nErro ao enviar email" + RESET)

    if opção == 2:
        print('\n\033[1;32;40mCADASTRO EXCLUÍDO COM SUCESSO!\033[m')
        arquivo = open('Orçamento9.txt', 'w')

# Salvando dados em arquivo de texto.
    if opção == 0:
        while True:
            print('{:=^73}' .format(' \033[1;33;40mCADASTRAR CLIENTE\033[m '))
            arquivo = open('Orçamento9.txt', 'a')
            cliente = (input('\n_ Nome do cliente: ')) .title()
            telefone = input('_ Nº de telefone: ').strip()
            ambiente = input('_ Ambiente Orçado: ')
            movel = input('_ Tipo de móvel: ')
            arquivo.write('\n\nDADOS DO CLIENTE:\n')
            arquivo.write(f'Cliente: {cliente}\n')
            arquivo.write(f'Telefone: {telefone}\n')
            arquivo.write(f'Ambiente: {ambiente}\n')
            arquivo.write(f'Movel: {movel}\n')
            arquivo.close()
            os.system('cls||clear')
            sleep(0.4)
            print('{:=^73}' .format(' \033[1;33;40mCADASTRAR CLIENTE\033[m '))
            print('Cliente:', cliente)
            print('Telefone:', telefone)
            print('Ambiente:', ambiente)
            print('Móvel:', movel)
            sleep(0.7)
            print('\n\033[1;32;40mCADASTRO REALIZADO COM SUCESSO!!!\033[m')
            cadastrar = input(
                '\nDeseja cadastrar outro cliente? [S/N]: ').upper() .strip()
            print('_'*60)
            if cadastrar == 'N':
                break
            os.system('cls||clear')

# Lendo dados do arquivo de texto.
    if opção == 1:
        with open("Orçamento9.txt", "r") as arquivo:
            dados = arquivo.read()
        print(str(dados))

    if opção == 4:
        print('{:=^73}' .format(' \033[1;33;40mORÇAMENTO POR M²\033[m '))
        altura = float(
            input('\nDigite a altura do móvel em metros: --->Exemplo: 2.60\nAltura: '))
        largura = float(
            input('Digite a largura do móvel em metros:\nLargura: '))
        preçom2 = float(input('Digite o valor do metro quadrado:\nR$: '))
        m2 = altura * largura
        orçamento1 = altura * largura * preçom2
        cont += 1
        s += orçamento1
        sleep(0.4)
        print('='*30)
        print(f'\033[1;30mMEDIDA TOTAL M² ==> {m2:.2f}M²\033[m')
        arquivo = open('Orçamento9.txt', 'a')
        medida = (f'MEDIDA TOTAL M² ==> {m2:.2f}M²\n')
        arquivo.write(f'{medida}')
        print(f'\033[1;30mPREÇO DO MÓVEL ==> R${orçamento1:.2f}\033[m')
        arquivo = open('Orçamento9.txt', 'a')
        preco = (f'PREÇO DO MÓVEL: R${orçamento1:.2f}')
        arquivo.write(f'{preco}\n')
        arquivo.write('='*60)

        print('='*30)

    if opção in (5, 6):
        sleep(0.4)
        print('{:=^73}' .format(
            ' \033[1;33;40mORÇAMENTO SOB PREÇO DO MATERIAL\033[m '))
        material = float(input('\nDigite o valor de todo o material:\nR$ '))
        sleep(0.4)
        orçamento2 = material * 2
        orçamento3 = material * 3
        cont += 1
        s += orçamento2

        print('='*29)
        print('\033[1;34mORÇAMENTO 2:\033[m')
        print(f'\033[1;30mPREÇO DO MÓVEL ==> R${orçamento2:.2f}\033[m')
        print('\033[1;34m\nORÇAMENTO 3:\033[m')
        print(f'\033[1;30mPREÇO DO MÓVEL ==> R${orçamento3:.2f}\033[m')
        arquivo = open('Orçamento9.txt', 'a')
        preco1 = (f'PREÇO DO MÓVEL: R${orçamento3:.2f}')
        arquivo.write(f'{preco1}\n')
        print('='*29)

    if opção == 8:
        sleep(0.4)
        print('\n\n{:=^73}' .format(' \033[1;33;40mDICAS IMPORTANTES\033[m '))
        print(
            '\033[1;37m\nDúvidas? Veja abaixo algumas dicas para cada opção escolhida\033[m')
        print('\033[1;33m\nDica 1 - Orçamento por M²:\033[m')
        print('''\33[1;30mAs medidas deverão ser inseridas em Metros, não use vírgula,use somente ponto quando a medida não for exata. O valor do metro² não deverá conter ponto e nem vírgula.
EXEMPLO: 
medida exata = 2  [ sem ponto ]
medida não exata = 2.60 [ com ponto ]
Preço do Metro² = R$ 1200
Preço do Móvel = 2 x 2.60 x 1200
Preço do Móvel = R$ 6240\033[m''')
        print('\033[1;33m\nDica 2 - Material x 2 ou x 3\033[m')
        print('''\033[1;30mDeverá ser inserido o valor total da matéria-prima para fabricação do móvel e multiplicar por 2  ou 3.
EXEMPLO:
Preço Material = R$ 2300
Preço do Móvel = R$2300 x 2
Preço do Móvel = R$ 4600
Obs: O sistema fará os cálculos automaticamente.\033[m''')
        print('\033[1;33m\nDica 3 - Calculadora de Taxas e Prazos:\033[m')
        print('''\033[1;30mA calculadora de taxas foi projetada para auxiliar na hora do orçamento, possibilitando ao usuário o cáculo das taxas e prazos no próprio sistema.\033[m''')
        print('_'*60)

    if opção == 7:
        sleep(0.4)
        print('\n{:=^73}'  .format(
            '\033[1;32;40m CALCULADORA DE TAXAS E PRAZOS\033[m '))

        vp = float(input('\nQUAL O VALOR DO MÓVEL?\nR$:'))
        sleep(0.4)

        fp = int(input('''\033[1;30mSELECIONE A FORMA DE PAGAMENTO:
[1] DINHEIRO/PIX À VISTA:
[2] CARTÃO DE DÉBITO A VISTA:
[3] 3x OU MAIS NO CARTÃO COM JUROS:
[4] ATÉ 2x SEM JUROS NO CARTÃO:
QUAL A OPÇÃO? \033[m'''))

# FORMAS DE PAGAMENTO
        fp1 = vp - (vp * 10 / 100)
        fp2 = vp - (vp * 5 / 100)
        fp3 = vp / 2
        fp4 = vp + (vp * 10 / 100)
        fp5 = vp
# PARCELAMENTO
        p1 = vp
        p2 = vp / 2
        p3 = (vp + vp * 10 / 100) / 3
        p4 = (vp + vp * 10 / 100) / 4
        p5 = (vp + vp * 10 / 100) / 5
        p6 = (vp + vp * 10 / 100) / 6
        p7 = (vp + vp * 10 / 100) / 7
        p8 = (vp + vp * 10 / 100) / 8
        p9 = (vp + vp * 10 / 100) / 9
        p10 = (vp + vp * 10 / 100) / 10
        p11 = (vp + vp * 10 / 100) / 11
        p12 = (vp + vp * 10 / 100) / 12

        if fp == 1:
            sleep(0.4)
            print('='*60)
            print(
                f'\033[1;34;40mNO DINHEIRO OU PIX O VALOR A SER PAGO SERÁ DE R${fp1:.2f}\033[m')
            print('='*60)

        if fp == 2:
            sleep(0.4)
            print('='*60)
            print(
                f'\033[1;34;40mNO CARTÃO A VISTA O VALOR A SER PAGO SERÁ DE R${fp2:.2f}\033[m')
            print('='*60)

        if fp == 3:
            sleep(0.4)
            p = int(input(f'''
OPÇÕES DE PARCELAMENTO COM JUROS:
3x --> 3x de R${p3:.2f}
4x --> 4x de R${p4:.2f}
5x --> 5x de R${p5:.2f}
6x --> 6x de R${p6:.2f}
7x --> 7x de R${p7:.2f}
8x --> 8x de R${p8:.2f}
9x --> 9x de R${p9:.2f}
10x --> 10x de R${p10:.2f}
11x --> 11x de R${p11:.2f}
12x --> 12x de R${p12:.2f}
EM QUANTAS VEZES DESEJA PARCELAR? '''))
            sleep(0.4)
            parcelas = fp4 / p
            print('='*60)
            print(f'''\033[1;34;40mO TOTAL DA SUA COMPRA COM JUROS É DE R${fp4:.2f}
A SUA COMPRA SERÁ PARCELADA EM {p}x DE R${parcelas:.2f}\033[m''')
            print('='*60)

        if fp == 4:
            sleep(0.4)
            psj = int(input(f'''
OPÇÕES DE PARCELAMENTO SEM JUROS:

1x --> 1x de R${p1:.2f} SEM JUROS.

2x --> 2x de R${p2:.2f} SEM JUROS.

EM QUANTAS VEZES DESEJA PARCELAR? '''))
            sleep(0.4)
            parcela1 = fp5 / psj
            print('='*60)
            print(
                f'\033[1;34;40mA SUA COMPRA SERÁ PARCELADA EM {psj}x DE R${parcela1:.2f}\033[m')
            print('='*60)

    if opção == 9:
        break
    if opção not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
        print('opção inválida')
    print('_'*60)
    print(f'\nSoma de todos os orçamentos: R${s:.2f}')
    print(f'Total de Orçamentos: {cont}')
    print('_'*60)

    continuar = str(input(
        '\033[1;37m\nDESEJA VOLTAR AO MENU PRINCIPAL? [ S / N ]:\033[m ')).upper() .strip()[0]
    sleep(0.4)
    os.system('cls||clear')

    if continuar == 'N':
        break

sleep(0.4)
print('\n\n{:×^70}'.format('\033[1;32m ORÇAMENTO FINALIZADO\033[m '))
