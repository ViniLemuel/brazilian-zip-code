import PySimpleGUI as sg

 
def tela_cep():
    sg.theme('DarkBlue')

    cep = [ 
        [sg.Text('Informe o CEP (Apenas números)', font= 'arial 12', pad=(0, 0))],
        [sg.Input(size=(30, 0), font= 'arial 12 bold', pad=(0, 0), key='cep')],
        [sg.Button('Consultar', font='arial 12', size=(10, 1)) , sg.Button('Sair', font='arial 12', size=(10, 1))]]

    coluna1 = [
        [sg.Text('LOGRADOURO:', font='arial 12')],
        [sg.Text('BAIRRO:', font='arial 12')],
        [sg.Text('LOCALIDADE:', font='arial 12')],
        [sg.Text('UF:', font='arial 12')],
        [sg.Text('DDD:', font='arial 12')] ]

    coluna2 = [
        [sg.Input(font='arial 12 bold', background_color='white',key='logradouro', size=(35, 1))],
        [sg.Input(font='arial 12 bold', background_color='white',key='bairro', size=(30, 1))],
        [sg.Input(font='arial 12 bold', background_color='white',key='localidade', size=(30, 1))],
        [sg.Input(font='arial 12 bold', background_color='white',key='uf', size=(4, 1))],
        [sg.Input(font='arial 12 bold', background_color='white',key='ddd', size=(4, 1))]]

    botoes = [
        [sg.Button('Voltar', font='arial 12', size=(8, 1))],
        [sg.Text(' ' * 5)],
        [sg.CButton('Sair', font='arial 12', size=(8, 1))]]

    layout = [
        [sg.Column(cep, justification='center', element_justification='center')],
        [sg.Column(coluna1, pad=((0, 20), 0)), sg.Column(coluna2)],
        [sg.Column(botoes, justification='center')]]

    janela = sg.Window('Consultar CEP', element_padding=(0, 10), layout=layout, size=(500, 380), finalize= True)

