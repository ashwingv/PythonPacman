from util import manhattanDistance
from game import Directions
from layout import Layout
import random, util

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """
 
   
  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.
   
    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best
   
    "Add more of your code here if you want to"
   
    return legalMoves[chosenIndex]
 
  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.
   
    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.
   
    The code below extracts some useful information from the state, like the
    remaining food (oldFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.
   
    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    minX=0
    minY=0
    maxY=successorGameState.data.layout.height-1
    maxX=successorGameState.data.layout.width-1
    #print maxX
    #print maxY
    pacPos=successorGameState.getPacmanPosition()
    #print pacPos
    gPos=successorGameState.getGhostPositions()
    #print gPos
    pacX=pacPos[0]
    pacY=pacPos[1]
    food=successorGameState.getFood()
    for ghostPosition in gPos:
      if (ghostPosition[0]==pacX+1 and ghostPosition[1]==pacY):
        return float('-inf')
      elif (ghostPosition[0]==pacX-1 and ghostPosition[1]==pacY):
        return float('-inf')
      elif (ghostPosition[0]==pacX and ghostPosition[1]==pacY+1):
        return float('-inf')
      elif (ghostPosition[0]==pacX and ghostPosition[1]==pacY-1):
        return float('-inf')
      else:
        return successorGameState.getScore()
    if ((food[pacX+1][pacY]==True) and (pacX+1 < maxX)):
      return successorGameState.getScore()
    elif ((food[pacX-1][pacY]==True) and (pacX-1 > minX)) :
      return successorGameState.getScore()
    elif ((food[pacX][pacY+1]==True) and  (pacY+1 < maxY)):
      return successorGameState.getScore()
    elif ((food[pacX][pacY-1]==True) and (pacY-1 > minY)) :
	  return successorGameState.getScore()
    else:
      return float('inf')
    util.raiseNotDefined()
    
    #return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.
   
    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.
   
    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.
   
    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class. 
  """
 
  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """
  """ MinimaxAgent.treeDepth
      MinimaxAgent.numGAgents """
  treeDepth=0    			# GLOBAL STATIC VARIABLE TO KEEP TRACK OF THE TREE DEPTH
  numGAgents=0        		# GLOBAL STATIC VARIABLE TO KEEP TRACK OF THE TOTAL NUMBER OF GHOST AGENTS
  finalMoves={}
 
  def Max(self,x,y):        # FUNCTION TO RETURN THE MAX OF TWO NUMBERS
    #print "Max comparing x = ",x
    #print "with y= ",y
    if(x>y):
     return x
    else:
     return y

 
  def Min(self,x,y):        # FUNCTION TO RETURN THE MIN OF TWO NUMBERS
    #print " Min of x ",x
    #print " and y ",y
    if(x<y):
      #print "returning x",x
      return x
    else:
      return y


  def MaxValue(self,state,tmpdepth):
    #print " inside the max value function "
    #print state
    #print "depth =",tmpdepth
    if(tmpdepth==0):
      #print " leaf node inside maxvalue call returning ",state.getScore()
      return state.getScore()
    v=float('-inf')                  			# ASSIGNING MINUS INFINITY
    pacLegalActions=state.getLegalActions(0)    # GET PACMANS LEGAL ACTIONS
    if Directions.STOP in pacLegalActions: pacLegalActions.remove(Directions.STOP)
    pacSuccessors = [(state.generateSuccessor(0, Paction), Paction) for Paction in pacLegalActions] # PACS SUCC STATES
    #print pacSuccessors
    #if (len(pacSuccessors)==0):
      #print " no successor for pacman so returning get score  "
      #return minState.getScore()
    for nextPstate, Paction in pacSuccessors:     # CHECKING ALL THE NEXT GAME STATES
        #print "------------------------>calling min value for ghost 1 for pacman action ",Paction
        tmpV=self.MinValue(nextPstate,1,tmpdepth)
        #print "Before update ",MinimaxAgent.finalMoves
        #print "tmpv is ",tmpV
        #print "state is ",nextPstate
        #print "Paction is ",Paction
        if(tmpdepth==self.depth):
          MinimaxAgent.finalMoves.update({tmpV:(nextPstate,Paction)})
        #print "After update ",MinimaxAgent.finalMoves
        #print "________________________________________________________________________________________________________________"
        #print " ---------------> MAX : Temp V is ",tmpV
        v=self.Max(v,tmpV)    # CALLING MIN-VALUE
        #print "Max v is ",v
        #MinimaxAgent.finalMoves.update({v:(nextPstate,Paction)})
    return v
    util.raiseNotDefined()
   
  def MinValue(self,minState,gIndex,tmpdepth):
    currIndex=gIndex
    #print "the gindex is ", gIndex
    #print "MinValue depth =",tmpdepth
    if(tmpdepth==0):
      tmp=scoreEvaluationFunction(minState)
      #print "------------------------------------------------>Leaf node @ min value function",tmp
      return minState.getScore()
    v=float('inf')
    if(currIndex<MinimaxAgent.numGAgents):
      gLegalActions=minState.getLegalActions(currIndex)
      gSuccessors = [(minState.generateSuccessor(currIndex, Gaction), Gaction) for Gaction in gLegalActions]
      if (len(gSuccessors)==0):
        #print " no succesor for ghost returnig get score ",currIndex
        return minState.getScore()
      for nextGstate, Gaction in gSuccessors:
        #print "-------------------------->calling min value for the next ghost for ghost action",Gaction
        #print "-------------------------->calling min value for the next ghost",currIndex+1
        tmpV=self.MinValue(nextGstate,currIndex+1,tmpdepth)
        #MinimaxAgent.finalMoves.update({tmpV:(nextGstate,Gaction)})
        #print " -------------------------> Min : Tmp V is ",tmpV
        v=self.Min(v,tmpV)
        #print"Min v is",v
    elif(tmpdepth>0):
      #print " depth is greater than 0 "
      tmpdepth=tmpdepth-1
      gLegalActions=minState.getLegalActions(currIndex)
      gSuccessors = [(minState.generateSuccessor(currIndex, Gaction), Gaction) for Gaction in gLegalActions]
      #print gSuccessors
      if (len(gSuccessors)==0):
        #print " no succesor for ghost returnig get score ",currIndex
        return minState.getScore()
      for nextGstate, Gaction in gSuccessors:
        #print "-------------------------->calling max value for the next ghost for ghost action",Gaction
        #print "============================>calling max value for the pacman",currIndex
        tmpV=self.MaxValue(nextGstate,tmpdepth)
        #MinimaxAgent.finalMoves.update({tmpV:(nextGstate,Gaction)})
        #print "--------------------------> Tmp V is ",tmpV
        v=self.Min(v,tmpV)
        #print"Min v is",v
        #MinimaxAgent.finalMoves.update({v:(nextGstate,Gaction)})
    return v
    util.raiseNotDefined()
     
  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction.
     
      Here are some method calls that might be useful when implementing minimax.
     
      gameState.getLegalActions(agentIndex): 
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1
     
      Directions.STOP:
        The stop direction, which is always legal
     
      gameState.generateSuccessor(agentIndex, action):
      (state.generateSuccessor(0, action), action) 
        Returns the successor game state after an agent takes an action
     
      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    MinimaxAgent.numGAgents=gameState.getNumAgents()-1    # STATIC VARIABLES TO TRACK OF THE NUMBER OF GHOST IN THE MAZE
    MinimaxAgent.treeDepth=self.depth
    MinimaxAgent.finalMoves={}
    #print " ++++++++++++++++++++++++++++++++GET ACTION+++++++++++++++++++++++++++++++++++++++++++ "
    #print " Get Action :the total number of ghost in the maze is ", MinimaxAgent.numGAgents
    #print " Get Action :the min max agent is called with the depth of ", MinimaxAgent.treeDepth
    move=self.MaxValue(gameState,MinimaxAgent.treeDepth)
    #print "--------->?????????????????????Lets SEEEE",move
    #print MinimaxAgent.finalMoves
    #print MinimaxAgent.finalMoves[move]
    #print MinimaxAgent.finalMoves[move][1]
    return MinimaxAgent.finalMoves[move][1]
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
############################################################################################################################### 
 
class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """
  treeDepth=0    	  # GLOBAL STATIC VARIABLE TO KEEP TRACK OF THE TREE DEPTH
  numGAgents=0        # GLOBAL STATIC VARIABLE TO KEEP TRACK OF THE TOTAL NUMBER OF GHOST AGENTS
  finalMoves={}
 
  def Max(self,x,y):        # FUNCTION TO RETURN THE MAX OF TWO NUMBERS
    #print "Max comparing x = ",x
    #print "with y= ",y
    if(x>y):
     return x
    else:
     return y

 
  def Min(self,x,y):        # FUNCTION TO RETURN THE MIN OF TWO NUMBERS
    #print " Min of x ",x
    #print " and y ",y
    if(x<y):
      #print "returning x",x
      return x
    else:
      return y


  def MaxValue(self,state,tmpdepth,alpha,beta):
    #print " inside the max value function "
    #print state
    #print "depth =",tmpdepth
    if(tmpdepth==0):
      #print " leaf node inside maxvalue call returning ",state.getScore()
      return state.getScore()
    v=float('-inf')                  			# ASSIGNING MINUS INFINITY
    pacLegalActions=state.getLegalActions(0)    # GET PACMANS LEGAL ACTIONS
    if Directions.STOP in pacLegalActions: pacLegalActions.remove(Directions.STOP)
    pacSuccessors = [(state.generateSuccessor(0, Paction), Paction) for Paction in pacLegalActions] # PACS SUCC STATES
    #print pacSuccessors
    #if (len(pacSuccessors)==0):
      #print " no successor for pacman so returning get score  "
      #return minState.getScore()
    for nextPstate, Paction in pacSuccessors:     # CHECKING ALL THE NEXT GAME STATES
        #print "------------------------>calling min value for ghost 1 for pacman action ",Paction
        tmpV=self.MinValue(nextPstate,1,tmpdepth,alpha,beta)
        if(tmpdepth==self.depth):
          MinimaxAgent.finalMoves.update({tmpV:(nextPstate,Paction)})
        #print " ---------------> MAX : Temp V is ",tmpV
        v=self.Max(v,tmpV)    # CALLING MIN-VALUE
        #print "Max v is ",v
        if(v>=beta):
          #print "pruning @ MAX value "
          return v
        aplha=self.Max(alpha,v)
        #MinimaxAgent.finalMoves.update({v:(nextPstate,Paction)})
    return v
    util.raiseNotDefined()
   
  def MinValue(self,minState,gIndex,tmpdepth,mAlpha,mBeta):
    currIndex=gIndex
    minAlpha=mAlpha
    minBeta=mBeta
    #print "the gindex is ", gIndex
    #print "MinValue depth =",tmpdepth
    if(tmpdepth==0):
      tmp=scoreEvaluationFunction(minState)
      #print "------------------------------------------------>Leaf node @ min value function",tmp
      return minState.getScore()
    v=float('inf')
    if(currIndex<MinimaxAgent.numGAgents):
      gLegalActions=minState.getLegalActions(currIndex)
      gSuccessors = [(minState.generateSuccessor(currIndex, Gaction), Gaction) for Gaction in gLegalActions]
      if (len(gSuccessors)==0):
        #print " no succesor for ghost returnig get score ",currIndex
        return minState.getScore()
      for nextGstate, Gaction in gSuccessors:
        #print "-------------------------->calling min value for the next ghost for ghost action",Gaction
        #print "-------------------------->calling min value for the next ghost",currIndex+1
        tmpV=self.MinValue(nextGstate,currIndex+1,tmpdepth,minAlpha,minBeta)
        #MinimaxAgent.finalMoves.update({tmpV:(nextGstate,Gaction)})
        #print " -------------------------> Min : Tmp V is ",tmpV
        v=self.Min(v,tmpV)
        if(v<=minAlpha):
          #print "pruning @ MIN value "
          return v
        minBeta=self.Min(minBeta,v)
        #print"Min v is",v
    elif(tmpdepth>0):
      #print " depth is greater than 0 "
      tmpdepth=tmpdepth-1
      gLegalActions=minState.getLegalActions(currIndex)
      gSuccessors = [(minState.generateSuccessor(currIndex, Gaction), Gaction) for Gaction in gLegalActions]
      #print gSuccessors
      if (len(gSuccessors)==0):
        #print " no succesor for ghost returnig get score ",currIndex
        return minState.getScore()
      for nextGstate, Gaction in gSuccessors:
        #print "-------------------------->calling max value for the next ghost for ghost action",Gaction
        #print "============================>calling max value for the pacman",currIndex
        tmpV=self.MaxValue(nextGstate,tmpdepth,mAlpha,mBeta)
        #MinimaxAgent.finalMoves.update({tmpV:(nextGstate,Gaction)})
        #print "--------------------------> Tmp V is ",tmpV
        v=self.Min(v,tmpV)
        if(v<=minAlpha):
          #print "pruning @ MIN value "
          return v
        minBeta=self.Min(minBeta,v)
        #print"Min v is",v
    #MinimaxAgent.finalMoves.update({v:(nextGstate,Gaction)})
    return v
    util.raiseNotDefined()
   
  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
    MinimaxAgent.numGAgents=gameState.getNumAgents()-1    # STATIC VARIABLES TO TRACK OF THE NUMBER OF GHOST IN THE MAZE
    MinimaxAgent.treeDepth=self.depth
    MinimaxAgent.finalMoves={}
    #print " ++++++++++++++++++++++++++++++++GET ACTION+++++++++++++++++++++++++++++++++++++++++++ "
    #print " Get Action :the total number of ghost in the maze is ", MinimaxAgent.numGAgents
    #print " Get Action :the min max agent is called with the depth of ", MinimaxAgent.treeDepth
    move=self.MaxValue(gameState,MinimaxAgent.treeDepth,float('-inf'),float('inf'))
    #print "--------->?????????????????????Lets SEEEE",move
    #print MinimaxAgent.finalMoves
    #print MinimaxAgent.finalMoves[move]
    #print MinimaxAgent.finalMoves[move][1]
    return MinimaxAgent.finalMoves[move][1]
    util.raiseNotDefined()
    

#You can stop here, the following two questions are not released for this session.

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """
   
  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction
     
      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).
   
    DESCRIPTION: <write something here so we know what you did>
  """
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
