from create import create
import PySimpleGUI as sg

def set_ui() :
    sg.theme('BluePurple')
    layout = [[sg.Text('Data:')],
            [sg.Input(key='DATA')],
            [sg.Text('File name:')],
            [sg.Input(key='NAME')],
            [sg.Button('Create'), sg.Button('Exit')]]

    window = sg.Window('QR-code maker', layout)
    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Create':
            create(values['DATA'], values['NAME'])
    window.close()

if __name__ == '__main__' :
    set_ui()