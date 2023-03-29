class register:
    def __init__(self,CID=None, Name=None, Address=None, Mobile=0, Email=None, DOB=None, Gender=None, Password=None, Payment=None):
        # self.Id = None
        self.CID = CID
        self.Name = Name
        self.Address = Address
        self.Mobile = Mobile
        self.Email = Email
        self.DOB = DOB
        self.Gender = Gender
        self.Password = Password
        self.Payment = Payment


    def getCID(self):
        return str(self.CID)
    def getName(self):
        return str(self.Name)
    def getAddress(self):
        return str(self.Address) 
    def getMobile(self):
        return str(self.Mobile)
    def getEmail(self):
        return str(self.Email)
    def getDOB(self):
        return str(self.DOB)
    def getGender(self):
        return str(self.Gender)
    def getPassword(self):
        return str(self.Password)
    def getPayment(self):
        return str(self.Payment)


    def setCID(self, CID):
        self.CID = CID
    def setName(self, Name):
        self.Name = Name
    def setAddress(self, Address):
        self.Address = Address
    def setMobile(self, Mobile):
        self.Mobile = Mobile
    def setEmail(self, Email):
        self.Email = Email
    def setDOB(self, DOB):
        self.DOB = DOB
    def setGender(self, Gender):
        self.Gender = Gender
    def setPassword(self, Password):
        self.Password = Password
    
    


