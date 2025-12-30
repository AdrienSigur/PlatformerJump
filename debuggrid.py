import pygame

def debug_grid(surface):
    # 1. On récupère la position de la souris
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # 2. On prépare la police d'écriture
    font = pygame.font.SysFont("Arial", 18)
    
    # 3. On dessine une grille (Lignes verticales et horizontales)
    # On fait des lignes gris clair tous les 100 pixels
    col = (200, 200, 200) # Gris clair
    
    # Lignes Verticales (X)
    for x in range(0, 1280, 100):
        pygame.draw.line(surface, col, (x, 0), (x, 720))
        # Petit chiffre pour se repérer
        text = font.render(str(x), True, "black")
        surface.blit(text, (x + 5, 5))

    # Lignes Horizontales (Y)
    for y in range(0, 720, 100):
        pygame.draw.line(surface, col, (0, y), (1280, y))
        text = font.render(str(y), True, "black")
        surface.blit(text, (5, y + 5))

    # 4. On affiche les coordonnées à côté de la souris
    coord_text = f"X: {mouse_x} | Y: {mouse_y}"
    # On crée une étiquette noire
    label = font.render(coord_text, True, "white", "black") 
    # On la colle à côté de la souris (+15 pour décaler un peu)
    surface.blit(label, (mouse_x + 15, mouse_y + 15))