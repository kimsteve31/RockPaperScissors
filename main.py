import pygame
import random

# Screen Size variables
screen_width = 500
screen_height = 500

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Static Variables
choice = ('rock', 'paper', 'scissor')

# Button Class for the user input options
class Button(object):
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        """
        Draw the button onto the window
        :param win: The pygame display window
        :param outline: Draw additional rectagle border if True
        :return: None
        """
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, black)
            win.blit(text, (self.x + (self.width // 2 - text.get_width() // 2), self.y + (self.height // 2 - text.get_height() // 2)))

    def isOver(self, pos):
        """
        Control the button click functionality
        :param pos: the (x, y) tuple location for the mouse
        :return: True if mouse cursor is within the button's location
        """
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False

# Application for the pygame rock paper scissor
class Application(object):
    def __init__(self):
        pygame.init()
        win = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Rock Paper Scissors")
        self.main(win)

    def main(self, win):
        """
        Runs the main application
        :param win: The pygame  window is created at the initialization of Application Object
        :return: None
        """

        # The rock, paper, scissor buttons
        rockButton = Button(white, 50, 400, 100, 50, 'ROCK')
        paperButton = Button(white, 200, 400, 100, 50, 'PAPER')
        scissorButton = Button(white, 350, 400, 100, 50, 'SCISSOR')

        # Player and computer scores
        player = 0
        computer = 0

        run = True
        while run:
            userChoice = 'none'
            compChoice = 'none'
            beginGame = False
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    run = False

                # Control mouse button events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rockButton.isOver(pos):
                        userChoice = 'rock'
                        compChoice = self.computer_generate()
                        beginGame = True
                    elif paperButton.isOver(pos):
                        userChoice = 'paper'
                        compChoice = self.computer_generate()
                        beginGame = True
                    elif scissorButton.isOver(pos):
                        compChoice = self.computer_generate()
                        userChoice = 'scissor'
                        beginGame = True

            self.display_score(win, player, computer)
            self.display_playground(win, rockButton, paperButton, scissorButton)

            if beginGame:
                self.game_initiate(win)

            self.display_player(userChoice, win)
            self.display_computer(compChoice, win)

            if beginGame:
                scores = self.decide_winner(userChoice, compChoice)
                pygame.display.update()
                pygame.time.delay(1000)
                player += scores[0]
                computer += scores[1]

            pygame.display.update()
            pygame.time.delay(40)

    def decide_winner(self, user, computer):
        """
        This method outputs the user and computer scores given the user and computer choice
        :param user: User's choice
        :param computer: Computer Choice
        :return: Return list with format [user_score, computer_score]
        """
        user_index = choice.index(user)
        computer_index = choice.index(computer)
        diff = user_index - computer_index
        if diff == -2 or diff == 1:
            return [1, 0]
        elif diff == 0:
            return [0, 0]
        else:
            return [0, 1]

    def computer_generate(self):
        """
        Generate the computer choice
        :return: computer choice
        """
        return choice[random.randrange(3)]

    def game_initiate(self, win):
        """
        When an event has been triggered, this method runs the game sequence.
        :param win: The pygame display
        :return: None
        """
        font = pygame.font.SysFont('comicsans', 70)

        pygame.draw.rect(win, white, (0, screen_height // 4, screen_width, screen_height // 2))
        text = font.render('ROCK!', 1, black)
        win.blit(text, (180, 300))
        self.display_player('rock', win)
        self.display_computer('rock', win)
        pygame.display.update()
        pygame.time.delay(500)

        pygame.draw.rect(win, white, (0, screen_height // 4, screen_width, screen_height // 2))
        text = font.render('PAPER!', 1, black)
        win.blit(text, (170, 300))
        self.display_player('paper', win)
        self.display_computer('paper', win)
        pygame.display.update()
        pygame.time.delay(500)

        pygame.draw.rect(win, white, (0, screen_height // 4, screen_width, screen_height // 2))
        text = font.render('SCISSOR!', 1, black)
        win.blit(text, (140, 300))
        self.display_player('scissor', win)
        self.display_computer('scissor', win)
        pygame.display.update()
        pygame.time.delay(500)

        pygame.draw.rect(win, white, (0, screen_height // 4, screen_width, screen_height // 2))
        text = font.render('SHOOT!', 1, black)
        win.blit(text, (165, 300))

    def display_score(self, win, player, computer):
        """
        Display the score as long as winner hasn't reached max score
        :param win: Pygame display
        :param player: THe player score
        :param computer: The computer score
        :return: None
        """
        font = pygame.font.SysFont('comicsans', 70)
        if player < 10 and computer < 10:
            pygame.draw.rect(win, black, (150, 30, 75, 50))
            pygame.draw.rect(win, black, (295, 30, 75, 50))
            text1 = font.render(str(player), 1, white)
            text2 = font.render(str(computer), 1, white)
            win.blit(text1, (185, 35))
            win.blit(text2, (297, 35))

    def display_playground(self, win, rock, paper, scissor):
        """
        Draw the buttons and the background white game rectangle
        :param win: Pygame display
        :param rock: Rock Button
        :param paper: Paper Button
        :param scissor: Scissor Button
        :return: None
        """
        pygame.draw.rect(win, white, (0, screen_height // 4, screen_width, screen_height // 2))
        pygame.draw.rect(win, white, (230, 50, 50, 10))
        rock.draw(win, black)
        paper.draw(win, black)
        scissor.draw(win, black)

    def display_player(self, pick, win):
        """
        Display the player icons
        :param pick: The icon to display
        :param win: The pygame window
        :return: None
        """
        if pick == 'none':
            return False
        if pick == 'paper':
            player = pygame.image.load('paper.png')
        elif pick == 'scissor':
            player = pygame.image.load('scissor.png')
        else:
            player = pygame.image.load('rock.png')
        player = pygame.transform.scale(player, (100, 100))

        win.blit(player, (screen_width // 6, screen_height // 3))

    def display_computer(self, pick, win):
        """
        Display the computer icons
        :param pick: The icon to display
        :param win: Pygame window
        :return: None
        """
        if pick == 'none':
            return False
        if pick == 'paper':
            computer = pygame.image.load('paper.png')
        elif pick == 'scissor':
            computer = pygame.image.load('scissor.png')
        else:
            computer = pygame.image.load('rock.png')
        computer = pygame.transform.scale(computer, (100, 100))

        win.blit(computer, (4 * (screen_width // 6), screen_height // 3))

# Begin Program
if __name__ == '__main__':
    app = Application()
    pygame.quit()