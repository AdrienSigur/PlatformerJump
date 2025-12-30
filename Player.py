import pygame

class Player:
    def __init__(self, screen_w, screen_h):

        self.pos = pygame.Vector2(screen_w / 2, screen_h / 2)
        self.speed = 150
        self.radius = 40 
        self.hitbox = pygame.Rect(0, 0, 80, 80)

    def move(self, dt , Environnement):
       

        keys = pygame.key.get_pressed()

        # --- AXE X ---
        move_x = 0
        if keys[pygame.K_q]:
            move_x = -self.speed * dt
        if keys[pygame.K_d]:
            move_x = self.speed * dt
            
        self.pos.x += move_x
        self.hitbox.center = self.pos 
        
        for Colision in Environnement :
            if self.hitbox.colliderect(Colision):
          
                self.pos.x -= move_x 
                self.hitbox.center = self.pos
                break


        move_y = 0
        if keys[pygame.K_z]:
            move_y = -self.speed * dt
        if keys[pygame.K_s]:
            move_y = self.speed * dt
    
        self.pos.y += move_y
        self.hitbox.center = self.pos

        for Colision in Environnement :
            if self.hitbox.colliderect(Colision):
                self.pos.y -= move_y 
                self.hitbox.center = self.pos
                break

    def draw(self, surface):
        # Une MÉTHODE pour se dessiner sur l'écran
        pygame.draw.circle(surface, "red", self.pos, self.radius)

