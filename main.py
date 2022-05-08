import os
from selenium import webdriver

os.environ['PATH'] += os.path.abspath("./chromedriver.exe")
driver = webdriver.Chrome()
#Formulacao do driver
driver.get("https://weworkremotely.com/")
#Site avaliados
driver.implicitly_wait(5)


links_brutos = driver.find_elements_by_tag_name("a")
#Todos os link do site
#Limpando os links
links_limpos = []

for link in links_brutos:
    a = link.get_attribute("href")
    #Pegando o attributo de interesse
    try:
        if a.startswith("https://weworkremotely.com/remote-jobs/"):
            #Pegando somente os interessantes, basicamente remote job
            links_limpos.append(a)

    except AttributeError:
        pass



print(links_limpos)
driver.quit()