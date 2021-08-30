import sys
import pygame
tamano=width,height=650,700
tamano2=width,height=720,450
velocidad=[1.2,2]
velocidad2=[2.0,2]
blok=0,0,0,1
que=0,1,2,2
variable1=pygame.display.set_mode(tamano)
variable2=pygame.display.set_mode(tamano2)
imagen=pygame.image.load('rick.png')
imagen_rect=imagen.get_rect()
imagen2=pygame.image.load('stone.png')
imagen2_rect=imagen2.get_rect()
#bucle para el recorrido de la imagen
while 1:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT: sys.exit()
	imagen_rect=imagen_rect.move(velocidad)
	imagen2_rect=imagen2_rect.move(velocidad2)
	if imagen_rect.left < 0 or imagen_rect.right > width:
		velocidad[0] = -velocidad[0]
	if imagen_rect.top < 0 or imagen_rect.bottom > height:
		velocidad[1]= -velocidad[1]
	if imagen2_rect.right < 0 or imagen2_rect.left > width:
                velocidad2[0] = -velocidad2[0]
	if imagen2_rect.bottom < 0 or imagen2_rect.centery > height:
                velocidad2[1]= -velocidad2[1]

	variable1.fill(blok)
	variable1.blit(imagen,imagen_rect)
	variable2.fill(que)
	variable2.blit(imagen2,imagen2_rect)
	pygame.display.flip()
