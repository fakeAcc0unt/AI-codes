# min max
import math

#defining the minimax algorithm as a function
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # Checking for leaf nodes
    if curDepth == targetDepth:
        return scores[nodeIndex]
    
    if maxTurn:
        # Maximizer's turn
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        # Minimizer's turn
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))
    
#Main code
scores = list()
for _ in range(int(input("Enter the number of values: "))):
    temp = int(input("Enter value: "))
    scores.append(temp)
treeDepth = math.log(len(scores), 2)
print("The optimal value is: ", end = "")
print(minimax(0, 0, True, scores, int(treeDepth)))
