class Classy(object):
    def __init__(self):
        self.items = []
    def addItem(self, item):
        self.items.append(item)
    def getClassiness(self):
        totalClassiness = 0
        classyDict = {"tophat":2,"bowtie":4,"monocle":5}
        for item in self.items:
            try:
                totalClassiness += classyDict[item]
            except KeyError:
                pass
        return totalClassiness  
