import os

import pygame as pg


can_move_arr = ['grass', 'nike']

def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pg.image.load(fullname).convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [list(line.strip()) for line in mapFile]
    return level_map


def can_move(player, x, y, arr, direction):
    if direction == "up":
        obj = arr[y - 1][x]
        if obj.status in can_move_arr:
            return False
        return True
    if direction == "down":
        obj = arr[y + 1][x]
        if obj.status in can_move_arr:
            return False
        return True
    if direction == "left":
        obj = arr[y][x - 1]
        if obj.status in can_move_arr:
            return False
        return True
    if direction == "right":
        obj = arr[y][x + 1]
        if obj.status in can_move_arr:
            return False
        return True


def near_store(x, y, arr):
    if arr[y - 1][x].status == 'nike' or arr[y + 1][x].status == 'nike' or arr[y][x - 1].status == 'nike' or arr[y][x + 1].status == 'nike':
        return True
    return False
