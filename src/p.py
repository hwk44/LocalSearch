# import the pygame module, so you can use it
import pygame


# define a main function
def main():

    pygame.init()

    pygame.display.set_caption("minimal program")
    screen = pygame.display.set_mode((240, 180))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    # call the main function
    main()