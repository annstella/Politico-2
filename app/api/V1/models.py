
parties = [] 
class Parties:
    '''
    party class to define party objects
    '''
    def __init__(self, name, hqAddress, logoUrl):
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl

    @classmethod
    def get_all(cls):
        return parties


