import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
import collections


# For every item, create a list of similar items.
# Ex: item = 123, similarList = [11,22,33,44,55]
# This represents the current item as well as the list of items that are similar to it.

# For each item in the similarList, create a node in the graph that contains that item, and
# create an edge from item to similarItem. If the item already exists in the graph,
# only create the edge and not the node.


def createGraph(graph,data):
    print('Creating Graph based on CSV')
    for index,row in data.iterrows():
        graph.add_node(row['ASIN'])
        if row['numsimilar'] > 0:
            similarList = row['similar'].split()
            for item in similarList:
                graph.add_edge(row['ASIN'], item)

def importCSV(fileName):
    print('Importing CSV in DataFrame...')
    return pd.read_csv(fileName, dtype={'numsimilar':int})

def saveGraph(graph, fileName):
    nx.write_gml(graph, fileName)

def importGML(fileName):
    print('Loading Graph...')
    print('This may take a little while')
    graph = nx.read_gml(fileName)
    print('Graph loaded')
    return graph

def computePageRank(graph):
    print('Calculating PageRank for each Node!')
    return nx.pagerank(graph)

def sortPageRank(pagerank):
    result = collections.defaultdict(list)
    for key,value in pagerank.items():
        result[key] = value
    return sorted(result.items(), reverse=False)[:10]

# Start


amazonGraph = nx.DiGraph()
data = pd.DataFrame()

#data = importCSV("amzn.csv")
#createGraph(amazonGraph,data)
#saveGraph(amazonGraph, "test1.gml")

if __name__=='main':
    amazonGraph = importGML('amzn.gml')
    pagerank = computePageRank(amazonGraph)
    sortedPageRank = sortPageRank(pagerank)

    while(True):
        print('\n\n\n')
        print('What kind of query would you like to perform?')
        print('1 - PageRank of an item.')
        print('2 - 10 Most popular items.')
        print('\n')
        userInput = int(input())
        print('\n')
        if userInput == 1:
            print('Enter the ASIN for the Item you are searching for')
            asin = str(input())
            print('pagerank for that value is ' + str(pagerank[asin]))
        elif userInput == 2:
            print('The following are the most popular items')
            print(sortedPageRank)
        else:
            break