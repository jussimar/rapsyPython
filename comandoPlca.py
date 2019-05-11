# Importando sense hat
from sense_emu import SenseHat
import time
#instancia em python
sense = SenseHat()
#criando variaveis com cores
red = (255,0,0)
green = (0,255,0)
#controla a velodidade a padrão é 0.1
scroll_speed = 0.005

while True:
    sense.show_message("Olá Mundo!",scroll_speed,green)
    time.sleep(1)
    sense.clear(red)
    time.sleep(5)
    
    #pega a humidade do sensor
    humidity = sense.get_humidity()
    print("Umidade: " + str(humidity))
    sense.show_message("Umidade: " + str(humidity),scroll_speed,green)
    
    #pega a temperatura
    temperature = sense.get_temperature()
    print("Temperatura: " + str(temperature))
    sense.show_message("Temperatura: " + str(temperature),scroll_speed,green)