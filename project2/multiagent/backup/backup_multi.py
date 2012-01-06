from util import manhattanDistance
from game import Directions
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
    print successorGameState
    newPos = successorGameState.getPacmanPosition()
    print newPos # MCGS PRINTS THE POSTION AS A GRID(X,Y)
    oldFood = currentGameState.getFood()
    print oldFood # MCGS PRINTS A SEQENCE OF BOOLEAN FOOD INDICATOR VALUES
    newGhostStates = successorGameState.getGhostStates()
    print newGhostStates # MCGS PRINTS A OBJECT REFERENCE
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    print newScaredTimes # MCGS PRINTS A TUPLE CONTAINING THE TIME LIMIT FOR WHICH THE GHOST WILL REMAIN SCARED.
    "*** YOUR CODE HERE ***"
    print "score is ",successorGameState.getScore()
    return successorGameState.getScore()

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
  treeDepth=0    # GLOBAL STATIC VARIABLE TO KEEP TRACK OF THE TREE DEPTH
  numGAgents=0        # GLOBAL STATIC VARIABLE TO KEEP TRACK OF THE TOTAL NUMBER OF GHOST AGENTS
  finalMoves={}
 
  def Max(self,x,y):        # FUNCTION TO RETURN THE MAX OF TWO NUMBERS
    print "Max comparing x = ",x
    print "with y= ",y
    if(x>y):
     return x
    else:
     return y

 
  def Min(self,x,y):        # FUNCTION TO RETURN THE MIN OF TWO NUMBERS
    print " Min of x ",x
    print " and y ",y
    if(x<y):
      #print "returning x",x
      return x
    else:
      return y


  def MaxValue(self,state,tmpdepth):
    #print " inside the max value function "
    #print state
    #print "depth =",tmpdepth
    v=float('-inf')                  			# ASSIGNING MINUS INFINITY
    pacLegalActions=state.getLegalActions(0)    # GET PACMANS LEGAL ACTIONS
    if Directions.STOP in pacLegalActions: pacLegalActions.remove(Directions.STOP)
    pacSuccessors = [(state.generateSuccessor(0, Paction), Paction) for Paction in pacLegalActions] # PACS SUCC STATES
    print pacSuccessors
    for nextPstate, Paction in pacSuccessors:     # CHECKING ALL THE NEXT GAME STATES
        #print "------------------------>calling min value for ghost 1 for pacman action ",Paction
        tmpV=self.MinValue(nextPstate,1,tmpdepth)
        MinimaxAgent.finalMoves.update({tmpV:(nextPstate,Paction)})
        print " ---------------> MAX : Temp V is ",tmpV
        v=self.Max(v,tmpV)    # CALLING MIN-VALUE
        print "Max v is ",v
        #MinimaxAgent.finalMoves.update({v:(nextPstate,Paction)})
    return v
    util.raiseNotDefined()
   
  def MinValue(self,minState,gIndex,tmpdepth):
    currIndex=gIndex
    print "the gindex is ", gIndex
    print "MinValue depth =",tmpdepth
    v=float('inf')
    if(currIndex<MinimaxAgent.numGAgents):
      gLegalActions=minState.getLegalActions(currIndex)
      gSuccessors = [(minState.generateSuccessor(currIndex, Gaction), Gaction) for Gaction in gLegalActions]
      for nextGstate, Gaction in gSuccessors:
        #print "-------------------------->calling min value for the next ghost for ghost action",Gaction
        #print "-------------------------->calling min value for the next ghost",currIndex+1
        tmpV=self.MinValue(nextGstate,currIndex+1,tmpdepth)
        #MinimaxAgent.finalMoves.update({tmpV:(nextGstate,Gaction)})
        print " -------------------------> Min : Tmp V is ",tmpV
        v=self.Min(v,tmpV)
        print"Min v is",v
    elif(tmpdepth>1):
      tmpdepth=tmpdepth-1
      gLegalActions=minState.getLegalActions(currIndex)
      gSuccessors = [(minState.generateSuccessor(currIndex, Gaction), Gaction) for Gaction in gLegalActions]
      for nextGstate, Gaction in gSuccessors:
        #print "-------------------------->calling max value for the next ghost for ghost action",Gaction
        #print "============================>calling max value for the pacman",currIndex
        tmpV=self.MaxValue(nextGstate,tmpdepth)
        #MinimaxAgent.finalMoves.update({tmpV:(nextGstate,Gaction)})
        print "--------------------------> Tmp V is ",tmpV
        v=self.Min(v,tmpV)
        print"Min v is",v
    if(tmpdepth==1):
      tmp=scoreEvaluationFunction(minState)
      print "------------------------------------------------>Leaf node @ min value function",tmp
      return minState.getScore()
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
    """legal=gameState.getLegalActions(0)        # MCGS FOR TESTING
    treeDepth=self.depth                # CALCULATING THE DEPTH
    ghost=gameState.getNumAgents()-1        # CALCULATING THE NUMBER OF GHOSTS IN THE MAZE   
    print "depth is ...",self.depth
    print gameState
    print " the pacman position now is ",gameState.getPacmanPosition()"""
    MinimaxAgent.numGAgents=gameState.getNumAgents()-1    # STATIC VARIABLES TO TRACK OF THE NUMBER OF GHOST IN THE MAZE
    MinimaxAgent.treeDepth=self.depth
    MinimaxAgent.finalMoves={}
    print " ++++++++++++++++++++++++++++++++GET ACTION+++++++++++++++++++++++++++++++++++++++++++ "
    print " Get Action :the total number of ghost in the maze is ", MinimaxAgent.numGAgents
    print " Get Action :the min max agent is called with the depth of ", MinimaxAgent.treeDepth
    move=self.MaxValue(gameState,MinimaxAgent.treeDepth)
    print "--------->?????????????????????Lets SEEEE",move
    #print MinimaxAgent.finalMoves
    print MinimaxAgent.finalMoves[move]
    print MinimaxAgent.finalMoves[move][1]
    return MinimaxAgent.finalMoves[move][1]
    """print "the total number of agents are .. ",numAgents    # MCGS FOR TESTING    
    if Directions.STOP in legal: legal.remove(Directions.STOP)    # MCGS FOR TESTING
    print " legal actions after removal ", legal        # MCGS FOR TESTING
    gPos=gameState.getGhostPosition(1)
    print " the ghost state is ",gameState.getGhostState(1)
    print " the intial ghost position is ",gPos
    print " the ghost legal moves are ",gameState.getLegalActions(1)
    successors = [(gameState.generateSuccessor(0, action), action) for action in legal]
    for state, action in successors:
        print " the state is ", state
        print " the direction is ", action
        print " the ghost pos in this state is ", state.getGhostPosition(1)
        print " the ghost state is ", gameState.getGhostState(1)
        print " the ghost legal moves are ",gameState.getLegalActions(1)
        print " the pacman position now is ",state.getPacmanPosition()"""

   

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
   
class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """
   
  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
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
