import random as rd
import string
import matplotlib.pyplot as plt
import math
import numpy as np

#print rd.randint(0,9)
#print rd.choice(string.ascii_letters)

#cos python strings a fucking immutable for some reason
def replaceChar(string,char,index):
	s = string[:index-1]
	s = s + char + string[index:]
	return s


class DNA(object):
	#def __init__(self):
		#print "hello"


	#Generate random words
	def randWord(self,num):
		word = ''
		for n in range(0,num):
			word = word + rd.choice(string.ascii_letters + ' ')
		return word

class population(object):

	def __init__(self,phrase,mutationRate,popmax):
		self.phrase = phrase
		self.mutationRate = mutationRate
		self.popmax = popmax

	def initpool(self):
		pool = []
		for i in range(0,self.popmax):
			pool.append(DNA().randWord(len(self.phrase)))
		return pool
		
	def generate(self,pool,score):
		#Normalize the score to percentage list
		score = [float(x*100/len(self.phrase)) for x in score]
		if sum(score) != 0:
			normScore = [float(x/sum(score)) for x in score]
		else:
			return 1

		#start creating pool of children
		child = []
		for n in range(0,self.popmax):
			#find the two parents to create a child
			index1 = np.random.choice(np.arange(0,self.popmax), p=normScore)
			index2 = np.random.choice(np.arange(0,self.popmax), p=normScore)
			child.append((pool[index1][:len(self.phrase)/2] + pool[index2][len(self.phrase)/2:])) 
			#mutate the child given mutation rate
			x = rd.randrange(0,int(math.floor(1/self.mutationRate)))
			if  x == 0:
				child[n] = replaceChar(child[n],rd.choice(string.ascii_letters + ' '),(rd.randrange(0,len(child[n]))+1))
		return child



	def evaluate(self,pool):
		score = []
		for i in range(0,len(pool)):
			score.append(0)
			for n in range(0,len(self.phrase)):
				if pool[i][n] == self.phrase[n]:
					score[i] += 1
			if score[i] == len(self.phrase):
				return 1
		print 'Average fitness = ' + str((sum(score)*100/len(score))/len(self.phrase)) + '%'
		return score

#Here is a function to draw the data in a matplot


def main():
	score = 0
	iteration = 0
	#print "Please input desired phrase:"
	#phrase = raw_input()
	#print "Please input mutation rate:"
	#mutationRate = raw_input()
	#print "Please input max population:"
	#popmax = raw_input()
	phrase = 'Hello'
	mutationRate = 0.05
	popmax = 10
	num = len(phrase)
	a = population(phrase,mutationRate,popmax)
	curPool = a.initpool()
	score = a.evaluate(curPool)
	gen = a.generate(curPool,score)

	#print replaceChar(phrase,'h',len(phrase))
	
	while iteration < 10000:

		if gen == 1:
			gen = a.initpool()
		else:
			score = a.evaluate(gen)
			if score != 1:
				gen = a.generate(gen,score)
				print gen
			else:
				print score
				print gen
				print "The generation is " + str(iteration)
				return 0
		iteration += 1
		#print a.initpool()
		#Loop until all the letters match or iteration is reached

if __name__ == "__main__":
	main()