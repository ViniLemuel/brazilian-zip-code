from interface import *
from consulta import *

tela_cep()

while True: 
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break 

    elif event == 'Consultar':

        try:
            logradouro = consulta_cep(values['cep'])['logradouro']
            bairro = consulta_cep(values['cep'])['bairro']
            localidade = consulta_cep(values['cep'])['localidade']
            uf = consulta_cep(values['cep'])['uf']
            ddd = consulta_cep(values['cep'])['ddd']

            window['logradouro'].update(logradouro)
            window['bairro'].update(bairro)
            window['localidade'].update(localidade)
            window['uf'].update(uf)
            window['ddd'].update(ddd)

        except:
            sg.Popup ("CEP incorreto") 