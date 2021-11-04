import random, pygame, sys, spritesheet
from pygame.locals import *

# Declaración de constantes y variables
WHITE = (255, 255, 255)

# Función principal del juego

sonicx=[]
sonicy=[]
possonic=[]
destsonicx=[]
destsonicy=[]

def borrasonic(pos):
   sonicx.pop(pos)
   sonicy.pop(pos)
   possonic.pop(pos)
   destsonicx.pop(pos)
   destsonicy.pop(pos)


def creasonic(personaje_x, personaje_y):
   sonicx.append(370)
   sonicy.append(random.randrange(1,224))
   possonic.append(0)
   destsonicx.append(personaje_x)
   destsonicy.append(personaje_y)
   possonic.append(0)
def main():
   # Se inicializa el juego
   pygame.init()

   pygame.display.set_caption("Título del juego")
   screen = pygame.display.set_mode((320,224))

   fondo = pygame.image.load('fondo.jpeg')
   personaje = pygame.image.load('nave.png')

   contsonics=0

   sonics = pygame.image.load('sonic.gif')



   personaje_x = 10
   personaje_y = 10




   clock = pygame.time.Clock()

   izquierdapulsado=0
   derechapulsado=0
   arribapulsado=0
   abajopulsado=0
   posnave=44


   # Bucle principal
   cont=0
   contasonic=0
   contcreasonic=0
   pressed_up = False
   pressed_down = False
   pressed_left = False
   pressed_right = False
   while True:
      clock.tick(60)
      # 1.- Se dibuja la pantalla
      #screen.fill(WHITE)
      screen.blit(fondo, (cont, 0))
      screen.blit(personaje, (personaje_x, personaje_y),(0,posnave,35,22))

      contsonics=0
      while contsonics<len(sonicx):
         screen.blit(sonics, (sonicx[contsonics], sonicy[contsonics]), (possonic[contsonics], 145, 50, 50))
         contsonics +=1

      if cont<-2800:
         cont=0
      else:
         cont -=1

      # 2.- Se comprueban los eventos
      for event in pygame.event.get():

         if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

         if event.type == pygame.KEYDOWN:  # check for key presses
            if event.key == pygame.K_LEFT:  # left arrow turns left
               pressed_left = True
            elif event.key == pygame.K_RIGHT:  # right arrow turns right
               pressed_right = True
            elif event.key == pygame.K_UP:  # up arrow goes up
               pressed_up = True
            elif event.key == pygame.K_DOWN:  # down arrow goes down
               pressed_down = True
         elif event.type == pygame.KEYUP:  # check for key releases
            if event.key == pygame.K_LEFT:  # left arrow turns left
               pressed_left = False
            elif event.key == pygame.K_RIGHT:  # right arrow turns right
               pressed_right = False
            elif event.key == pygame.K_UP:  # up arrow goes up
               pressed_up = False
            elif event.key == pygame.K_DOWN:  # down arrow goes down
               pressed_down = False


      if pressed_up == True:
         personaje_y -=1
         posnave = 22
      if pressed_down == True:
         personaje_y +=1
         posnave = 0
      if pressed_left == True:
         personaje_x -=1
      if pressed_right == True:
         personaje_x +=1
      if pressed_up == False and pressed_down == False:
         posnave = 44

      if contcreasonic == 20:
         creasonic(personaje_x, personaje_y)
         contcreasonic =0
      else:
         contcreasonic +=1


      contsonics=0
      while contsonics < len(sonicx):
         if sonicx[contsonics] < -50:
            borrasonic(contsonics)
         else:
            sonicx[contsonics] -=2
         if contasonic == 2:
            if sonicy[contsonics] > personaje_y:
               sonicy[contsonics] -=1
            elif sonicy[contsonics] < personaje_y:
               sonicy[contsonics] +=1


         contsonics +=1

      if contasonic == 2:

         contsonics=0
         while contsonics<len(sonicx):
            posactual = possonic[contsonics]
            if posactual < int(150):
               possonic[contsonics] = possonic[contsonics] + 50
            else:
               possonic[contsonics] = 0
            contsonics += 1
         contasonic =0
      else:
         contasonic +=1

      # 3.- Se actualiza la pantalla
      pygame.display.update()

# Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':
   main()



