class driverregister:
    def __init__(self, DID=None, Name=None, Address=None, Mobile=0, Email=None, AGE=None, Gender=None, Number_Plate= None, Password=None, Status=None):
        # self.Id = None
        self.DID = DID
        self.Name = Name
        self.Address = Address
        self.Mobile = Mobile
        self.Email = Email
        self.AGE = AGE
        self.Gender = Gender
        self.Number_Plate = Number_Plate
        self.Password = Password
        self.Status = Status

    def getDID(self):
        return str(self.DID)

    def getName(self):
        return str(self.Name)

    def getAddress(self):
        return str(self.Address)

    def getMobile(self):
        return str(self.Mobile)

    def getEmail(self):
        return str(self.Email)

    def getAGE(self):
        return str(self.AGE)

    def getGender(self):
        return str(self.Gender)

    def getNumber_Plate(self):
        return str(self.Number_Plate)

    def getPassword(self):
        return str(self.Password)

    def getStatus(self):
        return str(self.Status)


    def setDID(self, DID):
        self.DID = DID

    def setName(self, Name):
        self.Name = Name

    def setAddress(self, Address):
        self.Address = Address

    def setMobile(self, Mobile):
        self.Mobile = Mobile

    def setEmail(self, Email):
        self.Email = Email

    def setAGE(self, AGE):
        self.AGE = AGE

    def setGender(self, Gender):
        self.Gender = Gender

    def setNumber_Plate(self, Number_Plate):
        self.Number_plate = Number_Plate

    def setPassword(self, Password):
        self.Password = Password

    def setStatus(self, Status):
        self.Status = Status




