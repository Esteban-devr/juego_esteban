import pygame
from pygame.locals import *
import random

pygame.init()

# Crear la ventana
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Proyecto esteban')

# Colores
black = (0, 0, 0)
gray = (100, 100, 100)
green = (0, 200, 0)
red = (200, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Tamaños de la carretera y marcadores
road_width = 300
marker_width = 10
marker_height = 50

# Cordenadas de los carriles
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# Carretera y marcadores de bordes
road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# Animacion de los marcadores de carril
lane_marker_move_y = 0

# Cordenadas iniciales del jugador
player_x = 250
player_y = 400

# Configuracion de frames
clock = pygame.time.Clock()
fps = 120

# Configuraciones del juego
gameover = False
speed = 2
score = 0
level = 1

class Vehicle(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        # Escalar la imagen para que no sea más ancha que el carril
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))
        
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
class PlayerVehicle(Vehicle):
    
    def __init__(self, x, y):
        image = pygame.image.load('images/car.png')
        super().__init__(image, x, y)
        
# Grupos de sprites
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

# Crear el auto del jugador 
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

# Cargar las imagenes de los vehiculos
image_filenames = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load('images/' + image_filename)
    vehicle_images.append(image)
    
# Cargar la imagen del choque
crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()

pygame.mixer.init()  # Inicializa el mixer de sonido
pygame.mixer.music.load('mf.mp3')  # Carga el archivo de música
pygame.mixer.music.play(-1)  # Reproduce la música en bucle (-1 indica que se repita infinitamente)

# Cargar sonido de choque
crash_sound = pygame.mixer.Sound('ca.wav')

# Ciclo principal
running = True
while running:
    
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        # Mover el vehiculo con las teclas izquierda y derecha
        if event.type == KEYDOWN:
            
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100
                
            # Verificar si hay una colisión lateral después de cambiar de carril
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):
                    
                    gameover = True
                    crash_sound.play()  # Reproducir sonido de choque
                    pygame.mixer.music.stop()  # Detener la música de fondo
                    
                    # Colocar el auto del jugador junto al otro vehículo
                    # y determinar dónde posicionar la imagen de choque
                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
            
            
    # Dibujar el pasto
    screen.fill(gray)
    
    # Dibujar el camino
    pygame.draw.rect(screen, black, road)
    
    # Dibujar los marcadores de borde
    pygame.draw.rect(screen, blue, left_edge_marker)
    pygame.draw.rect(screen, blue, right_edge_marker)
    
    # Dibujar los marcadores de carril
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        if level == 2:
            pygame.draw.rect(screen, green, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
            pygame.draw.rect(screen, green, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        elif level >= 3:
            pygame.draw.rect(screen, red, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
            pygame.draw.rect(screen, red, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        else:
            pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
            pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        
    # Dibujar el carro del jugardor
    player_group.draw(screen)
    
    # Añadir el vehiculo
    if len(vehicle_group) < 2:
        
        # Asegurar que haya suficiente espacio entre los vehículos
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
                
        if add_vehicle:
            
            # Seleccionar un carril al azar
            lane = random.choice(lanes)
            
            # Seleccionar una imagen de vehículo al azar
            image = random.choice(vehicle_images)
            vehicle = Vehicle(image, lane, height / -2)
            vehicle_group.add(vehicle)
    
    # Hacer que los vehiculos se muevan
    for vehicle in vehicle_group:
        vehicle.rect.y += speed
        
        # Remover los vehicules que esten fuera de la pantalla
        if vehicle.rect.top >= height:
            vehicle.kill()
            
            # Añadir porcentaje
            score += 1
            
            # Subir la velocidad al tener 10 puntos
            if score > 0 and score % 10 == 0:
                speed += 2
                level += 1
    
    # Dibujar los vehiculos
    vehicle_group.draw(screen)
    
    # Mostrar el Puntaje y el nivel
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text_score = font.render('Puntaje: ' + str(score), True, white)
    text_level = font.render('Nivel: ' + str(level), True, white)
    text_score_rect = text_score.get_rect()
    text_score_rect.center = (50, 30)
    text_level_rect = text_level.get_rect()
    text_level_rect.center = (450, 30)  
    screen.blit(text_score, text_score_rect)
    screen.blit(text_level, text_level_rect)
    
    # Comprobar si hay una colisión frontal
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_sound.play() 
        pygame.mixer.music.stop()  
        crash_rect.center = [player.rect.center[0], player.rect.top]
            
    # Mostrar juego terminado
    if gameover:
        screen.blit(crash, crash_rect)
        
        pygame.draw.rect(screen, red, (0, 50, width, 100))
        
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Game over. Reintentar? (S o N)', True, white)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, 100)
        screen.blit(text, text_rect)
            
    pygame.display.update()

    # Esperar la entrada del usuario para reintentar o salir
    while gameover:
        
        clock.tick(fps)
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                gameover = False
                running = False
                
            # Obtener si el usuario dice si o no 
            if event.type == KEYDOWN:
                if event.key == K_s:
                    # Reiniciar el juego
                    gameover = False
                    speed = 2
                    score = 0
                    level = 1
                    vehicle_group.empty()
                    player.rect.center = [player_x, player_y]
                    pygame.mixer.music.play(-1)  
                elif event.key == K_n:
                    # Salir de los ciclos
                    gameover = False
                    running = False

pygame.quit()
