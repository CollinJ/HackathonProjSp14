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
                    if self.list_map[x][y][z] > 0:
                        vertex_list.append((x,y,z, self.list_map[x][y][z]))
        return vertex_list

    def update(self):
        next_map = zeroMap(self.x_size, self.y_size, self.z_size)
        for x in xrange(self.x_size):
            for y in xrange(self.y_size):
                for z in xrange(self.z_size):
                    n = self.neighbors(x,y,z)
                    next_map[x][y][z] = self.next_value(n, self.list_map[x][y][z])
        self.list_map = next_map
        
        
    def neighbors(self, x,y,z):
        neighbors = [0,0,0]
        for dx in xrange(-1,2):
            for dy in xrange(-1,2):
                for dz in xrange(-1,2):
                  if (0 <= x+dx < self.x_size) and (0 <= y+dy < self.y_size) and (0 <= z+dz < self.z_size) and not (x+dx == y+dy == z+dz == 0):
                      neighbors[self.list_map[x+dx][y+dy][z+dz]] += 1
        return neighbors

    def next_value(self, neighbors, curr):
        if curr == 0:
            if neighbors[1] == 0 and (3 <= neighbors[2] <= 4):
                return 2
            elif neighbors[2] == 0 and (3 <= neighbors[1] <= 4):
                return 1
        elif curr == 1:
          if neighbors[1] > neighbors[2] and neighbors[1] < 8 and neighbors[1] > 2:
              return 1
          else:
              return 0
        elif curr == 2:
          if neighbors[2] > neighbors[1] and neighbors[2] < 8 and neighbors[2] > 2:
              return 2
          else:
              return 0
        return 0




def randomMap(x_size, y_size, z_size):
    list_map = list()
    for x in xrange(x_size):
        x_list = list()
        for y in xrange(y_size):
            y_list = list()
            for z in xrange(z_size):
                y_list.append(random.randint(0,2))
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



