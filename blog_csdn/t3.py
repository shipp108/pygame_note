import math
import random

PI 		= math.pi
TWO_PI 	= PI * 2.0
HALF_PI	= PI / 2.0

iFramesPerSecond 		= 60
iNumHidden 				= 1
iNeuronsPerHiddenLayer 	= 10
iNumOutputs 			= 2
dActivationResponse		= 1.0
dMaxTurnRate			= 0.2
dMaxSpeed 				= 2.0
iSweeperScale 			= 5
iNumSensors				= 5
dSensorRange			= 25
iNumSweepers			= 40
iNumTicks				= 2000
dMineScale 				= 2
dCrossoverRate			= 0.7
dMutationRate 			= 0.1
dMaxPerturation			= 0.3
iNumElite				= 4
iNumCopiesElite			= 1
dCellSize				= 20.0
iTouramentCompetitors 	= 5

WindowWidth				= 640
WindowHeight 			= 480

# CNN
class SNeuron(object):
	def __init__(self, NumInputs):
		self._NumInputs = NumInputs
		self._Weights 	= []
		
		for i in xrange(self._NumInputs):
			self._Weights.append(random.random() - random.random())	# generate random weight from -1 to 1
		return

class SNeuronLayer(object):
	def __init__(self, NumNeurons, NumInputsPerNeuron):
		self._NumNeurons 	= NumNeurons
		self._Neurons 		= []
		
		for i in xrange(self._NumNeurons):
			self._Neurons.append(SNeuron(NumInputsPerNeuron))
		return
		
class CNeuralNet(object):
	def __init__(self, NumInputs, NumOuputs, NumHidden, NeuronsPerHiddenLayer):
		self._NumInputs 			= NumInputs
		self._NumOutoputs 			= NumOutputs
		self._NumHiddenLayers 		= NumHidden
		self._NeuronsPerHiddenLyr 	= NeuronsPerHiddenLayer
		self._Layers 				= []
		
		self.CreateNet()
		return 

	def CreateNet(self):
		if self._NumHiddenLayers > 0:
			# inputs layer
			self._Layers.append(SNeuronLayer(self._NeuronsPerHiddenLyr, self._NumInputs))
			# hidden layers
			for i in xrange(self._NumHiddenLayers):
				self._Layers.append(SNeuronLayer(self._NeuronsPerHiddenLyr, self._NeuronsPerHiddenLyr))
			# outpur layer
			self._Layer.append(SNeuronLayer(self._NumOuputs, self._NeuronsPerHiddenLyr))
		else:
			self._Layer.append(SNeuronLayer(self._NumOuputs, self._NumInputs))
	
	
	def GetWeights(self):
		weights = []
		for i in xrange(self._NumHiddenLayers + 1):
			for j in xrange(self._Layers[i]._NumNeurons):
				for k in xrange(self._Layers[i]._Neurons[j]._NumInputs):
					weights.append(self._Layers[i]._Neurons[j]._Weights[k])
					
		return weights
	
	def PutWeights(self, weights):
		weightIdx = 0
		for i in xrange(self._NumHiddenLayers + 1):
			for j in xrange(self._Layers[i]._NumNeurons):
				for k in xrange(self._Layers[i]._Neurons[j]._NumInputs):
					self._Layers[i]._Neurons[j]._Weights[k] = weights[weightIdx]
					weightIdx += 1
		
		return
	
	def Update(self, inputs):
		outputs 	= []
		weightIdx 	= 0
		
		if len(inputs) != self._NumInputs:
			print "input size not equal _NumInputs"
			return outputs
			
		for i in xrange(self._NumHiddenLayers + 1):
			if i > 0: 
				# hidden layer input is the last layer's output
				inputs = copy.deepcopy(outputs)
		
			outputs 	= []
			weightIdx 	= 0
			
			for j in xrange(self._Layers[i]._NumNeurons):
				netInputs = 0.0
				NumInputs = self._Layers[i]._Neurons[j]._NumInputs
				
				for k in xrange(NumInputs - 1):
					 netInputs += (self._Layers[i]._Neurons[j]._Weights[k] * inputs[weightIdx])
					 weightIdx += 1
		
				netInputs += (self._Layers[i]._Neurons[j].Weights[NumInputs - 1] * dBias) 	# dBias = -1
				outputs.append(slef.Sigmoid(netInputs, dActivationResponse))				# dActivationResponse = 1
				weightIdx = 0
		
		return outputs
	
	def Sigmoid(self, netinputs, activationResponse):
		return 1.0 / (1.0 + math.exp(-netinputs / activationResponse))
		
	def CalculateSplitPoints(self):
		SplitPoints = []
		WeightCounter = 0
		
		for i in xrange(self._NumHiddenLayers + 1):
			for j in xrange(self._Layers[i]._NumNeurons):
				for k in xrange(self._Layers[i]._Neurons[j]._NumInputs):
					WeightsCounter += 1
				SplitPoints.append(WeightCounter - 1)
		
		print SplitPoints
		return SplitPoints
		
# SGenome
class SGenome(object):
	def __init__(self, numWeights):
		self._vecWeights = []
		self._dFitness = 0.0
		for i in xrange(numWeights):
			self._vecWeights.append(random.random() - random.random())	# generate a random double in the range (-1, 1)
		
	def __lt__(self, sgenome):
		return self._dFitness < sgenome._dFitness

# GA
class GA(object):
	def __init__(self, PopSize, MutationRate, CrossoverRate, NumWeights):
		self._vecPop 			= []
		self._vecSplitPoints 	= []
		self._iPopSize 			= PopSize
		self._iChromoLength 	= NumWeights
		self._dMutationRate		= MutationRate
		self._dCrossoverRate 	= CrossoverRate
		self._dBestFitness		= 0.0
		self._dAverageFitness 	= 0.0
		self._dWorstFitness		= 99999999
		self._dTotalFitness 	= 0.0
		self._iFittestGenome 	= 0
		self._iGeneration 		= 0
		
		self.CreatePopulation()
		return 
	
	def Reset(self);
		self._dTotalFitness 	= 0.0
		self._dBestFitness 		= 0.0
		self._dWorstFitness 	= 99999999
		self._dAverageFitness 	= 0.0
		
	def CreatePopulation(self):
		self._vecPop = []
		self._iFittestGenome 	= 0
		self._iGeneration 		= 0
		
		self.Reset()
		for i in xrange(self._iPopSize):
			self._vecPop.append(SGenome(self._ChromoLength))
		
		
	def GetChromoRoulette(self):
		Slice = random.random() * self._dTotalFitness
		TheChosenOne = None
		FitnessSoFar = 0
		
		for i in xrange(self._PopSize):
			FitnessSoFar += self._vecPop[i]._dFitness
			if FitnessSoFar >= Slice:
				TheChosenOne = copy.deepcopy(self._vecPop[i])
				break
			
		return TheChosenOne


	def GetTournamentSelection(self, n):
		BestFitnessSoFar 	= -999999
		ChosenOne 			= 0
	
		# select n members from the population at random testing against
		# the best found so far
		for i in xrange(n):
			ThisTry = random.randint(0, self._iPopSize - 1)
			if self._vecPop[ThisTry]._dFitness > BestFitnessSoFar:
				ChosenOne = ThisTry
				BestFitnessSoFar = self._vecPop[ThisTry]._dFitness
		
		return self._vecPop[ChosenOne]			
	
	
	def Mutate(self, chromo):
		newChromo = []
		for idx, gene in enumerate(chromo):
			if random.random() < self._dMutationRate:
				gene += (random.random() - random.random()) * dMaxPerturbation 				# dMaxPerturbation = 0.3
			newChromo.append(gene) 
		return newChromo
		
	def Crossover(self, mum, dad):
		baby1 = []
		baby2 = []
		
		if random.random() > self._dCrossoverRate or mum == dad:
			baby1 = copy.deepcopy(mum)
			baby2 = copy.deepcopy(dad)
		else:
			cp = random.randint(0, self._iChromoLength - 1)
			baby1 = mum[:cp] + dad[cp:]
			baby2 = dad[:cp] + mum[cp:]
		
		return baby1, baby2
	
	def CrossoverAtSpilts(self, mum, dad):
		baby1 = []
		baby2 = []
		
		if random.random() > self._dCrossoverRate or mum == dad:
			baby1 = copy.deepcopy(mum)
			baby2 = copy.deepcopy(dad)
		else:
			cpIdx1 = random.randint(0, len(self._vecSpiltPoints) - 2)
			cp1 = self._vecSplitPoints[cpIdx1]
			cp2 = self._vecSplitPoints[random.randint(cpIdx1, len(self._vecSplitPoints) - 1)]
			baby1 = num[:cp1] + dad[cp1:cp2] + mum[cp2:]
			baby2 = dad[:cp1] + mum[cp1:cp2] + dad[cp2:]
		
		return baby1, baby2
	
	def GrabNBest(self, NBest, NumCopies):
		newPop = []
		popIdx = self._iPopSize - 1 - NBest
		for i in xrange(NBest):
			for j in xrange(NumCopies):
				newPop.append(self._vecPop[popIdx])
			popIdx += 1
		return newPop
	
	def Epoch(self, old_pop):
		self._vecPop = copy.deepcopy(old_pop)
		self.Reset()
		self._vecPop.sort()
		self.CalculateBestWorstAvTot()
		
		vecNewPop = []
		if (iNumCopiesElite * iNumElite) % 2 == 0:
			vecNewPop = self.GrabNBest(iNumElite, iNumCopiesElite)
			
		while len(vecNewPop) < self._iPopSize:
			mum = self.GetChromoRoulette()
			dad = self.GetChromoRoulette()
			baby1, baby2 = self.CrossoverAtSplits(mum._vecWeights, dad._vecWeights)
			baby1 = self.Mutate(baby1)
			baby2 = self.Mutate(baby2)
			
			vecNewPop.append(baby1)
			vecNewPop.append(baby2)
			
		self._vecPop = copy.deepcopy(vecNewPop)
		return self._vecPop
		
	def CalculateBestWorstAvTot(self):
		self._dTotalFitness = 0.0
		HighestSoFar 		= 0
		LowestSoFar 		= 9999999
		
		for i in xrange(self._iPopSize):
			CurrPopFitness = self._vecPop[i]._dFitness
			if CurrPopFitness > HighestSoFar:
				HighestSoFar 			= CurrPopFitness
				self._dBestFitnest 		= HighestSoFar
				self._iFittestGenome 	= i
				
			if CurrPopFitness < LowestSoFar:
				LowestSoFar 		= CurrPopFitness
				self._dWorstFitness = LowestSoFar
		
			self._dTotalFitness += CurrPopFitness
		
		self._dAverageFitness = self._dTotalFitness / self._iPopSize
		
# MineSweeper
class CMinesweeper(object):
	def __init__(self):
		self._dRotation 	= random.random() * TWO_PI
		self._lTrack 		= 0.16
		self._rTrack 		= 0.16
		self._dFitness 		= 0
		self._dScale 		= iSweeperScale
		self._iClosestMine 	= 0
		self._vLookAt 		= SVector2D()
		self._ItsBrain 		= CNeuralNet()
		self._dSpeed 		= 0.0
		
		self._vPosition 	= SVector2D(random.random() * WindowWidth, random.random() * WindowHeight)
		return
	
	def Reset(self):
		self._vPosition 	= SVector2D(random.random() * WindowWidth, random.random() * WindowHeight)
		self._dFitness 		= 0
		self._dRotation		= random.random() * TWO_PI
		return
	
	def GetClosestMine(self, mines):
		closestSoFar 	= 99999.9
		vClosestObj 	= SVector2D(0.0, 0.0)
		
		for idx, mine in enumerate(mines):
			lenToObj 	= Vec2DLength(mine - self._vPosition)
			if lenToObj < ClosestSoFar:
				closestSoFar = lenToObj
				vClosestObj = self._vPosition - mine
				self._iClosestMine = idx
		
		return vClosestObj
		
	def CheckForMine(self, mines, size):
		DistToObj = self._vPosition - mines[self._iClosestMine]
		if Vec2DLength(DistToObj) < (size + 5):
			return self._iClosestMine
		return -1
	
	def Update(self, mines):
		inputs = []
		
		vClosestMine = self.GetClosestMine(mines)
		vClosestMine = Vec2DNormalize(vClosestMine)
		
		inputs.append(vClosestMine._x)
		inputs.append(vClosestMine._y)
		inputs.append(self._vLookAt._x)
		inputs.append(self._vLookAt._y)
		outputs = self._ItsBrain.Update(inputs)		
	
		if len(ouput) < iNumOutputs:
			print "Output size not corrent. Length of output %d, iNumOutputs %d" % (len(output), iNumOutputs)
			return False
		
		self._lTrack = output[0]
		self._rTrack = output[1]
		
		RotForce = self._lTrack - self._rTrack
		
		# Clamp rotation
		if RotForce < -dMaxTurnRate:
			RotForce = -dMaxTurnRate
		else if RotRate > dMaxTurnRate:
			RotForce = dMaxTurnRate
		
		self._dRatation += RotTurnRate
		
		self._dSpeed = self.lTrack + self._rTrack
		self._vLookAt._x = -math.sin(self._dRotation)
		self._vLookAt._y = math.cos(self._dRotation)
		
		self._vPosition = self._vPosition + (self._vLookAt * self._dSpeed)
		
		self._vPosition._x = 0 if self._vPosition._x > WindowWidth else WindowWidth if self._vPosition._x < 0 else self._vPosition._x
		self._vPosition._y = 0 if self._vPosioton._y > WindowHeight else WindowHeight if self._vPosition._y < 0 else self._vPosition._y
		
		return True

if __name__ == "__main__":
	sweeper = [SPoint(-1, -1), SPoint(-1, 1), SPoint(-0.5, 1), SPoint(-0.5, -1), SPoint(0.5, -1), SPoint(1, -1),
				SPoint(1, 1), SPoint(0.5, 1), SPoint(-0.5, -0.5), SPoint(0.5, -0.5), SPoint(-0.5, 0.5), SPoint(-0.25, 0.5),
				SPoint(-0.25, 1.75), SPoint(0.25, 1.75), SPoint(0.25, 0.5), SPoint(0.5, 0.5)]
					
	mine = [SPoint(-1, -1), SPoint(-1, 1), SPoint(1, 1), SPoint(1, -1)]
	
	
