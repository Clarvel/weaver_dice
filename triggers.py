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
        length = len(self.events)

        # if no number specified, choose randomly from available triggers
        if num is None: 
            # determine which trigger indexes are filled
            triggers = []
            for a in range(1, length):
                if self.events[a-1] is not None:
                    triggers.push(a)
            # choose one index randomly
            num = triggers[random.randint(0,len(triggers))]

        # if num is not in the possible indexes, raise error
        if num not in range(1,length):
            raise IndexError('bad event number')
        return "(%d) %s" % (num, self.events[num-1])
