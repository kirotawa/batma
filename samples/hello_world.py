# -*- coding:utf-8 -*-

import sys
import os
sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__), '..')))

import batma

class Game(batma.Game):
    def initialize(self):
        pass
    
    def load_content(self):
        self.label = batma.Label(u'Hello World!', (320, 240))

    def update(self, tick):
        pass
    
    def draw(self):
        self.label.draw()

game = Game()
batma.run()