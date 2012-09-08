from neolib.daily.Daily import Daily
from neolib.exceptions import dailyAlreadyDone
from neolib.exceptions import parseException
import logging

class GiantJelly(Daily):
    
    def play(self):
        # Visit daily page
        pg = self.player.getPage("http://www.neopets.com/jelly/jelly.phtml")
        
        # Process daily
        pg = self.player.getPage("http://www.neopets.com/jelly/jelly.phtml", {'type': 'get_jelly'})
        
        # Ensure daily not previously completed
        if pg.content.find("NO!") != -1:
            raise dailyAlreadyDone
        
        # Parse prize
        try:
            parts = pg.getParser().find_all("p")
        
            self.img = parts[2].img['src']
            self.prize = parts[3].b.text
            
            # Show that we won
            self.win = True
        except Exception:
            logging.getLogger("neolib.daily").exception("Could not parse Giant Jelly daily.")
            logging.getLogger("neolib.html").info("Could not parse Giant Jelly daily.", {'pg': pg})
            raise parseException
        
    def getMessage(self):
        if self.win:
            return "You recieved a " + self.prize + "!"
        else:
            return "You did not win anything"