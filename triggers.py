"""
triggers.py - Trigger Event utility for Weaver Dice
Copyright 2014, Gundor Gepein
Licensed under the GPL3.

Weaver Dice copyright 2013-2014, Wildbow
"""

import gspread, random

class TriggerSheet:
    def __init__(self, gclient, title=None, key=None):
        if title:
            self.sheet = gclient.open(title)
        elif key:
            self.sheet = gclient.open_by_key(key)
        self.events = self.worksheet().col_values(1)
    def worksheet(self):
        wks = self.sheet.sheet1
        assert wks.title == "Trigger Events"
        return wks
    def event(self, num=None):
        if not num: num = random.randint(1,len(self.events)+1)
        if num not in range(1,len(self.events)+1):
            raise IndexError('bad event number')
        
        return "(%d) %s" % (num, self.events[num-1])

def claim(self, triggerIndex, sender, character = "", game = ""):
	# character and game are option inputs
	
	triggerSheet = self.sheet.sheet1
	usedSheet = self.sheet.sheet2

	# trust the exception handler if trigger index is out of bounds
	trigger = triggerSheet.col_values(1)[triggerIndex-1]
	writer = triggerSheet.col_values(2)[triggerIndex-1]
	if trigger is None or writer is None:
		raise IndexError('no trigger found at [%s]' % triggerIndex)

	# I have no idea how to add this to the spreadsheet, this is just 
	# for general formatting purposes
	usedSheet.pushRow([game, trigger, writer, character, sender])
	# again, no idea how to do this remove rows
	triggerSheet.popRow(triggerIndex-1)
