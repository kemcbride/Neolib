""":mod:`MarrowGuess` -- Contains the MarrowGuess class

.. module:: MarrowGuess
   :synopsis: Contains the MarrowGuess class
.. moduleauthor:: Joshua Gilman <joshuagilman@gmail.com>
"""

from neolib.daily.Daily import Daily
from neolib.exceptions import dailyAlreadyDone
from neolib.exceptions import parseException
from neolib.exceptions import marrowNotAvailable
import logging
import random

class MarrowGuess(Daily):
    
    """Provides an interface for the Marrow Guess daily
    
    For a more detailed description, please refer to the Daily class.
    """
    
    def play(self, pounds = 0):  
        # If no guess was given, automatically generate one.
        if not pounds:
            # Neopets suggests between 200 - 800 pounds
            pounds = random.randrange(200, 800)
            
        pg = self.player.getPage("http://www.neopets.com/medieval/guessmarrow.phtml")
        
        # Indicates we can't guess yet
        if not "enter your value as an integer" in pg.content:
            raise marrowNotAvailable
            
        form = pg.form(action="process_guessmarrow.phtml")
        pg = form.submit()
        
        if "WRONG!" in pg.content:
            return
            
        # NOTE: This daily is still under development
        # It is not currently known what a winning page looks like, thus it's logged until further development
        logging.getLogger("neolib.daily").info("Possible Marrow Guess winning page", {'pg': pg})
        self.win = True
            
    def getMessage(self):
        if self.win:
            # NOTE: This daily is still under development
            return "You won. Please notify the application developer ASAP."
        else:
            return "You did not guess right!"
