"""
MONITORES PARA LOS FILOSOFOS

from multiprocessing import Process
from multiprocessing import Condition, Lock, Manager
from multiprocessing import Value
from multiprocessing import current_process
import time, random

"""
from multiprocessing import Condition, Lock, Manager
#K=100
#NPHIL = 5 #numero de filosofos

class Table(object):
    def __init__(self,NPHIL,manager):
        self.eating = 0 #Value('i', 0) #numero de filosofos comiendo
        self.NPHIL = NPHIL
        self.phil = manager.list([False]*NPHIL) #true si el filosofo i esta comiendo
        self.current_phil = None
        #los semaforos necesarios
        self.mutex = Lock()
        self.free_fork = Condition(self.mutex)
        
    def set_current_phil(self,current): #current es el numero del proceso actual
        self.current_phil = current
          
    def no_lr_eating(self): #no estan comiendo los de al lado del filosofo i
        i = self.current_phil
        return not self.phil[(i-1)%(self.NPHIL)] and not self.phil[(i+1)%(self.NPHIL)]

    def wants_eat(self,num): #i es el filosofo
        self.mutex.acquire()
        self.set_current_phil(num)
        self.free_fork.wait_for(self.no_lr_eating)
        self.phil[num] = True
        self.eating += 1
        self.mutex.release()

    def wants_think(self,num):
        self.mutex.acquire()
        self.phil[num] = False
        self.eating -= 1
        #self.no_writers.notify_all()
        self.free_fork.notify()
        self.mutex.release()

class CheatMonitor(object):
    def __init__(self):
        self.eating = 0 #Value('i', 0) #numero de filosofos comiendo
        #self.NPHIL = NPHIL
        self.phil = manager.list([False]*NPHIL) #true si el filosofo i esta comiendo
        self.hungry = anager.list([False]*NPHIL) #true si el filosofo i quiere comer pero no puede
        self.current_phil = None
        #los semaforos necesarios
        self.mutex = Lock()
        self.free_fork = Condition(self.mutex)
        self.chungry = Condition(self.mutex)
        
    def set_current_phil(self,current): #current es el numero del proceso actual
        self.current_phil = current
          
    def no_lr_eating(self): #no estan comiendo los de al lado del filosofo i
        i = self.current_phil
        return not self.phil[(i-1)%(self.NPHIL)] and not self.phil[(i+1)%(self.NPHIL)]
   
    def not_hungry(self):
        i = self.current_phil
        return not self.hungry[(i+1)%(self.NPHIL)]

    def wants_eat(self,num): #i es el filosofo
        self.mutex.acquire()
        self.set_current_phil(num)
        self.chungry.wait_for(self.not_hungry)
        self.hungry[num] = True
        self.free_fork.wait_for(self.no_lr_eating)
        self.phil[num] = True
        self.eating += 1
        self.hungry[num] = True
        self.mutex.release()

    def wants_think(self,num):
        self.mutex.acquire()
        self.phil[num] = False
        self.eating -= 1
        #self.no_writers.notify_all()
        self.free_fork.notify()
        self.mutex.release()
 
#    def is_eating(self):
#        self.eating += 1
        


"""
    def want_eat(self,num): #i es el filosofo
        self.mutex.acquire()
        self.chungry.wait_for(self.not_hungry())
        self.hungry[num] = True
        set_current_phil(self,num)
        self.free_fork.wait_for(self.n...())
        self.phil[num] = True
        self.eating += 1
        self.hungry[num] = True
        self.mutex.release()


    def want_think(self,num):
        self.mutex.acquire()
        self.phil[num] = False
        self.eating -= 1
        #self.no_writers.notify_all()
        self.free_fork.notify()
        self.mutex.release()
"""