#!/usr/bin/env python

# Solving & playing MASTERMIND game
#
# Combination are represented as char string. The char # is reserved.
#
# @todo base Wouldn't it be easier to implement in int, through base calculation ?
#

import random

class Combination:
    """
    Class representing a combination
    """
    keys = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    len_keys = len(keys)

    def __init__(self, comb="0110"):
        self.comb = comb
        self.len = len(comb)
        self.iter = list(range(self.len))
    
    def __getitem__(self, key):
        return(self.comb[key])

    def __setitem__(self, key, val):
        self.comb = self.comb[:key] + val + self.comb[key+1:]
        
    def __eq__(self, propc):
        assert propc.len == self.len
        assert propc.len > 0
        
        prop = Combination(propc.comb)
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
        
    def next(self, c = 6):
        """
        Look at the "next" combination, knowing "color base" and digit number

        In case no next combination exists, "0"*self.len is return
        """
        i = 0
        temp = self.comb
        while (i < self.len):
            j = self.keys.find(temp[i])
            if (j < (c-1)):
                temp = temp[:i] + self.keys[j+1] + temp[(i+1):]
                return(Combination(temp))
            else:
                temp = temp[:i] + self.keys[0] + temp[(i+1):]
                i = i + 1
        return(Combination("0"*self.len))

    def next2(self, c = 6):
        """
        Alternative implementation of next method

        In case no next combination exists, "0"*self.len is return        
        """
        temp = ""
        fin = True
        for i in self.comb:
            j = self.keys.find(i)
            if ((j < (c-1))&fin):
                temp += self.keys[j+1]
                fin = False
            elif not(fin):
                temp += i
            else:
                temp += self.keys[0]
        if fin:
            temp = "0"*self.len
        return(Combination(temp))

class RandomCombination(Combination):
    """
    Random combination class
    """    
    def __init__(self, n=4, c=6):
        assert c < self.len_keys
        comb = ""
        for i in range(n):
            comb += self.keys[random.randint(0,c-1)]
        super().__init__(comb)
        
class AIdumb:
    """
    Class implementing an automatic player, paying randomly without memory
    """        
    def __init__(self, game, silent=False):
        self.game = game
        
    def play(self, max = 1e6):
        notwon = True
        i = 0
        while (notwon & (i<max)):
            newtry = RandomCombination(n = self.game.n, c = self.game.c)
            rep = self.game.propose(newtry)
            notwon = (self.game.trace[-1][1][0] != 4)
            i = i+1
            print("{0} - {1}".format(i, rep))

class AIdumbnext:
    """
    Class implementing an methodic dumb player, playing the next combo
    """
    
    def __init__(self, game, silent=False):
        self.game = game
        
    def play(self, max = 1e6):
        notwon = True
        i = 0
        while (notwon & (i<max)):
            if (i==0):
                newtry = Combination("0"*self.game.n)
            else:
                # roll, brute force ?
                # find the next available combo !
                # recursively ??
                # would be more rational to build a ruleset ?
                newtry = self.game.trace[-1][0].next(self.game.c)
                pass
            rep = self.game.propose(newtry)
            notwon = (self.game.trace[-1][1][0] != 4)
            i = i+1
            print("{0} - {1}".format(i, rep))

class AInext:
    """
    Class implementing an methodic dumb player, playong the next available combo
    """
    
    def __init__(self, game, silent=False):
        self.game = game
        
    def play(self, start = None, max = 1e6):
        if start == None:
            start = "0"*self.game.n
        notwon = True
        i = 0
        while (notwon & (i<max)):
            if (i==0):
                newtry = Combination(start)
            elif (i>max):
                print("max iteration reached!!!")
                break
            else:
                newtry = Combination("0"*self.game.n)
                while not(self.available(newtry)):
                    newtry = newtry.next(self.game.c)
            rep = self.game.propose(newtry)
            notwon = (self.game.trace[-1][1][0] != 4)
            i = i+1
            print("{0} - {1}".format(i, rep))
        return(i)
            
    def available(self, comb):
        """
        Tell me if this combination is available, from past master answers
        """
        # for a combination to be available, all past answers have to match
        g = Game(comb, self.game.c, self.game.duplicates) # if the solution were *comb*
        ret = True
        for d in self.game.trace:
            ret &= ((g.root == d[0])==d[1])
        return(ret)

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
    
def testAll():
    """
    This function tries all starting combinations
    """
    c = Combination("0000")
    results = []
    first = True
    while ((c.comb != "0000") | first):
        first = False
        g = Game(c)
        ai = AInext(g)
        results.append(ai.play("1234"))
        c = c.next(4)
    return(results)
