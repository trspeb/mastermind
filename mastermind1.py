#!/usr/bin/env python

# Solving & playing MASTERMIND game
#
# Combination are represented as char string. The char # is reserved.
#

import random

class Combination:
    """
    Class representing a combination
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
        assert prop.len == self.len
        assert prop.len > 0
        
        rcrp = 0
        rcbp = 0
        iterm = self.iter.copy()
        # first we have to count rcrp:"right color right place"
        for i in self.iter:
            if self[i] == prop[i]:
                iterm.remove(i) # we should not check anymore at rcrp places
                rcrp += 1
#                print((rcrp,rcbp,prop.comb,i))
        # then we look at rcbp:"right color bad place"
        for i in iterm:
            for j in iterm:
                if self[i] == prop[j]:
                    prop[j] = "#"
                    rcbp += 1
#                    print((rcrp,rcbp,prop.comb,i,j))
                    break
        return(rcrp, rcbp)
        
    def __repr__(self):
        return(self.comb)

class RandomCombination(Combination):
    """
    Random combination class
    """
    keys = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    len_keys = len(keys)
    
    def __init__(self, n=4, c=6):
        assert c < self.len_keys
        comb = ""
        for i in range(n):
            comb += self.keys[random.randint(0,c-1)]
#        print(comb)
        super().__init__(comb)
        
class AIdumb:
    """
    Class implementing an automatic player, paying randomly without memory
    """        
    def __init__(self, game, silent=False):
        self.game = game
        
    def play(self):
        notwon = True
        i = 0
        while notwon:
            newtry = RandomCombination(n = self.game.n, c = self.game.c)
            rep = self.game.propose(newtry)
            notwon = (self.game.trace[-1][1][0] != 4)
            i = i+1
            print("{0} - {1}".format(i, rep))

class AInext:
    """
    Class implementing an methodic player, playong the next available combo
    """
    
    def __init__(self, game, silent=False):
        self.game = game
        
    def play(self):
        notwon = True
        i = 0
        while notwon:
            if (i==0):
                newtry = Combination("1"*self.game.n)
            else:
                # roll, brute force ?
                # find the next available combo !
                # recursively ??
                pass
            rep = self.game.propose(newtry)
            notwon = (self.game.trace[-1][1][0] != 4)
            i = i+1
            print("{0} - {1}".format(i, rep))

class Game:
    """
    Class representing a Game
    """

    def __init__(self, root=Combination("1234"), c=6, duplicates=False):
        self.root = root
        self.n = root.len
        self.c = c
        self.duplicates=duplicates
        self.trace = []
        
    def propose(self, combination):
        self.trace.append((combination, self.root == combination))
        return(self.trace[-1])
    
