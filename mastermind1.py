#!/usr/bin/env python

# Playing a little with MASTERMIND game
#
# Combination are represented as char string. The char # is reserved.
#

import random

class Combination:
    """
    Class representing a combination
    
    to be tested with :
    
    1234 == 1234 => (4,0)
    1234 == 4321 => (0,4)
    1234 == 1242 => (2,1)
    1122 == 2111 => (1,2)
    1112 == 2221 => (0,2)
    3130 == 3120 => (3,0)
    """

    def __init__(self, comb="1234"):
        self.comb = comb
        self.len = len(comb)
        self.iter = list(range(self.len))
    
    def __getitem__(self, key):
        return(self.comb[key])

    def __setitem__(self, key, val):
        self.comb = self.comb[:key] + val + self.comb[key+1:]
        
    def __eq__(self, prop):
        assert prop.len==self.len
        
        rcrp = 0
        rcbp = 0
        iterm = self.iter.copy()
        # first we have to count "right color right place"
        for i in self.iter:
            if self[i] == prop[i]:
                iterm.remove(i) # we should not check anymore at rcrp places
                rcrp += 1
#                print((rcrp,rcbp,prop.comb,i))
        # then we look at "right color bad place"
        for i in iterm:
            for j in iterm:
                if self[i] == prop[j]:
                    prop[j] = "#"
                    rcbp += 1
#                    print((rcrp,rcbp,prop.comb,i,j))
                    break
        return(rcrp, rcbp)

class RandomCombination(Combination):
    """
    Random combination class
    """
    def __init__(self, n=4, c=6):
        comb = ""
        for i in range(n):
            comb += str(random.randint(0,c-1))
        print(comb)
        super().__init__(comb)
        
class Game:
    """
    Class representing a Game
    """

    def __init__(self, root="1234", n=4, duplicates=False):
        self.root = root
        self.n = len(root)
        self.duplicates=duplicates
        self.trace = []

        
    
            



