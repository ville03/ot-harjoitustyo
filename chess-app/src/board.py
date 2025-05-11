class Board:
    def __init__(self, board):
        self.bs = board
        self.moves = []
        self.enpassant = ""
        self.whitesturn = True
        self.castlerights = ["ws", "wl", "bs", "bl"]
        self._validcharacters="abcdefgh12345678x+#RNBQK0-="

    def move(self, move):
        # R = rook, N = knight, B = bishop, Q = queen, K = king, P = pawn, + = check, # = checkmate, x = capture, a-h = collums, 1-8 = rows
        # castle short = 0-0, castle long = 0-0-0, promotition = x8=X
        #longest possibilities Qe4xf5+ or exd8=Q+ has 7 characters from which last is check or checkmate
        try:
            if self.validate(move):
                self.moves.append(move)
                self.whitesturn = not self.whitesturn
                return True
            return False
        except IndexError:
            return False

    def validate(self, move):
        result=False
        if len(move)>7 or len(move)<2: # too long or too short
            return False
        for i in move:
            if i not in self._validcharacters: # check if all characters are valid
                return False
        #checking comes in a later version
        if move[len(move)-1] in "#+": # no check mode
            move = move[:-1]
        if move[0] == "R":
            return self.rook(move)
        if move[0] == "N":
            return self.knight(move)
        if move[0] == "B":
            return self.bishop(move)
        if move[0] == "Q":
            return self.queen(move)
        if move[0] in "K0": # king move (or castle)
            return self.king(move)
        if move[0] in "abcdefgh": #pawn move
            result = self.pawn(move)
        return result

    def rook(self, move):#Rexd4 tai R4xd4 tai Rxd4 tai R4d4 tai Red4 tai Rd4
        endlocation=move[-2:]
        move = move[1:-2]
        if self.whitesturn:
            if move[-1:] == "x":
                if self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97][0] != "b":
                    return False
                move=move[:-1]
            elif self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] != "":
                return False
            row = int(endlocation[1])+1
            colum = ord(endlocation[0])-97
            if move in "12345678":#e4
                while row <=8:
                    if self.bs[8-row][colum] == "wR":
                        self.bs[8-row][colum] =""
                        self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wR"
                        self.enpassant = ""
                        return True
                    if self.bs[8-row][colum] != "":
                        break
                    row+=1
                row = int(endlocation[1])-1
                while row >0:
                    if self.bs[8-row][colum] == "wR":
                        self.bs[8-row][colum] =""
                        self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wR"
                        self.enpassant = ""
                        return True
                    if self.bs[8-row][colum] != "":
                        break
                    row-=1
            row = int(endlocation[1])
            colum = ord(endlocation[0])-97+1
            while colum <8:
                if self.bs[8-row][colum] == "wR":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wR"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                colum+=1
            colum = ord(endlocation[0])-97-1
            while colum >=0:
                if self.bs[8-row][colum] == "wR":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wR"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                colum-=1
            colum = ord(endlocation[0])-97
            row = int(endlocation[1])+1
            while row <=8:
                if self.bs[8-row][colum] == "wR":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wR"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                row+=1
            row = int(endlocation[1])-1
            while row >0:
                if self.bs[8-row][colum] == "wR":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wR"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                row-=1
        else:
            if move[-1:] == "x":
                if self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97][0] != "w":
                    return False
                move=move[:-1]
            elif self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] != "":
                return False
            row = int(endlocation[1])+1
            colum = ord(endlocation[0])-97
            if move in "12345678":#e4
                while row <=8:
                    if self.bs[8-row][colum] == "bR":
                        self.bs[8-row][colum] =""
                        self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bR"
                        self.enpassant = ""
                        return True
                    if self.bs[8-row][colum] != "":
                        break
                    row+=1
                row = int(endlocation[1])-1
                while row >0:
                    if self.bs[8-row][colum] == "bR":
                        self.bs[8-row][colum] =""
                        self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bR"
                        self.enpassant = ""
                        return True
                    if self.bs[8-row][colum] != "":
                        break
                    row-=1
            row = int(endlocation[1])
            colum = ord(endlocation[0])-97+1
            while colum <8:
                if self.bs[8-row][colum] == "bR":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bR"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                colum+=1
            colum = ord(endlocation[0])-97-1
            while colum >=0:
                if self.bs[8-row][colum] == "bR":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bR"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                colum-=1
            colum = int(endlocation[1])
            row = int(endlocation[1])+1
            while row <=8:
                if self.bs[8-row][colum] == "bR":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bR"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                row+=1
            row = int(endlocation[1])-1
            while row >0:
                if self.bs[8-row][colum] == "bR":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bR"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                row-=1


    def knight(self, move):
        move = move[1:]
        endlocation=move[-2:]
        if self.whitesturn:
            is_queen=False
            i=0
            for row in self.bs:
                j=0
                for tile in row:
                    if tile == "wK":
                        is_queen=True
                        self.bs[i][j]=""
                        break
                    j+=1
                i+=1
                if is_queen:
                    break
            if is_queen:
                self.bs[8-int(endlocation[1])][ord(endlocation[0])-97]="wK"
                return True
            return False
        else:
            is_queen=False
            i=0
            for row in self.bs:
                j=0
                for tile in row:
                    if tile == "bK":
                        is_queen=True
                        self.bs[i][j]=""
                        break
                    j+=1
                if is_queen:
                    break
                i+=1
            if is_queen:
                self.bs[8-int(endlocation[1])][ord(endlocation[0])-97]="bK"
                return True
            return False

    def bishop(self, move):
        endlocation=move[-2:]
        move = move[1:-2]
        if self.whitesturn:
            if move[-1:] == "x":
                if self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97][0] != "b":
                    return False
                move=move[:-1]#only disambiguation left
            elif self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] != "":
                return False
            row = int(endlocation[1])+1
            colum = ord(endlocation[0])-97+1
            while row <= 8 and colum < 8:
                if self.bs[8-row][colum] == "wB":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wB"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                row+=1
                colum+=1
            row = int(endlocation[1])+1
            colum = ord(endlocation[0])-97-1
            while row <= 8 and colum >= 0:
                if self.bs[8-row][colum] == "wB":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wB"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                row+=1
                colum-=1
            row = int(endlocation[1])-1
            colum = ord(endlocation[0])-97+1
            while row > 0 and colum < 8:
                if self.bs[8-row][colum] == "wB":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wB"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                row-=1
                colum+=1
            colum = ord(endlocation[0])-97-1
            row = int(endlocation[1])-1
            while row > 0 and colum >= 0:
                if self.bs[8-row][colum] == "wB":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wB"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                row-=1
                colum-=1
        else:
            if move[-1:] == "x":
                if self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97][0] != "w":
                    return False
                move=move[:-1]#only disambiguation left
            elif self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] != "":
                return False
            row = int(endlocation[1])+1
            colum = ord(endlocation[0])-97+1
            while row <= 8 and colum < 8:
                if self.bs[8-row][colum] == "bB":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bB"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                row+=1
                colum+=1
            row = int(endlocation[1])+1
            colum = ord(endlocation[0])-97-1
            while row <= 8 and colum >= 0:
                if self.bs[8-row][colum] == "bB":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bB"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                row+=1
                colum-=1
            row = int(endlocation[1])-1
            colum = ord(endlocation[0])-97+1
            while row > 0 and colum < 8:
                if self.bs[8-row][colum] == "bB":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bB"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                row-=1
                colum+=1
            colum = ord(endlocation[0])-97-1
            row = int(endlocation[1])-1
            while row > 0 and colum >= 0:
                if self.bs[8-row][colum] == "bB":
                    self.bs[8-row][colum] =""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bB"
                    self.enpassant = ""
                    return True
                if self.bs[8-row][colum] != "":
                    break
                row-=1
                colum-=1

    def queen(self, move):
        move = move[1:]
        endlocation=move[-2:]
        if self.whitesturn:
            is_queen=False
            i=0
            for row in self.bs:
                j=0
                for tile in row:
                    if tile == "wQ":
                        is_queen=True
                        self.bs[i][j]=""
                        break
                    j+=1
                i+=1
                if is_queen:
                    break
            if is_queen:
                self.bs[8-int(endlocation[1])][ord(endlocation[0])-97]="wQ"
                return True
            return False
        else:
            is_queen=False
            i=0
            for row in self.bs:
                j=0
                for tile in row:
                    if tile == "bQ":
                        is_queen=True
                        self.bs[i][j]=""
                        break
                    j+=1
                i+=1
                if is_queen:
                    break
            if is_queen:
                self.bs[8-int(endlocation[1])][ord(endlocation[0])-97]="bQ"
                return True
            return False

    def king(self, move):
        if self.whitesturn:
            castlerights=self.castlerights
            cr=""
            if "bs" in self.castlerights:
                cr=cr+"bs"
            if "bl" in self.castlerights:
                cr=cr+"bl"
            self.castlerights=cr
            if move == "0-0" and "ws" in castlerights:#short castle
                if self.bs[7][4]=="wK" and self.bs[7][5]=="" and self.bs[7][6]=="" and self.bs[7][7]=="wR":
                    self.bs[7][4]=""
                    self.bs[7][5]="wR"
                    self.bs[7][6]="wK"
                    self.bs[7][7]=""
                    return True
            elif move == "0-0-0" and "wl" in castlerights:#long castle
                if self.bs[7][4]=="wK" and self.bs[7][3]=="" and self.bs[7][2]=="" and self.bs[7][1]=="" and self.bs[7][0]=="wR":
                    self.bs[7][4]=""
                    self.bs[7][3]="wR"
                    self.bs[7][2]="wK"
                    self.bs[7][0]=""
                    return True
            else:
                endlocation=move[-2:]
                if move[1] == "x":
                    if self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97][0] != "b":
                        self.castlerights=castlerights
                        return False
                elif self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] != "":
                    self.castlerights=castlerights
                    return False
                
                if self.bs[8-int(endlocation[1])-1][ord(endlocation[0]) - 97] == "wK":
                    self.bs[8-int(endlocation[1])-1][ord(endlocation[0]) - 97] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wK"
                    return True
                if self.bs[8-int(endlocation[1])-1][ord(endlocation[0]) - 97-1] == "wK":
                    self.bs[8-int(endlocation[1])-1][ord(endlocation[0]) - 97-1] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wK"
                    return True
                if self.bs[8-int(endlocation[1])-1][ord(endlocation[0]) - 97+1] == "wK":
                    self.bs[8-int(endlocation[1])-1][ord(endlocation[0]) - 97+1] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wK"
                    return True
                if self.bs[8-int(endlocation[1])+1][ord(endlocation[0]) - 97] == "wK":
                    self.bs[8-int(endlocation[1])+1][ord(endlocation[0]) - 97] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wK"
                    return True
                if self.bs[8-int(endlocation[1])+1][ord(endlocation[0]) - 97-1] == "wK":
                    self.bs[8-int(endlocation[1])+1][ord(endlocation[0]) - 97-1] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wK"
                    return True
                if self.bs[8-int(endlocation[1])+1][ord(endlocation[0]) - 97+1] == "wK":
                    self.bs[8-int(endlocation[1])+1][ord(endlocation[0]) - 97+1] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wK"
                    return True
                if self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97-1] == "wK":
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97-1] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wK"
                    return True
                if self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97+1] == "wK":
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97+1] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "wK"
                    return True
                self.castlerights=castlerights
                return False
        else:
            castlerights=self.castlerights
            cr=""
            if "ws" in self.castlerights:
                cr=cr+"ws"
            if "wl" in self.castlerights:
                cr=cr+"wl"
            self.castlerights=cr
            if move == "0-0" and "bs" in castlerights:#short castle
                if self.bs[0][4]=="bK" and self.bs[0][5]=="" and self.bs[0][6]=="" and self.bs[0][7]=="bR":
                    self.bs[0][4]=""
                    self.bs[0][5]="bR"
                    self.bs[0][6]="bK"
                    self.bs[0][7]=""
                    return True
            elif move == "0-0-0" and "bl" in castlerights:#long castle
                if self.bs[0][4]=="bK" and self.bs[0][3]=="" and self.bs[0][2]=="" and self.bs[0][1]=="" and self.bs[0][0]=="bR":
                    self.bs[0][4]=""
                    self.bs[0][3]="bR"
                    self.bs[0][2]="bK"
                    self.bs[0][0]=""
                    return True
            else:
                endlocation=move[-2:]
                if move[1] == "x":
                    if self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97][0] != "w":
                        self.castlerights=castlerights
                        return False
                elif self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] != "":
                    self.castlerights=castlerights
                    return False
                
                if self.bs[8-int(endlocation[1])-1][ord(endlocation[0]) - 97] == "bK":
                    self.bs[8-int(endlocation[1])-1][ord(endlocation[0]) - 97] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bK"
                    return True
                if self.bs[8-int(endlocation[1])-1][ord(endlocation[0]) - 97-1] == "bK":
                    self.bs[8-int(endlocation[1])-1][ord(endlocation[0]) - 97-1] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bK"
                    return True
                if self.bs[8-int(endlocation[1])-1][ord(endlocation[0]) - 97+1] == "bK":
                    self.bs[8-int(endlocation[1])-1][ord(endlocation[0]) - 97+1] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bK"
                    return True
                if self.bs[8-int(endlocation[1])+1][ord(endlocation[0]) - 97] == "bK":
                    self.bs[8-int(endlocation[1])+1][ord(endlocation[0]) - 97] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bK"
                    return True
                if self.bs[8-int(endlocation[1])+1][ord(endlocation[0]) - 97-1] == "bK":
                    self.bs[8-int(endlocation[1])+1][ord(endlocation[0]) - 97-1] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bK"
                    return True
                if self.bs[8-int(endlocation[1])+1][ord(endlocation[0]) - 97+1] == "bK":
                    self.bs[8-int(endlocation[1])+1][ord(endlocation[0]) - 97+1] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bK"
                    return True
                if self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97-1] == "bK":
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97-1] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bK"
                    return True
                if self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97+1] == "bK":
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97+1] = ""
                    self.bs[8-int(endlocation[1])][ord(endlocation[0]) - 97] = "bK"
                    return True
                self.castlerights=castlerights
                return False

    def pawn(self, move): #exd8=Q+ what captures where promotition to what check
        enpassant = self.enpassant
        self.enpassant = ""
        returnvalue = False
        startlocatition=""
        piece="P"
        if move[1]=="x":
            startlocatition=move[0]+str(int(move[3]))
            move=move[2:]
        elif self.bs[8-int(move[1])][ord(move[0]) - 97] != "": # invalid end locatition
            return False
        if len(move)>2 and move[1] in "80":
            piece = move[3]
            move = move[:-2]
        if self.whitesturn:
            #ord(character) - 97 changes letter to their index on the alphabet
            if startlocatition == "":
                if self.bs[8-int(move[1])+1][ord(move[0]) - 97] == "wP": # normal pawn pushes
                    self.bs[8-int(move[1])+1][ord(move[0]) - 97] = ""
                    self.bs[8-int(move[1])][ord(move[0]) - 97] = "w"+piece
                    returnvalue = True
                # douple pushes must end on the 4th row, cant go trough stuff, douple pawn push
                elif move[1] == "4" and self.bs[8-int(move[1])+1][ord(move[0]) - 97] == "" and self.bs[8-int(move[1])+2][ord(move[0]) - 97] == "wP":
                    self.enpassant = move[0]+str(int(move[1])-1)
                    self.bs[8-int(move[1])+2][ord(move[0]) - 97] = ""
                    self.bs[8-int(move[1])][ord(move[0]) - 97] = "w"+piece
                    returnvalue = True
            elif move == enpassant:
                self.bs[8-int(move[1])][ord(move[0]) - 97] = "w"+piece
                self.bs[8-int(startlocatition[1])+1][ord(startlocatition[0]) - 97] = ""
                self.bs[8-int(move[1])+1][ord(move[0]) - 97] = ""
                returnvalue = True
            elif self.bs[8-int(startlocatition[1])+1][ord(startlocatition[0]) - 97] == "wP": # capture
                if self.bs[8-int(move[1])][ord(move[0]) - 97][0] == "b":
                    self.bs[8-int(move[1])][ord(move[0]) - 97] = "w"+piece
                    self.bs[8-int(startlocatition[1])+1][ord(startlocatition[0]) - 97] = ""
                    returnvalue = True
        else:
            if startlocatition == "":
                if self.bs[8-int(move[1])-1][ord(move[0]) - 97] == "bP": # normal pawn pushes
                    self.bs[8-int(move[1])-1][ord(move[0]) - 97] = ""
                    self.bs[8-int(move[1])][ord(move[0]) - 97] = "b"+piece
                    returnvalue = True
                # douple pushes must end on the 4th row, cant go trough stuff, douple pawn push
                elif move[1] == "5" and self.bs[8-int(move[1])-1][ord(move[0]) - 97] == "" and self.bs[8-int(move[1])-2][ord(move[0]) - 97] == "bP":
                    self.enpassant = move[0]+str(int(move[1])+1)
                    self.bs[8-int(move[1])-2][ord(move[0]) - 97] = ""
                    self.bs[8-int(move[1])][ord(move[0]) - 97] = "b"+piece
                    returnvalue = True
            elif move == enpassant:
                self.bs[8-int(move[1])][ord(move[0]) - 97] = "b"+piece
                self.bs[8-int(startlocatition[1])-1][ord(startlocatition[0]) - 97] = ""
                self.bs[8-int(move[1])-1][ord(move[0]) - 97] = ""
                returnvalue = True
            elif self.bs[8-int(startlocatition[1])-1][ord(startlocatition[0]) - 97] == "bP": # capture
                if self.bs[8-int(move[1])][ord(move[0]) - 97][0] == "w":
                    self.bs[8-int(move[1])][ord(move[0]) - 97] = "b"+piece
                    self.bs[8-int(startlocatition[1])-1][ord(startlocatition[0]) - 97] = ""
                    returnvalue = True
        if not returnvalue:
            self.enpassant = enpassant
        return returnvalue
        #self.bs=[["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        #         ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
        #         ["", "", "", "", "", "", "", ""],
        #         ["", "", "", "", "", "", "", ""],
        #         ["", "", "", "", "", "", "", ""],
        #         ["", "", "", "", "", "", "", ""],
        #         ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
        #         ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        #         ]

    def board(self):
        return self.bs
