class TicTacToeGame:
    
    
    def __init__(self):
        print("Enjoy Tic Tac Toe Game ")
        self.list=[[" "," "," "],[" "," "," "],[" "," "," "]]
        self.turn=1
    ListOfInputs=[]
    def grid(self,list):
        
        c=0
        print()
        print()
        for row in self.list:
            print("       |       |       ")
            for i in range(len(row)):
                
                print("   "+row[i]+"   ",end="")
                if i !=2:
                    print('|',end='')
            print()
            c+=1
            if c!=3:
                print("_______|_______|_______")
            else:
                print("       |       |       ")
    def checker(self,list,EnteredEle,indices):
        win=True
        for i in range(3):
            if self.list[indices[0]][i]!=EnteredEle:
                
                win=False
                break
        if win :
            return True
        win=True
        for i in range(3):
            if self.list[i][indices[1]]!=EnteredEle:
                
                win=False
                break
        if win :
            
            return True
        if indices[0]+indices[1]==2 or indices[0]==indices[1]:
            if indices[0]==indices[1]:
                win=True
                for i in range(3):
                    if self.list[i][i]!=EnteredEle:
                        win=False
                if win :
                    return True
            if indices[0]+indices[1]==2:
                win=True
                for i in range(3):
                    if self.list[i][2-i]!=EnteredEle:
                        win=False
                if win :
                    return True
    
    def inpu(self):
        
        if self.turn==1:
            print("\n\nFor X>>>>")
        else:
            print("\n\nFor O>>>>")
        
        r=int(input("enter the row:"))
        c=int(input("enetr the column:"))
        #print(ListOfInputs)
        if (r>=1 and r<=3 and c>=1 and c<=3) and [r-1,c-1] not in self.ListOfInputs:
            
            
            if self.turn==1:
                self.list[r-1][c-1]='X'
            if self.turn==0:
                self.list[r-1][c-1]='O'
           
            self.ListOfInputs.append([r-1,c-1])
            self.grid(self.list)
            if self.turn==1:
                EnteredEle="X"
            else:
                EnteredEle="O"
            
            self.turn=1-self.turn
            return EnteredEle,[r-1,c-1]
        else:
            print("wrong input ........\n Try again")
            return self.inpu()
    def start(obj):
        while True:
            EnteredEle,indices=obj.inpu()
            x=obj.checker(list,EnteredEle,indices)
            #print(x,EnteredEle,indices,list)
            if x:
                print(EnteredEle+"' partipant won .... Gelichavu Babu")
                break
obj=TicTacToeGame()
obj.start()
