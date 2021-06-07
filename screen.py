# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)

'''
    Here starts refactored code
    Usable links:
    https://pythonworld.ru/osnovy/peregruzka-operatorov.html - here some information about methods and their overload

'''
# actual file

class Vec2d:
    """ Class for 2-dimensinal vectors """
    def __init__(self, x,  y):
        try:
            self.x = int(x)
            self.y = int(y)
        except:
            raise(ValueError)

    def __add__(self, other):
        """ Returns sum of two vectors """
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """" Returns subtraction between vectors """
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, num):
        """ Returns multiplication between number and vector """
        return Vec2d(self.x * num, self.y * num)

    def __len__(self):
        """ Returns length of vector (integer!) """
        return int(math.sqrt(self.x * self.x + self.y * self.y))

    def int_pair(self):
        """ Returns coordinates of vector """
        return (self.x, self.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return (self.x == other.x, self.y == other.y)


class Polyline:
    """ Class for closed curves """
    def __init__(self):
        self.points_lst = []
        self.speeds_lst = []

    def new_point(self, x, y):
        """ Adding new point """
        self.points_lst.append(Vec2d(x, y))
        self.speeds_lst.append(Vec2d(random.random() * 2, random.random() * 2))

    def del_point(self):
        """ Delete last point """
        self.points_lst.pop()
        self.speeds_lst.pop()

    def set_points(self):
        """ Recalculating points coordinates """
        for indx in range(len(self.points_lst)):
            points = self.points_lst[indx] + self.speeds_lst[indx]
            if points.x > SCREEN_DIM[0] or points.x < 0:
                self.speeds_lst[indx] = Vec2d(-self.speeds_lst[indx].x,
                self.speeds_lst[indx].y)
            if points.y > SCREEN_DIM[1] or points.y < 0:
                self.speeds_lst[indx] = Vec2d(self.speeds_lst[indx].x,
                -self.speeds_lst[indx].y)

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """ Drawing of broken curve """
        # should I recieve gameDisplay or take it from instance of another class?
        if style == "line":
            for p_n in range(-1, len(self.points_lst) - 1):
                pygame.draw.line(ScreenSaver.gameDisplay, color,
                                self.points_lst[p_n].int_pair(),
                                self.points_lst[p_n + 1].int_pair(), width)
        elif style == "points":
            for p in self.points_lst:
                pygame.draw.circle(ScreenSaver.gameDisplay, color, p.int_pair(), width)

    def change_speed(self, insrease=True):
        """ Increasing or Decreasing speed """
        for i in self.speeds_lst:
            if increase:
                i = i * (1 + 0.5)
            else:
                i = i * 0.5


class Knot(Polyline):
    """ Class Knot """
    def get_knot(self, count):
        if len(self.points_lst) < 3:
            return []
        ref_points = []
        for i in range(-2, len(self.points_lst) - 2):
            ptn = []
            ptn.append((self.points_lst[i] + self.points_lst[i + 1]) * 0.5)
            ptn.append(self.points_lst[i + 1])
            ptn.append((self.points_lst[i + 1] + points[i + 2]) * 0.5)
            ref_points.extend(self.get_points(ptn, count))
        return ref_points

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_point(self, base_points, alpha, deg=None):
        if deg is None:
            deg = len(base_points) - 1
        if deg == 0:
            return base_points[0]
        return (base_points[deg] * alpha) + self.get_point(base_points, alpha, deg - 1) * (1 - alpha)


class HelpScreen:
    """ Class for screen of Help """
    def __init__(self):
        self.data = [
                    ["F1", "Show Help"],
                    ["R", "Restart"]
                    ["P", "Pause/Play"],
                    "Num+", "More points"],
                    ["Num-", "Less points"],
                    ["I", "Increase speed"],
                    ["D", "Decrease speed"],
                    ["Del, Delete last point"],
                    ["", ""],
                    [str(steps), "Current points"]
                    ]
        gameDisplay.fill((50, 50, 50))
        self.font1 = pygame.font.SysFont("courier", 24)
        self.font2 = pygame.font.SysFont("serif", 24)

    def draw_help(self):
        """ Drawing screen of Help """
        pygame.draw.lines(ScreenSaver.gameDisplay, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(self.data):
            ScreenSaver.gameDisplay.blit(self.font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            ScreenSaver.gameDisplay.blit(self.font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


class ScreenSaver:
    """ Class to start excution of ScreenSaver """
    def __init__(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode(SCREEN_DIM)
        pygame.display.set_caption("MyScreenSaver")
        self.steps = 35
        self.working = True
        self.show_help = False
        self.pause = True
        self.knot = Knot()
        self.hue = 0
        self.color = pygame.Color(0)

    def run(self):
        """ runs screensaver """
        while working:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.working = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.working = False
                    if event.key == pygame.K_r: # key r
                        self.knot = Knot()
                    if event.key == pygame.K_p: # key p
                        self.pause = not self.pause
                    if event.key == pygame.K_KP_PLUS:
                        self.steps += 1
                    if event.key == pygame.K_F1:
                        self.show_help = not self.show_help
                    if event.key == pygame.K_KP_MINUS:
                        self.steps -= 1 if self.steps > 1 else 0
                    if event.key == pygame.K_i:
                        self.knot.change_speed()
                    if event.key == pygame.K_d:
                        self.knot.change_speed(False)
                    if event.key == pygame.K_DELETE:
                        self.knot.del_point()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.knot.new_point(x, y)

            self.gameDisplay.fill((0, 0, 0))
            self.hue = (self.hue + 1) % 360
            self.color.hsla = (self.hue, 100, 50, 100)
            self.knot.draw_points()
            self.knot.draw_points(self.knot.get_knot(self.steps), "line", 3, self.color)
            if not self.pause:
                self.knot.set_points()
            if show_help:
                HelpScreen().draw_help()

            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()
        exit(0)



if __name__ == "__main__":
    screen_s = ScreenSaver()
    screen_s.run()
