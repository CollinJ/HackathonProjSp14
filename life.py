from math import *

from pyglet.gl import *
import pyglet
from random import random,randint
from bisect import bisect

class GameOfLife(object):
    
    def __init__(self, x_size, y_size, z_size, list_map=None, B=None, S=None):
        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size
        if list_map is None:
            self.list_map = randomMap(x_size, y_size, z_size, 1)
        else:
            self.list_map = list_map
        self.B = [4,5] if B is None else B
        self.S = [5] if S is None else S

    def reset(self):
        self.list_map = randomMap(self.x_size, self.y_size, self.z_size, 1)

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
                  if not (dx == dy == dz == 0):
                      neighbors[self.list_map[(x+dx)%self.x_size][(y+dy)%self.y_size][(z+dz)%self.z_size]] += 1
                  #if (0 <= x+dx < self.x_size) and (0 <= y+dy < self.y_size) and (0 <= z+dz < self.z_size) and not (dx == dy == dz == 0):
                  #    neighbors[self.list_map[x+dx][y+dy][z+dz]] += 1
        return neighbors

    def next_value(self, neighbors, curr):
        if neighbors[1] in self.B and curr == 0:
            return 1
        elif neighbors[1] in self.S and curr == 1:
            return 1
        #elif 11 <= neighbors[1] <= 15:
        #    return 1
        #elif 6 <= neighbors[1] <= 6:
        #    return 1
        return 0
        

class GameOfLife2D(object):
    
    def __init__(self, x_size, y_size, z_size, list_map=None):
        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size
        if list_map is None:
            self.list_map = random2DMap(x_size, y_size, z_size, 1)
        else:
            self.list_map = list_map
        self.B = [3]
        self.S = [2,3]

    def reset(self):
        self.list_map = random2DMap(self.x_size, self.y_size, self.z_size, 1)

    def getVertexList(self):
        vertex_list = list()
        for x in xrange(self.x_size):
            for y in xrange(self.y_size):
                for z in xrange(self.z_size):
                    if self.list_map[x][y][z] > 0:
                        vertex_list.append((x,y,z,x==0))
        return vertex_list

    def update(self):
        next_map = zeroMap(self.x_size, self.y_size, self.z_size)
        for x in xrange(self.x_size):
            if x == 0:
              for y in xrange(self.y_size):
                  for z in xrange(self.z_size):
                      n = self.neighbors(x,y,z)
                      next_map[x][y][z] = self.next_value(n, self.list_map[x][y][z])
            else:
                next_map[x] = self.list_map[x-1]
        self.list_map = next_map
        
        
    def neighbors(self, x,y,z):
        neighbors = [0,0,0]
        for dy in xrange(-1,2):
            for dz in xrange(-1,2):
              if not (dy == dz == 0):
                  neighbors[self.list_map[0][(y+dy)%self.y_size][(z+dz)%self.z_size]] += 1
              #if (0 <= x+dx < self.x_size) and (0 <= y+dy < self.y_size) and (0 <= z+dz < self.z_size) and not (dx == dy == dz == 0):
              #    neighbors[self.list_map[x+dx][y+dy][z+dz]] += 1
        return neighbors

    def next_value(self, neighbors, curr):
        if neighbors[1] in self.B and curr == 0:
            return 1
        elif neighbors[1] in self.S and curr == 1:
            return 1
        #elif 11 <= neighbors[1] <= 15:
        #    return 1
        #elif 6 <= neighbors[1] <= 6:
        #    return 1
        return 0
class GameOfWar(object):
    
    def __init__(self, x_size, y_size, z_size, list_map=None):
        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size
        if list_map is None:
            self.list_map = randomMap(x_size, y_size, z_size, 2)
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
            if neighbors[1] < 2 and (4 <= neighbors[2] <= 5):
                return weighted_choice([(0,1),(2,1)])
            elif neighbors[2] < 2 and (4 <= neighbors[1] <= 5):
                return weighted_choice([(0,1),(1,1)])
        elif curr == 1:
          if neighbors[1] < 8 and neighbors[1] > 2:
              return weighted_choice([(0, neighbors[2]), (1, neighbors[1]), (2, neighbors[2]*3)])
          else:
              return 0
        elif curr == 2:
          if neighbors[2] < 8 and neighbors[2] > 2:
              return weighted_choice([(0, neighbors[1]), (2, neighbors[2]), (1, neighbors[1]*3)])
          else:
              return 0
        return 0


    def reset(self):
        self.list_map = randomMap(self.x_size, self.y_size, self.z_size, 2)


def randomMap(x_size, y_size, z_size, max_int):
    list_map = list()
    for x in xrange(x_size):
        x_list = list()
        for y in xrange(y_size):
            y_list = list()
            for z in xrange(z_size):
                y_list.append(randint(0,max_int*20)<=max_int)
            x_list.append(y_list)
        list_map.append(x_list)
    return list_map

def random2DMap(x_size, y_size, z_size, max_int):
    list_map = list()
    for x in xrange(x_size):
        x_list = list()
        for y in xrange(y_size):
            y_list = list()
            for z in xrange(z_size):
                if(x==0):
                    y_list.append(randint(0,max_int))
                else:
                    y_list.append(0)
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

def weighted_choice(choices):
    values, weights = zip(*choices)
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random() * total
    i = bisect(cum_weights, x)
    return values[i]


