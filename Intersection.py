import re
import csv
import pandas as pd
from igraph import *
#import louvain as la
import xlsxwriter
import networkx as nx
import itertools
from igraph.drawing import vertex
from matplotlib import pyplot as plt
from operator import itemgetter
import networkx as nx
import numpy as np
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
dt=0
row = 0
offo=0
column = 0
bas=0
maximum=0
yourlist2=[]
mylist =[]
mylist1=[]
mylist2=[]
yourlist =[]
yourlist1 =[]
Edges=[]
rjj=0
uff=0
temp=0
temp1 =[]
position=0
pos=[]
templist=[]
positionlist=[]
for chalpa in range(9): #make time changes (1 num more)
    mylist.append([])
    mylist1.append([])
    mylist2.append([])
G = Graph(directed = True)
df=pd.read_csv('SUPERUSER A2Q 2.csv')#Edges data
f1 = open("PALS.txt", "a")
f2 = open("SIM.txt", "a")
f3= open("Jaccard.txt", "a")
for k in range(9): #change in time (1 num more)
      #fil2 = open('Jaccah rd.csv', 'a+')
      newdf = df[(df.TIME == k)]
      nodekag =newdf[['SRC']].values.tolist()
      nodekag1 =newdf[['TGT']].values.tolist()
      nodekag2 = nodekag + nodekag1
      nodekag3=np.array(nodekag2)
      nodekag4=np.unique(nodekag3)
      nodekag5=nodekag4.tolist()
      print(G)
      G.add_vertices(nodekag5)
      kaggle = newdf[['SRC', 'TGT']].values.tolist()
      for line in kaggle:
          edge1=G.vs['name'].index(line[0])
          edge2 = G.vs['name'].index(line[1])
          #dest to source not considered
          Edges.append([str(edge1),str(edge2)])
          G.add_edges([(edge1,edge2)])
      total = len(set(newdf.index))
      print('Time'+str(k)+':')
      f1.write('Time'+str(k)+':')
      #partition = la.find_partition(G, la.ModularityVertexPartition)
      partition=G.community_infomap()
      modularity_dict = {}
      for i,c in enumerate(partition):
        for name in c:
            modularity_dict[name] = i
            G.vs['modularity'] = (modularity_dict)
      for i,c in enumerate(partition):
         jac = list(c)
         z=0
         for t in list(c):
            for u in list(c):
                 mytuple = [str(t), str(u)]
                 if mytuple in Edges:
                     z = z + 1
         numerator = z * 2
         rjj = rjj+z
         if (len(c) !=1):
             denominator = len(c) * (len(c)-1)
         if (len(c) == 1): denominator=len(c)
         density = numerator/denominator
         relative=z/len(Edges)
         print(density)
         print(relative)
         mylist[bas].append(density)
         mylist1[bas].append(relative)
         cluster = G.subgraph(c)
         Clustering = cluster.transitivity_undirected(mode='nan')
         mylist2[bas].append(Clustering)
         #if (k==0):

         for it in range(len(c)):
             for v, tar in enumerate(G.vs['name']):
                 if c[it]==v:
                     c[it]=tar
                     break
         yourlist1.append(list(c))
         print('Community ' + str(i) + ':', list(c))
         print(len(c))
         if(k != 0):

          for simmi, items in enumerate(yourlist):
                temp = len(intersection(items, list(c)))
                if (maximum < temp):
                    maximum = temp
                    #position = simmi
                    pos=items.copy()
          f3.write('Time'+str(k)+':\n')
          f3.write(str(pos))
          f3.write('\n')
          f3.write(str(list(c)))
          f3.write('\n')
                #templist.append(temp)
          #if(yourlist1[position]=='k'): yourlist1[position]=list(c)
          #else:
           #   while(dt==0):
            #      templist.remove(maximum)
             #     maximum=max(templist)
              #    pos=pos+1
               #   if (yourlist1[templist.index(maximum)+pos] == 'k'):
                #      yourlist1[templist.index(maximum)+pos] = list(c)
                 #     dt=1
          #pos=0
          #templist.clear()
          maximum = 0

         f1.write('Community'+str(i)+':\n'+str(len(c))+'           \n')
         f1.write(str(list(c)))
         for x in list(c):
         #  f1.write(str(x)+" \n")
           f2.write('Time' + str(k) + ',')
           f2.write(str(x)+", "+str(i)+"\n")
      f1.write('Communities count: '+str(i+1)+'\n')
      output = plot(partition)
      output.save(str(k) + 'graph.png')
      mylist.append([])
      mylist1.append([])
      mylist2.append([])
      bas = bas + 1
      yourlist=yourlist1.copy()

      #yy=len(yourlist1)
     # with fil2:
      #    write0 = csv.writer(fil2)
       #   write0.writerows(yourlist1)
        #  print(str(yourlist1))

      yourlist1.clear()
      #yourlist1=['k']*32
      uff = 0
      print("not in any community")
      print(len(Edges)-rjj)
      rjj=0
      Edges.clear()
      #print(rjj)
      G.clear()
file = open('Density.csv', 'a+')
with file:
          write= csv.writer(file)
          write.writerows(mylist)
file_relative = open('relative.csv', 'a+')
with file_relative:
    write1 = csv.writer(file_relative)
    write1.writerows(mylist1)
file_cluster = open('cluster.csv', 'a+')
with file_cluster:
    write2= csv.writer(file_cluster)
    write2.writerows(mylist2)
f1.close()
f2.close()