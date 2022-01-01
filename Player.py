class player:
    playMode = False

    def __init__(self, playerName, playerPass):
        self.username = playerName
        self.password = playerPass

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getPlay(self):
        return self.playMode

    def setPlay(self, mode = False):
        self.playMode = mode