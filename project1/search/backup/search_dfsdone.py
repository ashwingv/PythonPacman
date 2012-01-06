"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  #print '\n ********************* ' # MCGS NOT SURE 
  print "********************** problem :", problem # MCGS NOT SURE
  print "********************** Start:", problem.getStartState() # MCGS NOT SURE
  print " ********************** Is the start a goal?", problem.isGoalState(problem.getStartState()) # MCGS NOT SURE
  print " ********************** Start's successors:", problem.getSuccessors(problem.getStartState()) # MCGS NOT SURE
  return  [s,s,w,s,w,w,s,w]
  #return  [s,s,w,s,w,w,w,s] # MCGS WRONG DONE FOR TESTING

def depthFirstSearch(problem):
	"""
  	Search the deepest nodes in the search tree first [p 74].
  
 	 Your search algorithm needs to return a list of actions that reaches
  	the goal.  Make sure to implement a graph search algorithm [Fig. 3.18].
  
 	 To get started, you might want to try some of these simple commands to
  	understand the search problem that is being passed in:
  
  	print "Start:", problem.getStartState()
  	print "Is the start a goal?", problem.isGoalState(problem.getStartState())
 	 print "Start's successors:", problem.getSuccessors(problem.getStartState())
  	"""
  	"*** YOUR CODE HERE ***" 
	from game import Directions
  	s = Directions.SOUTH # ASSIGNING DIRECTIONS
  	w = Directions.WEST # ASSIGNING DIRECTIONS
	n = Directions.NORTH # ASSIGNING DIRECTIONS
	e = Directions.EAST # ASSIGNING DIRECTIONS
	#print "Start:", problem.getStartState()
	#print "Is the start a goal?", problem.isGoalState(problem.getStartState())
	#print "Start's successors:", problem.getSuccessors(problem.getStartState())
	moves=[]
	backTrack={}
	openStack=util.Stack() 	# CREATING A STACK TO PUSH THE CHILDREN
	closedQ=util.Queue()		# CREATING A QUEUE TO MAINTAIN THE CLOSED STATES
	finalMovStack=util.Stack()
	start=problem.getStartState()
	startNode=(start,'None',0)
	if(problem.isGoalState(start)): # CHECKING IF THE START IS THE GOAL STATE
		#print "!!!!!!start state is the goal state!!!!!!"
		return # IF YES RETURNING
	startSuccessor=problem.getSuccessors(start) # GETTING THE SUCCESSORS OF START STATE
	for node in startSuccessor:
		#print "the node is ",node
		#parentChild={startNode:node} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
		parentChild={node:startNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
		openStack.push(node)
		backTrack.update(parentChild)		# APPENDING IT TO BACKTRACK LIST
		#print " the back track now is ",backTrack
	while (not(openStack.isEmpty())):	# WHILE THE STACK IS NOT EMPTY REPEAT THE BELOW CODE SECTION
		currNode=openStack.pop()
		closedQ.push(currNode)
		#print "the current child is ",currNode
		#print "the current node is ", currNode[0]		
		if (problem.isGoalState(currNode[0])):
			goalNode=currNode;
			#print "Yeah!!!!! Yeah!!!! Yeah!!! goal reached"
			#print " the path is ",closedQ.items()
			break
		children=problem.getSuccessors(currNode[0])
		for child in children:
			#print "The child now is ",child
			if(openStack.list.count(child)==0 and closedQ.list.count(child)==0):
				#print "pusing it into stack"
				#parentchild={currNode:child} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
				parentchild={child:currNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
				openStack.push(child)
				backTrack.update(parentchild) # APPENDING IT TO BACKTRACK LIST
				#print " the back track now is ",backTrack
			else:
				print "pushing not needed"
	# BACK TRACKING CODE SEGMENT
	tempNode=goalNode
	while(not(tempNode==startNode)):
		print " Final node now is ", tempNode
		finalMovStack.push(tempNode)
		tempNode=backTrack[tempNode];
###############################################
	while (not(finalMovStack.isEmpty())):
		item=finalMovStack.pop()
		if (item[1]=='West'):
			moves.append(w)
		elif (item[1]=='North'):
			moves.append(n)
		elif (item[1]=='South'):
			moves.append(s)
		elif (item[1]=='East'):
			moves.append(e)
		else:
			print "none"
	return moves
	util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 74]"
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
