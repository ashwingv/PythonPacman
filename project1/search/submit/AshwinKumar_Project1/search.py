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
			if(closedQ.list.count(child)==0 and openStack.list.count(child)==0):
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
	#print moves
	return moves # RETURNING THE MOVES LIST
	util.raiseNotDefined()

def breadthFirstSearch(problem):
  	"Search the shallowest nodes in the search tree first. [p 74]"
  	"*** YOUR CODE HERE ***"
	#print " This is bfs implementation "
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
	distFrmRoot={}
	closedPriority={}
	#priorityDict={}
	start=problem.getStartState()
	startNode=(start,'None',0)
	if(problem.isGoalState(start)): # CHECKING IF THE START IS THE GOAL STATE
		return # IF YES RETURNING
	startSuccessor=problem.getSuccessors(start) # GETTING THE SUCCESSORS OF START STATE
	for node in startSuccessor:
		parentChild={node:startNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
		dist=node[2]
		tmpDict={node:dist}
		distFrmRoot.update(tmpDict)
		openQ.push(node,dist)
		simpleQ.push(node)
		backTrack.update(parentChild)		# UPDATING THE BACK TRACK DICT
	while (not(openQ.isEmpty())):			# WHILE THE STACK IS NOT EMPTY REPEAT THE BELOW CODE SECTION
		(currNode,closedPri)=openQ.pop()
		closedQ.push(currNode)
		closedPriority.update({currNode:closedPri})
		if (problem.isGoalState(currNode[0])): # CHECKING IF ITS THE GOAL NODE
			goalNode=currNode;					# IF YES SAVING IT IN A VARIABLE
			break
		children=problem.getSuccessors(currNode[0])
		for child in children:
			if(closedQ.list.count(child)==0 and simpleQ.list.count(child)==0):
				parentchild={child:currNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
				dist=child[2]+distFrmRoot[currNode]
				tempDict={child:dist}
				distFrmRoot.update(tempDict)
				openQ.push(child,dist)		# ADDING THE UNIQUE CHILDRENS TO THE OPEN STACK
				simpleQ.push(child)
				backTrack.update(parentchild) # APPENDING IT TO BACKTRACK LIST
			elif(simpleQ.list.count(child)>0):
				#  CODE SEGEMENT TO CHECK IF A NODE NEED TO REPLACED OPEN LIST OR NOT
				priority=distFrmRoot[child]
				parentchild={child:currNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
				dist=child[2]+distFrmRoot[currNode]
				if(dist<priority):
					tempDict={child:dist}
					del distFrmRoot[child]
					distFrmRoot.update(tempDict)
					openQ.push(child,dist)		# ADDING THE UNIQUE CHILDRENS TO THE OPEN STACK
					simpleQ.push(child)
					del backTrack[child]
					backTrack.update(parentchild) # APPENDING IT TO BACKTRACK LIST
			elif(closedQ.list.count(child)>0):
				#  CODE SEGEMENT TO CHECK IF A NODE NEED TO REPLACED CLOSED LIST OR NOT
				#print "closed Q changed"
				cp=closedPriority[child]
				priority=distFrmRoot[child]
				parentchild={child:currNode}
				dist=child[2]+distFrmRoot[currNode]
				if(dist<cp):
					del distFrmRoot[child]
					distFrmRoot.update({child:dist})	
					del backTrack[child]
					backTrack.update(parentchild) # APPENDING IT TO BACKTRACK LIST
							
	tempNode=goalNode
	#print "..... back track :",backTrack
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
  	"Search the node that has the lowest combi(currNode,closedPriority)ned cost and heuristic first."
  	"*** YOUR CODE HERE ***"
	from game import Directions
  	s = Directions.SOUTH # ASSIGNING DIRECTIONS
  	w = Directions.WEST # ASSIGNING DIRECTIONS
	n = Directions.NORTH # ASSIGNING DIRECTIONS
	e = Directions.EAST # ASSIGNING DIRECTIONS
	moves=[] # MOVES LIST THAT WILL BE RETURNED AT THE END OF THIS DFS FUCNTION CALL
	backTrack={} # BACKTRACK DICTIONARY TO HOLD THE PARENT CHILD RELATIONSHIP THAT IS USED TO BACK TRACK
	distFrmRoot={} # DISTFROMROOT A DICTIONARY TO KEEP TRACK OF THE LENTH OF NODES FROM THE ROOT
	FnDict={} 
	closedPriority={}
	openQ=util.PriorityQueue() 	# OPEN STACK TO PUSH THE CHILDREN
	simpleQ=util.Queue()		# A SIMPLE QUEUE USED TO DETECT LOOPS
	closedQ=util.Queue()		# CLOSED QUEUE TO MAINTAIN THE CLOSED STATES
	finalMovStack=util.Stack()	# A STACK TO KEEP THE FINAL LIST OF MOVES WHICH A SUBSET OF THE CLOSED QUEUE
	start=problem.getStartState()
	startNode=(start,'None',0)	# CREATING A DUMMY START NODE
	if(problem.isGoalState(start)): # CHECKING IF THE START IS THE GOAL STATE
		return # IF YES RETURNING
	startSuccessor=problem.getSuccessors(start) # GETTING THE SUCCESSORS OF START STATE
	for node in startSuccessor:
		parentChild={node:startNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
		Gn=node[2]							# g(n) DIST FROM ROOT NODE TO REACH CURRENT NODE
		tempDist={node:Gn}
		Hn=heuristic(node[0],problem)		# h(n) a HEURISTIC FUNCTION TO AID GREEDY APPROACH
		Fn=Gn+Hn							# f(n)=g(n)+h(n)  FORMULA FOR HEURISTIC APPROACH
		openQ.push(node,Fn)					# PUSING IN TO THE OPEN LIST WHICH IS A PRIORITY QUEUE
		tempFn={node:Fn}
		simpleQ.push(node)					# PUSHING TO THE SIMPLE QUEUE
		backTrack.update(parentChild)		# UPDATING THE BACK TRACK DICT
		distFrmRoot.update(tempDist)		# UPDATING THE DIST FROM ROOT DICT
		FnDict.update(tempFn)
	while (not(openQ.isEmpty())):		# WHILE THE PRIORITY QUEUE IS NOT EMPTY REPEAT THE BELOW CODE SECTION
		(currNode,closedPri)=openQ.pop()
		closedQ.push(currNode)
		closedPriority.update({currNode:closedPri})
		if (problem.isGoalState(currNode[0])): # CHECKING IF ITS THE GOAL NODE
			goalNode=currNode;		# IF YES SAVING IT IN A VARIABLE
			break
		children=problem.getSuccessors(currNode[0])
		for child in children:
			if(closedQ.list.count(child)==0 and simpleQ.list.count(child)==0):
				#print " if if if"
				parentChild={child:currNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
				#print "parent child is ",parent
				Gn=child[2]+distFrmRoot[currNode]
				tempDist={child:Gn}
				Hn=heuristic(child[0],problem)		# h(n) a HEURISTIC FUNCTION TO AID GREEDY APPROACH
				Fn=Gn+Hn							# f(n)=g(n)+h(n)  FORMULA FOR HEURISTIC APPROACH
				openQ.push(child,Fn)				# PUSING IN TO THE OPEN LIST WHICH IS A PRIORITY QUEUE
				tempFn={child:Fn}
				simpleQ.push(child)					# PUSHING TO THE SIMPLE QUEUE
				backTrack.update(parentChild)		# UPDATING THE BACK TRACK DICT
				#print "backTrack is ",backTrack
				distFrmRoot.update(tempDist)		# UPDATING THE DIST FROM ROOT DICT
				FnDict.update(tempFn)
			elif(simpleQ.list.count(child)>0):
				#  CODE SEGEMENT TO CHECK IF A NODE NEED TO REPLACED OPEN LIST OR NOT
				#print " elif elif elif"
				parentChild={child:currNode} # RECORDING THE PARENT CHILD RELATIONSHIP FOR BACK TRACKING FROM THE GOAL STATE
				#print "parent child is ",parent
				Gn=child[2]+distFrmRoot[currNode]
				tempDist={child:Gn}
				Hn=heuristic(child[0],problem)		# h(n) a HEURISTIC FUNCTION TO AID GREEDY APPROACH
				Fn=Gn+Hn
				oldPriority=FnDict[child]
				if(oldPriority>Fn):
					openQ.push(child,Fn)
					del backTrack[child]
					backTrack.update(parentChild)
					del FnDict[child]
					tempFn={child:Fn}
					FnDict.update(tempFn)
			elif(closedQ.list.count(child)>0):
				#  CODE SEGEMENT TO CHECK IF A NODE NEED TO REPLACED CLOSED LIST OR NOT
				#print "closed Q changed"
				cp=closedPriority[child]
				parentchild={child:currNode}
				Gn=child[2]+distFrmRoot[currNode]
				tempDist={child:Gn}
				Hn=heuristic(child[0],problem)		# h(n) a HEURISTIC FUNCTION TO AID GREEDY APPROACH
				Fn=Gn+Hn
				if(Fn<cp):
					del distFrmRoot[child]
					distFrmRoot.update(tempDist)	
					del backTrack[child]
					backTrack.update(parentchild) # APPENDING IT TO BACKTRACK LIST
						
	tempNode=goalNode
	#print "back track is ",backTrack
	# CODE SEGMENT TO SELECT THE FINAL LIST OF MOVES FROM THE BACK TRACK DICT
	while(not(tempNode==startNode)): 
		finalMovStack.push(tempNode)
		#print "..........", tempNode
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
		
	"""start=problem.getStartState()
	startSuccessor=problem.getSuccessors(start) # GETTING THE SUCCESSORS OF START STATE
	for node in startSuccessor:
		print "manhattan distance = ",heuristic(node[0],problem)
		print " node[0] is ", node[0], start"""

  	util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
