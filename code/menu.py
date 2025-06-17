#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter.font import Font

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.blackgroundMenu = pygame.image.load('./asset/Summer5.png')
        self.rect = self.blackgroundMenu.get_rect(left=0,
                                                  top=0)  # dizendo aqui que o RECT (retangulo ivizivel ) ressebe blackgroundmenu (imagem do menu )

    def run(self, ):
        pygame.mixer_music.load('./asset/MENU.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.blackgroundMenu,
                             dest=self.rect)  # dizemos que a imagem tem que aparecer no rect
            self.menu_text(text_size=50, text="ADVENTURE", text_color=COLOR_ORANGE,
                           text_center_pos=((WIN_WIDTH / 2), 50))
            self.menu_text(text_size=50, text="SPACE", text_color=COLOR_ORANGE,
                           text_center_pos=((WIN_WIDTH / 2), 100))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=C_WHITE,
                               text_center_pos=((WIN_WIDTH / 2), 170 + i * 25)
                               )

            pygame.display.flip()
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
