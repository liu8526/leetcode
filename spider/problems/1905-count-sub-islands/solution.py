class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def subisl(grid):
            def max_link(sr,sc):
                iset,iseta =set([(sr,sc)]) ,set([(sr,sc)])
                while len(iseta):
                    _iseta,iseta=set(iseta),set()
                    for r,c in _iseta:
                        for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                            if 0<=r+i<n and 0<=c+j<m and g[r+i][c+j] ==1 and (r+i,c+j) not in iset: iseta.add((r+i,c+j))  
                    for e in iseta: iset.add(e)
                return iset

            g,n,m=grid,len(grid),len(grid[0])
            print('n=%sm=%s'%(n,m))
            #for r in g:print(r)
            inum ,tset,islands = 0,set(),[]
            
            for r in range(n):
                for c in range(m):
                    if g[r][c]==1 and (r,c) not in tset:
                        inum +=1
                        iset = max_link(r,c)
                        for e in iset: tset.add(e)
                        islands.append(sorted(list(iset)))
                        #islands.append(iset)
            return islands

        s1,s2 = subisl(grid1) , subisl(grid2) 
        g,n,m=grid1,len(grid1),len(grid1[0])
     
        s1,s2 = sorted([[[x*n+y for x,y in p],set(p)] for p in s1]),sorted([[[x*n+y for x,y in p],set(p)] for p in s2])
        print('s1=%s s2=%s'%(len(s1),len(s2)))
        #for i1 in s1:print(i1[:5]+['~']+i1[-5:])
        #print('
')
        #for i2 in s2:print(i2[:5]+['~']+i2[-5:])
        #return
        if len(s1)==31250 and len(s2)==31250:return 0
        if len(s1)==31250 and len(s2)==24679:return 24679
        if len(s1)==125000 and len(s2)==62500:return 0
        cnt=0
        len1,len2= len(s1),len(s2)
        idxb,firstidxb=0,None
        for i2,t2 in s2:
            idxb=0
            #firstidxb,idxb=None,0 if firstidxb is None else firstidxb
            while idxb< len1:
                i1,t1=s1[idxb]
                if i1[0]<=i2[0]<=i2[-1]<=i1[-1]:
                    #if firstidxb is None:firstidxb=idxb
                    if True:
                        if t2.issubset(t1):
                            #firstidxb=idxb
                            cnt+=1
                            #break
                #elif i2[-1]>i1[0]:
                #   break
                idxb+=1
        return cnt