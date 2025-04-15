class Board:
    def __init__(self, board):
        self.bs = board
        self.moves = []
        self.enpassant = ""
        self.whitesturn = True
        self._validcharacters="abcdefgh12345678x+#RNBQK0-="

    def move(self, move):
        # R = rook, N = knight, B = bishop, Q = queen, K = king, P = pawn, + = check, # = checkmate, x = capture, a-h = collums, 1-8 = rows
        # castle short = 0-0, castle long = 0-0-0, promotition = x8=X
        #longest possibilities Qe4xf5+ or exd8=Q+ has 7 characters from which last is check or checkmate
        if self.validate(move):
            self.moves.append(move)
            self.whitesturn = not self.whitesturn
            return True
        return False

    def validate(self, move):
        result=False
        if len(move)>7 or len(move)<2: # too long or too short
            return False
        for i in move:
            if i not in self._validcharacters: # check if all characters are valid
                return False
        #checking comes in a later version
        if move[len(move)-1] == "#" or move[len(move)-1] == "+": # no check mode
            move = move[:-1]
        if move[0] == "R":
            return self.rook(move)
        elif move[0] == "N":
            return self.knight(move)
        elif move[0] == "B":
            return self.bishop(move)
        elif move[0] == "Q":
            return self.queen(move)
        elif move[0] in "K0": # king move (castle)
            return self.king(move)
        elif move[0] in "abcdefgh": #pawn move
            result = self.pawn(move)
        return result

    def rook(self, move):
        pass

    def knight(self, move):
        pass

    def bishop(self, move):
        pass

    def queen(self, move):
        pass

    def king(self, move):
        pass

    def pawn(self, move): #exd8=Q+ what captures where promotition to what check
        returnvalue = False
        startlocatition=""
        piece="P"
        print(piece)
        if move[1]=="x":
            startlocatition=move[0]+move[3]
            move=move[2:]
        elif self.bs[8-int(move[1])][ord(move[0]) - 97] != "": # invalid end locatition
            return False
        if len(move)>2:
            piece = move[3]
            move = move[:-2]
        if self.whitesturn:
            #ord(character) - 97 changes letter to their index on the alphabet
            if startlocatition == "":
                if self.bs[8-int(move[1])+1][ord(move[0]) - 97] == "wP": # normal pawn pushes
                    self.bs[8-int(move[1])+1][ord(move[0]) - 97] = ""
                    self.bs[8-int(move[1])][ord(move[0]) - 97] = "wP"
                    self.enpassant = ""
                    returnvalue = True
                # douple pushes must end on the 4th row, cant go trough stuff, douple pawn push
                elif move[1] == "4" and self.bs[8-int(move[1])+1][ord(move[0]) - 97] == "" and self.bs[8-int(move[1])+2][ord(move[0]) - 97] == "wP":
                    self.enpassant = move[0]+str(int(move[1])+1)
                    self.bs[8-int(move[1])+2][ord(move[0]) - 97] = ""
                    self.bs[8-int(move[1])][ord(move[0]) - 97] = "wP"
                    returnvalue = True
        else:
            if len(move) == 2:
                if self.bs[8-int(move[1])][ord(move[0]) - 97] != "": # invalid end locatition
                    returnvalue = False
                elif self.bs[8-int(move[1])-1][ord(move[0]) - 97] == "bP": # normal pawn pushes
                    self.bs[8-int(move[1])-1][ord(move[0]) - 97] = ""
                    self.bs[8-int(move[1])][ord(move[0]) - 97] = "bP"
                    returnvalue = True
                elif move[1] == "5" and self.bs[8-int(move[1])-1][ord(move[0]) - 97] == "" and self.bs[8-int(move[1])-2][ord(move[0]) - 97] == "bP":
                    self.enpassant = move[0]+str(int(move[1])-1)
                    self.bs[8-int(move[1])-2][ord(move[0]) - 97] = ""
                    self.bs[8-int(move[1])][ord(move[0]) - 97] = "bP"
                    returnvalue = True
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
