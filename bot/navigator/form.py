import os
from selenium import webdriver

class Driver(webdriver.Chrome):
    BASE_URL = "https://weworkremotely.com/"
    # URL  do site que esta sendo navegado
    # Mata ou nao o bot

    def __init__(self, switch=False):
        self.driver_path = os.path.abspath('././chromedriver.exe')
        # Path do driver
        self.switch = switch
        os.environ['PATH'] += self.driver_path
        # Garantindo que a variavel PATH, esteja cadastrado no ambiente
        # A pedido do selenium
        super(Driver,self).__init__()
        # Vai inicializar o constructor do chrome
    
    def landing_page(self):
        self.get(self.BASE_URL)
        #Pegando o site

    def job_seeker_part(self):
        pass

    def __exit__(self,*args):
        def __init__():
            super().__init__()
        if self.switch:
            # Interrupto se e argumento passado no construtor igual a verdadeiro
            # Mata  o bot
            self.quit()
            print('Seus formulariaos foram preenchidos')
