       
 class SS:
    def __init__(self):
        self.item = []
        pass
        
    def inser(self, ind, ele):
        self.item.insert(ind, ele)
        pass
        
    def rm(self, ele):
        self.item.remove(ele)
        pass
    
    def pp(self):
        return print(self.item)
    
    def apnd(self, ele):
        self.item.append(ele)
        pass
    
    def srt(self):
        self.item.sort()
        pass
    
    def opp(self):
        self.item.pop(len(self.item)-1)
        pass
    
    def rvr(self):
        self.item[::-1]
        pass
    
    
    
    
    

if __name__ == '__main__':
    obj = SS()
    N = int(input())
    comm = []
    for i in range(N):
        comm.append(input().split())
        if comm[i][0] == 'insert':
            obj.inser(int(comm[i][1]), int(comm[i][2]))
        elif comm[i][0] == 'remove':
            obj.rm(int(comm[i][1]))
        elif comm[i][0] == 'append':
            obj.apnd(int(comm[i][1]))
        elif comm[i][0] == 'sort':
            obj.srt()
        elif comm[i][0] == 'pop':
            obj.opp()
        elif comm[i][0] == 'reverse':
            obj.rvr()
        else:
            obj.pp()
        
            

        
            
       
