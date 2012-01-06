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
	moves=[] # MOVES LIST THAT WILL BE RETURNED AT THE END OF THIS DFS FUCNTION CALL
	backTrack={} # BACKTRACK DICTIONARY TO HOLD THE PARENT CHILD RELATIONSHIP THAT IS USED TO BACK TRACK
	openStack=util.Stack() 	# OPEN STACK TO PUSH THE CHILDREN
	closedQ=util.Queue()		# CLOSED QUEUE TO MAINTAIN THE CLOSED STATES
	finalMovStack=util.Stack()	# A STACK TO KEEP THE FINAL LIST OF MOVES WHICH A SUBSET OF THE CLOSED QUEUE
	start=problem.getStartState()
	startNode=(start,'None',0)
	if(problem.isGoalState(start)): # CHECKING IF THE START IS THE GOAL STATE
		return # IF YES RETURNING
	startSuccessor=problem.getSuccessors(start) # GETTING THE SUCCESSORS OF START STATE
	for node in startSuccessor:
		parentChild={node:startNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
		openStack.push(node)
		backTrack.update(parentChild)		# UPDATING THE BACK TRACK DICT
	while (not(openStack.isEmpty())):	# WHILE THE STACK IS NOT EMPTY REPEAT THE BELOW CODE SECTION
		currNode=openStack.pop()
		closedQ.push(currNode)
		if (problem.isGoalState(currNode[0])): # CHECKING IF ITS THE GOAL NODE
			goalNode=currNode;		# IF YES SAVING IT IN A VARIABLE
			break
		children=problem.getSuccessors(currNode[0])
		for child in children:
			if(openStack.list.count(child)==0 and closedQ.list.count(child)==0):
				parentchild={child:currNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
				openStack.push(child)		# ADDING THE UNIQUE CHILDRENS TO THE OPEN STACK
				backTrack.update(parentchild) # APPENDING IT TO BACKTRACK LIST
	tempNode=goalNode
	# CODE SEGMENT TO SELECT THE FINAL LIST OF MOVES FROM THE BACK TRACK DICT
	while(not(tempNode==startNode)): 
		finalMovStack.push(tempNode)
		tempNode=backTrack[tempNode]
	while (not(finalMovStack.isEmpty())): # CREATING THE FINAL MOVES LIST
		item=finalMovStack.pop()
		if (item[1]=='West'):
			moves.append(w)
		elif (item[1]=='North'):
			moves.append(n)
		elif (item[1]=='South'):
			moves.append(s)
		elif (item[1]=='East'):
			moves.append(e)
	return moves # RETURNING THE MOVES LIST
	util.raiseNotDefined()

def breadthFirstSearch(problem):
  	"Search the shallowest nodes in the search tree first. [p 74]"
  	"*** YOUR CODE HERE ***"
	print " This is bfs implementation "
	from game import Directions
  	s = Directions.SOUTH # ASSIGNING DIRECTIONS
  	w = Directions.WEST # ASSIGNING DIRECTIONS
	n = Directions.NORTH # ASSIGNING DIRECTIONS
	e = Directions.EAST # ASSIGNING DIRECTIONS
	moves=[] # MOVES LIST THAT WILL BE RETURNED AT THE END OF THIS DFS FUCNTION CALL
	backTrack={} # BACKTRACK DICTIONARY TO HOLD THE PARENT CHILD RELATIONSHIP THAT IS USED TO BACK TRACK
	openQ=util.Queue() 	# OPEN STACK TO PUSH THE CHILDREN
	closedQ=util.Queue()		# CLOSED QUEUE TO MAINTAIN THE CLOSED STATES
	finalMovStack=util.Stack()	# A STACK TO KEEP THE FINAL LIST OF MOVES WHICH A SUBSET OF THE CLOSED QUEUE
	start=problem.getStartState()
	startNode=(start,'None',0)
	if(problem.isGoalState(start)): # CHECKING IF THE START IS THE GOAL STATE
		return # IF YES RETURNING
	startSuccessor=problem.getSuccessors(start) # GETTING THE SUCCESSORS OF START STATE
	for node in startSuccessor:
		parentChild={node:startNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
		openQ.push(node)
		backTrack.update(parentChild)		# UPDATING THE BACK TRACK DICT
	while (not(openQ.isEmpty())):	# WHILE THE STACK IS NOT EMPTY REPEAT THE BELOW CODE SECTION
		currNode=openQ.pop()
		closedQ.push(currNode)
		if (problem.isGoalState(currNode[0])): # CHECKING IF ITS THE GOAL NODE
			goalNode=currNode;		# IF YES SAVING IT IN A VARIABLE
			break
		children=problem.getSuccessors(currNode[0])
		for child in children:
			if(openQ.list.count(child)==0 and closedQ.list.count(child)==0):
				parentchild={child:currNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
				openQ.push(child)		# ADDING THE UNIQUE CHILDRENS TO THE OPEN STACK
				backTrack.update(parentchild) # APPENDING IT TO BACKTRACK LIST
	tempNode=goalNode
	# CODE SEGMENT TO SELECT THE FINAL LIST OF MOVES FROM THE BACK TRACK DICT
	while(not(tempNode==startNode)): 
		finalMovStack.push(tempNode)
		tempNode=backTrack[tempNode]
	while (not(finalMovStack.isEmpty())): # CREATING THE FINAL MOVES LIST
		item=finalMovStack.pop()
		if (item[1]=='West'):
			moves.append(w)
		elif (item[1]=='North'):
			moves.append(n)
		elif (item[1]=='South'):
			moves.append(s)
		elif (item[1]=='East'):
			moves.append(e)
	return moves # RETURNING THE MOVES LIST
  	util.raiseNotDefined()
      
def uniformCostSearch(problem):
  	"Search the node of least total cost first. "
	from game import Directions
  	s = Directions.SOUTH # ASSIGNING DIRECTIONS
  	w = Directions.WEST # ASSIGNING DIRECTIONS
	n = Directions.NORTH # ASSIGNING DIRECTIONS
	e = Directions.EAST # ASSIGNING DIRECTIONS
	moves=[] # MOVES LIST THAT WILL BE RETURNED AT THE END OF THIS DFS FUCNTION CALL
	backTrack={} # BACKTRACK DICTIONARY TO HOLD THE PARENT CHILD RELATIONSHIP THAT IS USED TO BACK TRACK
	openQ=util.PriorityQueue() 	# OPEN STACK TO PUSH THE CHILDREN
	simpleQ=util.Queue()
	closedQ=util.Queue()		# CLOSED QUEUE TO MAINTAIN THE CLOSED STATES
	finalMovStack=util.Stack()	# A STACK TO KEEP THE FINAL LIST OF MOVES WHICH A SUBSET OF THE CLOSED QUEUE
	start=problem.getStartState()
	startNode=(start,'None',0)
	if(problem.isGoalState(start)): # CHECKING IF THE START IS THE GOAL STATE
		return # IF YES RETURNING
	startSuccessor=problem.getSuccessors(start) # GETTING THE SUCCESSORS OF START STATE
	for node in startSuccessor:
		parentChild={node:startNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
		openQ.push(node,node[2])
		simpleQ.push(node)
		backTrack.update(parentChild)		# UPDATING THE BACK TRACK DICT
	while (not(openQ.isEmpty())):	# WHILE THE STACK IS NOT EMPTY REPEAT THE BELOW CODE SECTION
		currNode=openQ.pop()
		closedQ.push(currNode)
		if (problem.isGoalState(currNode[0])): # CHECKING IF ITS THE GOAL NODE
			goalNode=currNode;		# IF YES SAVING IT IN A VARIABLE
			break
		children=problem.getSuccessors(currNode[0])
		for child in children:
			if(simpleQ.list.count(child)==0 and closedQ.list.count(child)==0):
				parentchild={child:currNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
				openQ.push(child,child[2])		# ADDING THE UNIQUE CHILDRENS TO THE OPEN STACK
				simpleQ.push(child)
				backTrack.update(parentchild) # APPENDING IT TO BACKTRACK LIST
	tempNode=goalNode
	# CODE SEGMENT TO SELECT THE FINAL LIST OF MOVES FROM THE BACK TRACK DICT
	while(not(tempNode==startNode)): 
		finalMovStack.push(tempNode)
		tempNode=backTrack[tempNode]
	while (not(finalMovStack.isEmpty())): # CREATING THE FINAL MOVES LIST
		item=finalMovStack.pop()
		if (item[1]=='West'):
			moves.append(w)
		elif (item[1]=='North'):
			moves.append(n)
		elif (item[1]=='South'):
			moves.append(s)
		elif (item[1]=='East'):
			moves.append(e)
	return moves # RETURNING THE MOVES LIST

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
