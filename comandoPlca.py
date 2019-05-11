# Importando sense hat
from sense_emu import SenseHat
import time
#instancia em python
sense = SenseHat()
#criando variaveis com cores
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
#controla a velodidade a padrão é 0.1
scroll_speed = 0.005

sense.show_message("Olá Mundo!",scroll_speed,green)
nome = input("Digite seu nome: ")
sense.show_message(nome,scroll_speed,green)
#limpando matriz de led
sense.clear()

int_red = 0
int_green = 0
int_azul = 0
cor = (int_red, int_green, int_azul)

while True:
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
    
    #Como iremos controlar a matriz de leds
    #feedback de temperatura
    #Se a temperatura for de 0 a 30 gradus, gradativamenteaumenta o tom de azul
    int_red = 0
    int_green = 0
    int_azul = 0
    if (temperature > 0 and temperature <= 30):
          int_azul = (temperature * 8.6) #numa escla de zero a 255
          int_green = 0
          int_red = 0;
    elif (temperature > 30 and temperature < 101):
          int_azul = 0
          int_green = 0
          int_red = (temperature*3.64)
   
    
    sense.clear(cor)
        