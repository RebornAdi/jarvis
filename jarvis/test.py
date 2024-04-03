import pyautogui
    import time
    text=text.split(" ")
    app_name=""
    i=2
    while(i<len(text)):
        app_name+=text[i]
        app_name+=" "
        i+=1
    say(f"Opening app {app_name} sir.")
    # Press the Windows key to open the Start menu
    pyautogui.press('win')
    time.sleep(1)  # Wait for the Start menu to open

    pyautogui.write(f'{app_name}')
    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(1)