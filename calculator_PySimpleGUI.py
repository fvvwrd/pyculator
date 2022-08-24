from math import *
import PySimpleGUI as sg

layout = [
         [sg.Input(default_text='0',size=(26,1), justification='right',key='indi')],
         [sg.Button('C',button_color=('white','maroon')),sg.Button('±'),
          sg.Button('%'),sg.Button('√'),sg.Button('sin',button_color=('white','navy'))],
         [sg.Button('7'),sg.Button('8'),sg.Button('9'),sg.Button('+'),
          sg.Button('cos',button_color=('white','navy'))],
         [sg.Button('4'),sg.Button('5'),sg.Button('6'),sg.Button('-'),
          sg.Button('tg',button_color=('white','navy'))],
         [sg.Button('1'),sg.Button('2'),sg.Button('3'),sg.Button('×'),
          sg.Button('π',button_color=('white','navy'))],
         [sg.Button('0'),sg.Button(','),
          sg.Button('=',button_color=('white','maroon')),
          sg.Button('÷'),sg.Button('|x|',button_color=('white','navy'))]]

window = sg.Window('Calculator',layout,
                   #icon
                   margins=(10,10),element_padding=(10,10),element_justification='center',
                   auto_size_buttons=False,default_button_element_size=(3,1))

#Start
first_click = True
oper        = ''
x           = 0

#Function
def numkey(e):
    global first_click
    if first_click:
        window['indi'].update(e)
        print('first_click')
        if e !='0':
            print(e)
            print('e is not 0, not first click')
            first_click = False
    else:
        window['indi'].update(values['indi'] + e)

def plusminus():
    if values['indi'].find('.') == -1 and values['indi'].find('e') == -1:
        indi = -int(values['indi'])
    else:
        indi = -float(values['indi'])
    window['indi'].update(indi)

def sqroot():
    if values['indi'].find('.') == -1 and values['indi'].find('e') == -1:
        indi = sqrt(int(values['indi']))
    else:
        indi = sqrt(float(values['indi']))
    window['indi'].update(indi)

def arifm(e):
    global first_click, oper, x
    oper = e
    if values['indi'].find('.') == -1 and values['indi'].find('e') == -1:
        x = int(values['indi'])
    else:
        x = float(values['indi'])
    first_click = True

def equation():
    if values['indi'].find('.') == -1 and values['indi'].find('e') == -1:
        y = int(values['indi'])
    else:
        y = float(values['indi'])
    if oper == '+':
        window['indi'].update(x+y)
    if oper == '-':
        window['indi'].update(x-y)
    if oper == '×':
        window['indi'].update(x*y)
    if oper == '÷' and abs(y)>0.0000000001:
        window['indi'].update(x/y)
    first_click = True
    
while True:      
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'C':
        first_click = True
        oper        = ''
        x           = 0
        window['indi'].update(0)

    if event in ('0','1','2','3','4','5','6','7','8','9'):
        numkey(event)

    if event == '±':
        plusminus()

    if event == '√':
        sqroot()

    if event == 'π':
        indi = 3.1415
        window['indi'].update(indi)

    if event == '|x|':
        window['indi'].update(abs(float(values['indi'])))
        
    if event in ('+','-','×','÷'):
        arifm(event)

    if event == 'sin':
        indi=sin(float(values['indi']))
        window['indi'].update(indi)
    if event == 'cos':
        indi=cos(float(values['indi']))
        window['indi'].update(indi)
    if event == 'tg':
        indi=tan(float(values['indi']))
        window['indi'].update(indi)




    if event == '=':
        equation()

window.close()
