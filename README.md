# Esteban's Game

### This game is created to demonstrate everything learned in the course of GAME DESIGN AND DEVELOPMENT.

## Class Diagram
![image](https://github.com/Esteban-devr/juego_esteban/assets/133018246/72e93995-aaef-41db-b5ef-9d8a94dedf08)

### This is a very basic diagram showing the classes Vehicle and PlayerVehicle, along with their attributes. The relationship between them is that PlayerVehicle inherits from Vehicle. Additionally, both classes utilize functionalities provided by the pygame module, such as handling sprites and images.

## Entity Relationship Diagram
 ![image](https://github.com/Esteban-devr/juego_esteban/assets/133018246/2b658100-ca1b-4ec1-8ca2-a17b4a433942)

### The player controls a vehicle.
The vehicles move along the lanes of the road.
Lane markers are displayed on the screen to guide the player.
Collisions occur when vehicles crash into each other.
The player's score and level increase based on their performance in the game.
The game settings affect game features such as speed and screen size.

### Diccionario de datos
![image](https://github.com/Esteban-devr/juego_esteban/assets/133018246/5307fe0e-2c44-47c1-8051-d73cb976e046)

## Diagrama de secuencia
![image](https://github.com/Esteban-devr/juego_esteban/assets/133018246/2fcb414d-ff0b-42ed-a88f-5bb86df914c9)

### This diagram shows a simple interaction between the player, the vehicles, and the main game loop. Here are the main actions represented in the diagram:

1. The player calls the Move() method, which moves their vehicle left or right.
2. If there's a collision between the player and another vehicle, the player is notified.
3. The main game loop continues to run, involving moving the vehicles and checking for collisions.

##**User Manual: Vehicle Dodging Game**

Welcome to the Vehicle Dodging Game! This manual will guide you through the basics and instructions to play.

**1. Game Description:**
   - In this game, you will control a vehicle on a busy road.
   - Your objective is to dodge the oncoming vehicles and avoid crashing into them.
   - As you progress, the speed will increase, and the difficulty will rise.

**2. Controls:**
   - Use the left and right arrow keys to move to the corresponding lanes.
   - Left Arrow: Move left.
   - Right Arrow: Move right.

**3. Scoring and Levels:**
   - You will earn points for every successfully dodged vehicle.
   - The speed and difficulty will increase as you advance in the game.
   - Every 10 points reached, the speed will increase, and the level will advance.

**4. Collisions:**
   - If your vehicle collides with another vehicle or goes off the road, the game will end.
   - You can retry if you wish.

**5. Objective:**
   - The objective of the game is to achieve the highest score possible by dodging vehicles and advancing levels.

**6. Tips:**
   - Maintain focus and quick reaction to avoid collisions.
   - Don't forget to control the speed, especially as the game gets faster.

**7. Have Fun!**
   - Enjoy the game and compete with yourself or friends to see who can achieve the highest score.

Now that you know the basic rules, you're ready to start playing! Good luck and have fun dodging vehicles on the road!


