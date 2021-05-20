import pygame as pg

import requests
import os
import math

from Button import Button
from camera import *
from functions import can_move, load_level, load_image, near_store
from player import Player
from cell import Cell
from store import store

WIDTH = 500
HEIGHT = 500
WHITE = (255, 255, 255)





lst = load_level('test_map.txt')
new_lst = []
tiles_arr = []

get_status = {'.': 'grass', '#': 'road'}
pg.init()
clock = pg.time.Clock()
running = True
screen = pg.display.set_mode((WIDTH, HEIGHT))
canvas = pygame.Surface((WIDTH,HEIGHT))
player = Player()


for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == '@':
            player.rect.x = j * 68
            player.rect.y = i * 68
            a = Cell('road', j, i)
            lst[i][j] = a
            tiles_arr.append(a)
            print(a.rect.x)
        elif lst[i][j] == 'N':
            b = store('nike', j, i)
            b.check()
            lst[i][j] = b
            tiles_arr.append(b)
        else:
            a = Cell(get_status[lst[i][j]], j, i)
            tiles_arr.append(a)
            lst[i][j] = a


title_images = {'player': load_image('player.png')}

fon = pg.image.load('data\house_full.png').convert()



camera = Camera(player)
follow = Follow(camera, player)
border = Border(camera, player)
auto = Auto(camera, player)
camera.setmethod(follow)

cr_btn = Button(WIDTH / 2 - 40, HEIGHT - 100, 100, 50)
print(lst[0][0].rect.x, lst[0][0].rect.y)
for elem in lst:
    a = []
    for e in elem:
        a.append(e.status)
    print(a)
    print()
player.rect.move(0, 0)
while running:
    clock.tick(60)
    canvas.fill((0, 0, 0))
    ################################# CHECK PLAYER INPUT #################################
    #print(player.coord_x, player.coord_y, lst[player.coord_y][player.coord_x].status)
    #can_move = can_move(player, player.coord_x, player.coord_y, lst, "up")
    store = near_store(player.coord_x, player.coord_y, lst)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN and store:
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and can_move(player, player.coord_x, player.coord_y, lst, "left"):
                player.rect.x -= 68
            elif event.key == pygame.K_RIGHT and can_move(player, player.coord_x, player.coord_y, lst, "right"):
                player.rect.x += 68
            elif event.key == pygame.K_UP and can_move(player, player.coord_x, player.coord_y, lst, "up"):
                player.rect.y -= 68
            elif event.key == pygame.K_DOWN and can_move(player, player.coord_x, player.coord_y, lst, "down"):
                player.rect.y += 68

            elif event.key == pygame.K_1:
                camera.setmethod(follow)
            elif event.key == pygame.K_2:
                camera.setmethod(border)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY, player.X = False, False
            elif event.key == pygame.K_RIGHT:
                player.RIGHT_KEY, player.X = False, False
            if event.key == pygame.K_UP:
                player.UP_KEY, player.Y = False, False
            elif event.key == pygame.K_DOWN:
                player.DOWN_KEY, player.Y = False, False

    ################################# UPDATE/ Animate SPRITE #################################
    player.update()
    camera.scroll()
    ################################# UPDATE WINDOW AND DISPLAY #################################
    #canvas.blit(fon, (0 - camera.offset.x, 0 - camera.offset.y))
    for i in range(len(tiles_arr)):
        canvas.blit(tiles_arr[i].img, (tiles_arr[i].rect.x - camera.offset.x, tiles_arr[i].rect.y - camera.offset.y))

    print(store)
    if store:
        btn = cr_btn.show()
        surf1 = pg.Surface((cr_btn.w, cr_btn.h))
        surf1.fill((255, 0, 0))
        canvas.blit(surf1, btn)

    canvas.blit(player.current_image,(player.rect.x - camera.offset.x, player.rect.y - camera.offset.y))

    screen.blit(canvas, (0,0))
    pygame.display.update()
