# This file is responsbile for everything that happens on the starship live

import time
import threading

class SystemLoop:
    def __init__(self):
        self._power = 100
    
    def getPower(self):
        return self._power
    
    power = property(getPower)
    
    def systemLoop(self):
        while True:
            self._power -= 1
            
            #frame rate
            time.sleep(1)

