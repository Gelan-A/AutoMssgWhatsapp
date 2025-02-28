import pywhatkit as kit
import pyautogui
import time

def send_whatsapp_message(phone_no, message, repeat=10):
    """
    Stuur een WhatsApp-bericht naar een specifiek nummer en herhaal het bericht meerdere keren.

    Args:
        phone_no (str): Het WhatsApp-nummer van de ontvanger.
        message (str): Het bericht dat verstuurd moet worden.
        repeat (int): Het aantal keren dat het bericht verstuurd moet worden.
    """
    # Open WhatsApp chat once
    kit.sendwhatmsg_instantly(phone_no=phone_no, message=message)

    # Simuleer de "Enter"-toets om het eerste bericht te versturen
    pyautogui.press('enter')

    # Wacht even om zeker te zijn dat het bericht is verstuurd
    time.sleep(5)

    # Verstuur het bericht nog (repeat-1) keer binnen dezelfde sessie
    for _ in range(repeat - 1):
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        time.sleep(1)  # Wacht even tussen de berichten

# Voorbeeld gebruik van de functie
send_whatsapp_message("+31612345678", "Hallo, dit is een automatisch bericht vanuit Python!", repeat=10)

#disclaimer : als deze code voor het eerst runt dan opent het een whatsapp web pagina en vraagt om in te loggen met je telefoon.
#het is een eenmalige actie, het bericht wordt dan naar de meest recente chat verstuurd!.
