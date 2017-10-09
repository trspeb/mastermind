#!/usr/bin/env python

"""
Solving & playing MASTERMIND game

Restarted for keep it simple. Combination are char strings that could be
reduced with a to_int conversion in base $n_{colors}$.
"""

class MasterAnswer:
	"""
	Represents a answer of the master
	
	rcrp means "right color right place"
	rcbp means "right color bad place"
	"""
	def __init__(self, rcrp = 0, rcbp = 0):
		self.rcrp = rcrp
		self.rcbp = rcbp
		
	def inc_rcrp(self):
		self.rcrp += 1
		
	def inc_rcbp(self):
		self.rcbp += 1
		
	def __add__(self, ma):
		self.rcrp += ma.rcrp
		self.rcbp += ma.rcbp

class Combination:
	"""
	Represent a combination
	"""
	def __init__(self, comb = "0110", n_colors = 6):
		assert len(comb) > 0
		self.comb = comb
		assert n_colors > 1 # the game is not funny with 1 color ;)
		self.n_colors = n_colors
		
	def len(self):
		return(len(self.comb))
		
	def dec(self):
		return(Combination(self.comb[1:], self.n_colors))

	def __getitem__(self, index):
		return(self.comb[index])
	
	def __mod__(self, comb2, combr2=""):
		assert self.comb.len() == comb2.len()
		
		if self.comb.len ==0:
			return(MasterAnswer())
		
		if self.comb[0] == self.comb2[0]:
			return(MasterAnswer(1, 0) + self.comb.dec() % comb2.dec())

	
		
