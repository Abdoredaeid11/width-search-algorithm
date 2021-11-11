# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
adj_list={'A':['B','C'],'B':['D','E'],'C':['B','F'],'D':[],'E':['F'],'F':[]}
color={}
parent={}
Ttime={}
dfs_out=[]
for node in adj_list:
    color[node]='W'
    parent[node]=None
    Ttime[node]=[-1,-1]
time=0
def dfs(u):
    global time
    color[u]='G'
    Ttime[u][0]=time
    dfs_out.append(u)
    for v in adj_list[u]:
        if color[v]=='W':
          parent[v]=u
          dfs(v)
    color[u]='B'        
    Ttime[u][1]=time
    time+=1
dfs('A')  
print(color)
print(Ttime)
print(dfs_out)
print()
for node in adj_list.keys():
    print()
    print(node,"===>",Ttime[node])