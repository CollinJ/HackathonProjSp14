from math import *

from pyglet.gl import *
import pyglet
import random


class GameOfLife(object):
    
    def __init__(self, x_size, y_size, z_size, list_map=None):
        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size
        if list_map is None:
            self.list_map = randomMap(x_size, y_size, z_size)
        else:
            self.list_map = list_map

    def getVertexList(self):
        vertex_list = list()
        for x in xrange(self.x_size):
            for y in xrange(self.y_size):
                for z in xrange(self.z_size):
                    if self.list_map[x][y][z] == 1:
                        vertex_list.append((x,y,z))
        return vertex_list

    def update(self):
        next_map = zeroMap(self.x_size, self.y_size, self.z_size)
        for x in xrange(self.x_size):
            for y in xrange(self.y_size):
                for z in xrange(self.z_size):
                    n = self.neighbors(x,y,z)
                    if 8 <= n <= 9:
                        next_map[x][y][z] = 1
                        continue
                    elif 6 <= n <= 7:
                        next_map[x][y][z] = self.list_map[x][y][z]
                        continue
                    else:
                        next_map[x][y][z] = 0
                        continue
        self.list_map = next_map
        
        
    def neighbors(self, x,y,z):
        neighbors = 0
        neighbors += 1 if ((0 <= x-1 < self.x_size) and (0 <= y-1 < self.y_size) and (0 <= z-1 < self.z_size) and self.list_map[x-1][y-1][z-1]) else  0
        neighbors += 1 if ((0 <= x-1 < self.x_size) and (0 <= y-1 < self.y_size) and (0 <= z < self.z_size) and self.list_map[x-1][y-1][z]) else  0
        neighbors += 1 if ((0 <= x-1 < self.x_size) and (0 <= y-1 < self.y_size) and (0 <= z+1 < self.z_size) and self.list_map[x-1][y-1][z+1]) else  0
        neighbors += 1 if ((0 <= x-1 < self.x_size) and (0 <= y < self.y_size) and (0 <= z-1 < self.z_size) and self.list_map[x-1][y][z-1]) else  0
        neighbors += 1 if ((0 <= x-1 < self.x_size) and (0 <= y < self.y_size) and (0 <= z < self.z_size) and self.list_map[x-1][y][z]) else  0
        neighbors += 1 if ((0 <= x-1 < self.x_size) and (0 <= y < self.y_size) and (0 <= z+1 < self.z_size) and self.list_map[x-1][y][z+1]) else  0
        neighbors += 1 if ((0 <= x-1 < self.x_size) and (0 <= y+1 < self.y_size) and (0 <= z-1 < self.z_size) and self.list_map[x-1][y+1][z-1]) else  0
        neighbors += 1 if ((0 <= x-1 < self.x_size) and (0 <= y+1 < self.y_size) and (0 <= z < self.z_size) and self.list_map[x-1][y+1][z]) else  0
        neighbors += 1 if ((0 <= x-1 < self.x_size) and (0 <= y+1 < self.y_size) and (0 <= z+1 < self.z_size) and self.list_map[x-1][y+1][z+1]) else  0
        neighbors += 1 if ((0 <= x < self.x_size) and (0 <= y-1 < self.y_size) and (0 <= z-1 < self.z_size) and self.list_map[x][y-1][z-1]) else  0
        neighbors += 1 if ((0 <= x < self.x_size) and (0 <= y-1 < self.y_size) and (0 <= z < self.z_size) and self.list_map[x][y-1][z]) else  0
        neighbors += 1 if ((0 <= x < self.x_size) and (0 <= y-1 < self.y_size) and (0 <= z+1 < self.z_size) and self.list_map[x][y-1][z+1]) else  0
        neighbors += 1 if ((0 <= x < self.x_size) and (0 <= y < self.y_size) and (0 <= z-1 < self.z_size) and self.list_map[x][y][z-1]) else  0
        #This is US not a neighbor neighbors += 1 if ((0 <= x < self.x_size) and (0 <= y < self.y_size) and (0 <= z < self.z_size) and self.list_map[x][y][z]) else  0
        neighbors += 1 if ((0 <= x < self.x_size) and (0 <= y < self.y_size) and (0 <= z+1 < self.z_size) and self.list_map[x][y][z+1]) else  0
        neighbors += 1 if ((0 <= x < self.x_size) and (0 <= y+1 < self.y_size) and (0 <= z-1 < self.z_size) and self.list_map[x][y+1][z-1]) else  0
        neighbors += 1 if ((0 <= x < self.x_size) and (0 <= y+1 < self.y_size) and (0 <= z < self.z_size) and self.list_map[x][y+1][z]) else  0
        neighbors += 1 if ((0 <= x < self.x_size) and (0 <= y+1 < self.y_size) and (0 <= z+1 < self.z_size) and self.list_map[x][y+1][z+1]) else  0
        neighbors += 1 if ((0 <= x+1 < self.x_size) and (0 <= y-1 < self.y_size) and (0 <= z-1 < self.z_size) and self.list_map[x+1][y-1][z-1]) else  0
        neighbors += 1 if ((0 <= x+1 < self.x_size) and (0 <= y-1 < self.y_size) and (0 <= z < self.z_size) and self.list_map[x+1][y-1][z]) else  0
        neighbors += 1 if ((0 <= x+1 < self.x_size) and (0 <= y-1 < self.y_size) and (0 <= z+1 < self.z_size) and self.list_map[x+1][y-1][z+1]) else  0
        neighbors += 1 if ((0 <= x+1 < self.x_size) and (0 <= y < self.y_size) and (0 <= z-1 < self.z_size) and self.list_map[x+1][y][z-1]) else  0
        neighbors += 1 if ((0 <= x+1 < self.x_size) and (0 <= y < self.y_size) and (0 <= z < self.z_size) and self.list_map[x+1][y][z]) else  0
        neighbors += 1 if ((0 <= x+1 < self.x_size) and (0 <= y < self.y_size) and (0 <= z+1 < self.z_size) and self.list_map[x+1][y][z+1]) else  0
        neighbors += 1 if ((0 <= x+1 < self.x_size) and (0 <= y+1 < self.y_size) and (0 <= z-1 < self.z_size) and self.list_map[x+1][y+1][z-1]) else  0
        neighbors += 1 if ((0 <= x+1 < self.x_size) and (0 <= y+1 < self.y_size) and (0 <= z < self.z_size) and self.list_map[x+1][y+1][z]) else  0
        neighbors += 1 if ((0 <= x+1 < self.x_size) and (0 <= y+1 < self.y_size) and (0 <= z+1 < self.z_size) and self.list_map[x+1][y+1][z+1]) else  0
        return neighbors


def randomMap(x_size, y_size, z_size):
    list_map = list()
    for x in xrange(x_size):
        x_list = list()
        for y in xrange(y_size):
            y_list = list()
            for z in xrange(z_size):
                y_list.append(random.randint(0,1))
            x_list.append(y_list)
        list_map.append(x_list)
    return list_map

def zeroMap(x_size, y_size, z_size):
    list_map = list()
    for x in xrange(x_size):
        x_list = list()
        for y in xrange(y_size):
            y_list = list()
            for z in xrange(z_size):
                y_list.append(0)
            x_list.append(y_list)
        list_map.append(x_list)
    return list_map



