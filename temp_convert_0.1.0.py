'''
temp_convert.py
@author: Noah Totzke

Description: 
Takes in a tempature from user and convert ferrinheight to celsius and kelvin and vice versa.

08-10-2022: v0.0.1 - Initial Pre-release Version

08-11-2022: v0.0.2 - Layout elements now working

08-11-2022: v0.1.0 - Program now completely functional

'''

import PySimpleGUI as sg
from termcolor import colored

fconvert = 0
cconvert = 0
kconvert = 0
layout = [[sg.Text("Please input the tempature in Fahrenheit, Celsius or Kelvin")], [sg.Input(key='-INPUT-')], #Sets up window layout
          [sg.Text('Unit:'), sg.OptionMenu(values=['F°', 'C°', 'K°'], default_value='F°', key='-DATA_TYPE-')],
          [sg.Text(size=(40,1), key='-FerOUTPUT-')], 
          [sg.Text(size=(40,1), key='-CelOUTPUT-')], 
          [sg.Text(size=(40,1), key='-KelOUTPUT-')],
          [sg.Button("Convert"), sg.Button("Quit")]]

window = sg.Window("Temp Conversion", layout) #Create the window

def convertFer(temp_dat): #Will convert Celsuis and Kelvin into Fahrenheit
    global fconvert
    if values['-DATA_TYPE-'] == 'C°':
        try:
            fconvert = (temp_dat * (9/5)) + 32
        except:
            print("Unable to convert to F°")
    elif values['-DATA_TYPE-'] == 'K°':
        try:
            fconvert = (temp_dat - 273.15) * (9/5) + 32
        except:
            print("Unable to convert to F°")
    return fconvert
    
def convertCel(temp_dat): #Will convert Fahrenheit and Kelvin into Celsius
    global cconvert
    if values['-DATA_TYPE-'] == 'F°':
        try:
            cconvert = (temp_dat - 32) * (5/9)
        except:
            print("Unable to convert to C°")
    elif values['-DATA_TYPE-'] == 'K°':
        try:
            cconvert = temp_dat - 273.15
        except:
            print("Unable to convert to C°")
    return cconvert

def convertKel(temp_dat): #Will convert Celsuis and Fahrenheit into Kelvin
    global kconvert
    if values['-DATA_TYPE-'] == 'C°':
        try:
            kconvert = temp_dat + 273.15
        except:
            print("Unable to convert to K°")
    elif values['-DATA_TYPE-'] == 'F°':
        try:
            kconvert = (temp_dat - 32) * (5/9) + 273.15
        except:
            print("Unable to convert to K°")
    return kconvert

def clearWindow():
    window['-FerOUTPUT-'].update(" ")
    window['-CelOUTPUT-'].update(" ")
    window['-KelOUTPUT-'].update(" ")

while True:
    event, values = window.read()
   
    temp_dat = float(values['-INPUT-'])
    
    if event == sg.WIN_CLOSED or event == "Quit": # End program if user closes window or presses the Quit button
        break
    elif event == "Convert":
        if values['-DATA_TYPE-'] == 'F°':
            clearWindow()
            convertCel(temp_dat)
            convertKel(temp_dat)
            window['-CelOUTPUT-'].update("Celsius = " + str(cconvert) + 'C°')
            window['-KelOUTPUT-'].update("Kelvin = " + str(kconvert) + 'K°')
        elif values['-DATA_TYPE-'] == 'C°':
            clearWindow()
            convertFer(temp_dat)
            convertKel(temp_dat)
            window['-FerOUTPUT-'].update("Fahrenheit = " + str(fconvert) + 'F°')
            window['-KelOUTPUT-'].update("Kelvin = " + str(kconvert) + 'K°')
        elif values['-DATA_TYPE-'] == 'K°':
            clearWindow()
            convertFer(temp_dat)
            convertCel(temp_dat)
            window['-FerOUTPUT-'].update("Fahrenheit = " + str(fconvert) + 'F°')
            window['-CelOUTPUT-'].update("Celsius = " + str(cconvert) + 'C°')

window.close()