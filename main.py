class TicTacToe:

    def __init__(self):
        self.gameList = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ]
        self.gameMsg = [
            'Draw',
            'X wins',
            'O wins',
        ]
        self.errMsg = [
            'This cell is occupied! Choose another one!',
            'You should enter numbers!',
            'Coordinates should be from 1 to 3!'
        ]

    def printGameList(self):
        print("---------")
        [print('| ' + ' '.join(row) + ' |') for row in self.gameList]
        print("---------")

    def isXwins(self):
        for row in self.gameList:
            if row.count('X') == 3:
                return True
        for col in zip(*self.gameList):
            if col.count('X') == 3:
                return True
        a = self.gameList[0][0]
        b = self.gameList[1][1]
        c = self.gameList[2][2]
        if a == b and b == c and c == 'X':
            return True
        a = self.gameList[0][2]
        b = self.gameList[1][1]
        c = self.gameList[2][0]
        if a == b and b == c and c == 'X':
            return True
        return False

    def isOwins(self):
        for row in self.gameList:
            if row.count('O') == 3:
                return True
        for col in zip(*self.gameList):
            if col.count('O') == 3:
                return True
        a = self.gameList[0][0]
        b = self.gameList[1][1]
        c = self.gameList[2][2]
        if a == b and b == c and c == 'O':
            return True
        a = self.gameList[0][2]
        b = self.gameList[1][1]
        c = self.gameList[2][0]
        if a == b and b == c and c == 'O':
            return True
        return False

    def isFinished(self):
        if self.gameList[0].count('_') + self.gameList[1].count('_') + self.gameList[2].count('_') > 0:
            return False
        return True

    def inputCoordinates(self, turn):
        coordinates = input("Enter the coordinates:")
        if len(coordinates) == 3 and coordinates[0] in '123' and coordinates[1] == ' ' and coordinates[2] in '123':
            a, b = coordinates.split()
            a, b = int(a), int(b)
            if a < 1 or a > 3 or b < 1 or b > 3:
                print(self.errMsg[2])
                self.inputCoordinates(turn)
            elif self.gameList[b - 1][a - 1] != '_':
                print(self.errMsg[0])
                self.inputCoordinates(turn)
            else:
                self.gameList[b - 1][a - 1] = turn
        else:
            print(self.errMsg[1])
            self.inputCoordinates(turn)

    def start(self):
        self.printGameList()
        turn = 'X'
        while not any([self.isXwins(), self.isOwins(), self.isFinished()]):
            self.gameList.reverse()
            self.inputCoordinates(turn)
            self.gameList.reverse()
            self.printGameList()
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        if self.isXwins():
            print(self.gameMsg[1])
        elif self.isOwins():
            print(self.gameMsg[2])
        else:
            print(self.gameMsg[0])


game = TicTacToe()
game.start()