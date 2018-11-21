#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Bus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self,name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)



if __name__ == "__main__":
    
    bus1 = Bus(['Alice','Bill'])
    print bus1.passengers

    bus1.pick('Charlie')
    bus1.drop('Alice')
    print bus1.passengers
    
    bus2 = Bus()
    bus2.pick('Carrie')
    print bus2.passengers

    print '-------'

    bus3 = Bus()
    print bus3.passengers
    bus3.pick('Dave')
    print bus2.passengers
    print bus3.passengers

    print '--------'
    bus4 = Bus()
    print bus4.passengers
    bus4.pick('Tom')
    print bus3.passengers
    print bus4.passengers


