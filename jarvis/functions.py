def hello(text):   
    print("Hello , welcome to this program.")
def create_files(text):
    import os
    path="C:\\Users\\Aditya Atul Deshmukh\\Desktop\\test"
    for i in range(1,100):
        os.mkdir(f"{path}/{i}")
def del_files(text):
    import os
    for i in range(1,100):
        os.rmdir(f"C:\\Users\\Aditya Atul Deshmukh\\Desktop\\test\\{i}")
def open_vtop(username_text,password_text):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    import pyperclip
    import time
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://vtop.vit.ac.in/vtop/login')
    xpath = '//*[@id="stdForm"]/a/div/div[2]/button'
    student = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, xpath)))
    student.click()
    user_xpath='//*[@id="username"]'
    username=WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH,user_xpath)))
    username.click()
    pyperclip.copy(username_text)
    username.send_keys(Keys.CONTROL,'v')
    pass_xpath='//*[@id="password"]'
    password=WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH,pass_xpath)))
    password.click()
    pyperclip.copy(password_text)
    password.send_keys(Keys.CONTROL,'v')
    vtop_xpath='//*[@id="b5-pagewrapper"]/div[1]/div/div/div/div[1]'
    WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH,vtop_xpath)))
    time.sleep(5)
    browser.quit()
def whatsapp(text):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    import pyperclip
    import time
    message=""
    admi=""
    text=text.split(" ")
    length=len(text)
    i=4
    temp=""
    while(text[i]!="that"):
        temp+=f"{text[i]} "
        i+=1
    admi+=(temp[:-1])
    j=i+1
    temp2=""
    while(j!=length):
        temp2+=f"{text[j]} "
        j+=1
    message+=temp2[:-1]
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://web.whatsapp.com')
    time.sleep(10)
    xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    search_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, xpath)))
    search_box.click()
    pyperclip.copy(admi)
    search_box.send_keys(Keys.SHIFT, Keys.INSERT)
    search_box.click()
    search_box.send_keys(Keys.ENTER)
    top_click = WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
    top_click.click()
    pyperclip.copy(message)
    top_click.send_keys(Keys.SHIFT, Keys.INSERT)
    top_click.click()
    top_click.send_keys(Keys.ENTER)
    time.sleep(10)
    browser.quit()
def search(text):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    import pyperclip
    import time
    search_engine=""
    search_text=""
    text=text.split(" ")
    length=len(text)
    search_engine+=text[2]
    i=3
    while(i<=length-1):
        search_text+=f"{text[i]} "
        i+=1
    if(search_engine=="youtube"):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(f'https://www.youtube.com/{search_text}')
        close=input("Do you want to quit? : ")
        if(close=="yes"):
            browser.quit()
    elif(search_engine=="google"):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(f'https://www.google.com')
        xpath = '//*[@id="APjFqb"]'
        search_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, xpath)))
        search_box.click()
        pyperclip.copy(search_text)
        search_box.send_keys(Keys.CONTROL, 'v')
        search_box.click()
        search_box.send_keys(Keys.ENTER)
        close=input("Do you want to quit? : ")
        if(close=="yes"):
            browser.quit()



