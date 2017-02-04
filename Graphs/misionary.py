from Graph import Graph

number = 1

def generateGraph(misionary=3, cannibals=3):
    g = Graph()
    currentVertex = g.addVertex(0)
    currentVertex.setleftBank(3, 3)
    currentVertex.setrightBank(0, 0)
    currentVertex.setBoat(0, 0)
    currentVertex.prboat = (0,0)
    currentVertex.prleft = (3,3)
    generateVertex(currentVertex, g)
    head = currentVertex

    return g, head


def generateVertex(pred, graph):
    global number

    currentLeft = pred.getleftBank()
    currentRight = pred.getrightBank()

    if currentLeft == (0, 0):
        return

    for m in range(currentLeft[0] + 1):
        for c in range(currentLeft[1] + 1):
            if m + c != 2: continue
            elif currentLeft[0] - m < currentLeft[1] - c:
                continue
            elif currentLeft[0] - m == 3 and currentLeft[1] - c == 3:
                continue

            else:
                boat = (m, c)
                left = (currentLeft[0] - m, currentLeft[1] - c)

                for mis in range(boat[0] + 1):
                    for can in range(boat[1] + 1):

                        if sum((boat[0] - mis, boat[1] - can)) != 1:
                            continue
                        elif currentLeft[0] - boat[0] < 0 or currentLeft[1] - boat[1] < 0:
                            continue
                        elif currentRight[0] + mis < currentRight[1] + can:
                            continue

                        boat2 = (mis, can)
                        print(boat2)
                        newV = graph.addVertex(number)
                        number += 1
                        print(left[0] + boat[0] - mis, left[1] + boat[1] - can)
                        newV.setleftBank(left[0] + (boat[0]-mis), left[1] + (boat[1]-can))

                        newV.setrightBank(currentRight[0] + mis, currentRight[1] + can)

                        newV.setBoat(0,0)
                        newV.prboat = boat
                        newV.prleft = left
                        pred.addNeightbor(newV)
                        generateVertex(newV, graph)



graph, root = generateGraph()

graph.getDot()
graph.depthfistSearch(root)
"""digraph {
	0 [label="L: (3, 3)->(0, 0)->|R: (0, 0)"]
		0 -> 1
	1 [label="L: (2, 2)->(1, 1)->|R: (1, 0)"]
		1 -> 2
	2 [label="L: (2, 1)->(0, 2)->|R: (1, 1)"]
		2 -> 3
	3 [label="L: (1, 1)->(1, 1)->|R: (2, 1)"]
		3 -> 4
	4 [label="L: (1, 0)->(0, 2)->|R: (2, 2)"]
		4 -> 5
	5 [label="L: (0, 0)->(1, 1)->|R: (3, 2)"]
}"""