import pygame

class Player:
    def __init__(self, screen_w, screen_h):

        original_image = pygame.image.load("Models\\Mario.png").convert_alpha()

        self.image = pygame.transform.scale(original_image, (70, 70))

        self.pos = pygame.Vector2(screen_w - 1180 , screen_h - 100)
        self.speed = 200
        self.radius = 40 
        self.hitbox = self.image.get_rect()
        self.hitbox.center = self.pos

        self.gravity = 980
        self.velocity_y = 0
        self.jump_force = -600
        self.on_ground = False


    def move(self, dt , Environnement):
       
        keys = pygame.key.get_pressed()

        # --- AXE X ---
        move_x = 0
        if keys[pygame.K_LEFT]:
            move_x = -self.speed * dt
        if keys[pygame.K_RIGHT]:
            move_x = self.speed * dt
            
        self.pos.x += move_x
        self.hitbox.center = self.pos 
        
        for Colision in Environnement :
            if self.hitbox.colliderect(Colision):
                self.pos.x -= move_x 
                self.hitbox.center = self.pos
                break
        
        self.velocity_y += self.gravity * dt


        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_force # On donne une impulsion vers le haut
            self.on_ground = False

        self.pos.y += self.velocity_y * dt
        self.hitbox.center = self.pos

        for Colision in Environnement:
            if self.hitbox.colliderect(Colision):
                
               
                if self.velocity_y > 0:
                    self.pos.y = Colision.rect.top - self.hitbox.height / 2 
                    self.velocity_y = 0   
                    self.on_ground = True 
                
                
                elif self.velocity_y < 0:
                    self.pos.y = Colision.rect.bottom + self.hitbox.height / 2 
                    self.velocity_y = 0   

                self.hitbox.center = self.pos
                break 
            if self.hitbox.colliderect(Colision):
                self.pos.y -= move_y 
                self.hitbox.center = self.pos
                break

    def draw(self , surface):
        # Une MÉTHODE pour se dessiner sur l'écran
        surface.blit(self.image, self.hitbox)

        pygame.draw.rect(surface, (255, 0, 0), self.hitbox, 2)
       

