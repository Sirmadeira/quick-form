from navigator.form import Driver

#Aviso: O exite method e executado
#Ao sair do with statement
with Driver(switch = True) as bot:
    bot.landing_page()