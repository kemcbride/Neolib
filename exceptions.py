# General
class parseException(Exception):
    pass

class invalidUser(Exception):
    pass
    
class invalidType(Exception):
    pass
    
class invalidMethod(Exception):
    pass
    
    
# HTTP
class HTTPException(Exception):
    pass
    
    
    
# User
class logoutException(Exception):
    pass

class notEnoughBalance(Exception):
    pass
    
class notEnoughNps(Exception):
    pass
    
    
    
# Daily
class dailyAlreadyDone(Exception):
    pass
    
class snowagerAwake(Exception):
    pass
    
class marrowNotAvailable(Exception):
    pass
    
    
    
# Inventory
class emptyInventory(Exception):
    pass
    
    
    
# Shop
class invalidSearch(Exception):
    pass
    
class shopWizBanned(Exception):
    time = ""
    pass

class invalidShop(Exception):
    pass
    
class emptyShop(Exception):
    pass
    
class activeQuest(Exception):
    pass