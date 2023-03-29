class booking:
    def __init__(self, CID=None, Date=None, Time=None, Pick_Up=None, Destination=None, Status=None, BID=None):
        self.CID = CID
        self.Date = Date
        self.Time = Time
        self.Pick_Up = Pick_Up
        self.Destination = Destination
        self.Status = Status
        self.BID = BID


    def getCID(self):
        return str(self.CID)
    def getDate(self):
        return str(self.Date)

    def getTime(self):
        return str(self.Time)

    def getPick_Up(self):
        return str(self.Pick_Up)

    def getDestination(self):
        return str(self.Destination)

    def getStatus(self):
        return str(self.Status)

    def getBID(self):
       return  str(self.BID)



    def setCID(self, CID):
        self.CID = CID
    def setDate(self, Date):
        self.Date = Date

    def setTime(self, Time):
        self.Time = Time

    def setPick_Up(self, Pick_Up):
        self.Pick_Up = Pick_Up

    def setDestination(self, Destination):
        self.Destination= Destination

    def setStatus(self, Status):
        self.Status = Status

    def setBID(self, BID):
        self.BID = BID





