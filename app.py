import pyautogui
import webbrowser
from time import sleep


lista_nomes = ['nike', 'adidas']

for nome in lista_nomes:
    webbrowser.open_new('https://www.instagram.com')
    
    sleep(2)
    procurar = pyautogui.locateCenterOnScreen('icone_procurar.png')
    pyautogui.click(procurar[0],procurar[1],duration=1)
    sleep(2)

    pyautogui.typewrite(nome)
    sleep(2)

    pyautogui.move(200,0)
    sleep(1)

    pyautogui.click()
    sleep(3)

    publicacao = pyautogui.locateCenterOnScreen('publicacao.png')
    pyautogui.moveTo(publicacao[0],publicacao[1],duration=1)
    pyautogui.move(-10,50)
    pyautogui.click()
    sleep(1)

    curtida = pyautogui.locateCenterOnScreen('curtida.png')

    #comentario = pyautogui.locateCenterOnScreen('comentario.png')
    emoji = pyautogui.locateCenterOnScreen('emoji.png')

    if curtida is None:
        sleep(2)
        curtida_vazia = pyautogui.locateCenterOnScreen('curtida_vazia.png')
        pyautogui.moveTo(curtida_vazia[0],curtida_vazia[1],duration=1)
        pyautogui.click()
        
        sleep(1)
        pyautogui.moveTo(emoji[0],emoji[1],duration=1)
        pyautogui.move(150,0)
        pyautogui.click()
        pyautogui.typewrite('Folow me')
        
        sleep(1)
        publicar = pyautogui.locateCenterOnScreen('publicar.png')
        pyautogui.moveTo(publicar[0],publicar[1],duration=1)
        pyautogui.click()
        

    



