import pygame
from text import Text
from inputBox import InputBox

pygame.init()
pygame.font.init()

def print_chat_text(chat_win, chat_text):
    if len(chat_text) > 9:
        chat_text = chat_text[len(chat_text)-9:]
    line = 0
    chatx = 0
    chaty = 0
    for chat_line in chat_text:
        font = pygame.font.SysFont('Comic Sans MS', 50, True)
        if chat_line.split(":")[0] == 'Dan':
            chat_line = chat_line.split(":")[1]
            chat_surface = font.render(chat_line, True, ((85, 236, 13)))
            chat_win.blit(chat_surface, (chatx + 5, chaty + 5 + line))           
        else:
            chat_surface = font.render(chat_line, True, ((0,0,0)))
            text_width, _ = font.size(chat_line)
            chat_win.blit(chat_surface, (chatx + (500-text_width), chaty + 5 + line))            
        line += 40

def main():

    chat_win = pygame.display.set_mode((500, 600))
    pygame.display.set_caption('Socket Chat')
    inputBox = InputBox(100, 400, 300, 80)
    msg1 = Text("Dan: first msg", isBold=True, background=(0,200,0))
    msg2 = Text("Yarin: second msg", isBold=True, background=(255,255,200))
    texts = []

    running = True;
    chat_win.fill((255,255,255))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            submittedText = inputBox.handle_event(event)
            if submittedText != None:
                chat_win.fill((255,255,255)) 
                texts.append(submittedText)
                print_chat_text(chat_win, texts)
                 




        
        inputBox.draw(chat_win)           
        pygame.display.update()




main()

