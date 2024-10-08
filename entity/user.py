class User:
    def __init__(self, userId, username, password, role):
        self.userId = userId
        self.username = username
        self.password = password
        self.role = role
    
    # Getters
    def getUserId(self):
        return self.userId
    
    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def getRole(self):
        return self.role
    
    # Setters
    def setUserId(self, userId):
        self.userId = userId
    
    def setUsername(self, username):
        self.username = username
    
    def setPassword(self, password):
        self.password = password
    
    def setRole(self, role):
        self.role = role