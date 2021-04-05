import pyautogui
import webbrowser as web
from time import sleep

web.open('https://web.whatsapp.com/send?phone=')#Introducir numero de telefono despues de = 
sleep(10)

for i in range(100)#Numero de veces que se va a enviar el mensaje:
    pyautogui.typewrite('Hola buenas, este mensaje ha sido enviado con un bot')
    pyautogui.press('enter')