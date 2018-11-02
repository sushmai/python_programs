"""
Wardrobe
Arributes - name, clean

methods - getName()
        - isClean()

"""

class Clothing(object):
    def __init__(self, name, clean = True, times_worn = 0, max_wears = 1):
        self.name = name
        self.clean = clean
        self.times_worn = times_worn
        self.max_wears = max_wears 

            
    def getName(self):
        return self.name
    
    def isClean(self):
        return self.clean

    def wear(self):
        self.times_worn += 1
        if self.times_worn >= self.max_wears:
            self.clean = False
    def wash(self):
        self.clean = True
        self.times_worn = 0 
        
    
    def __str__(self):
        return "Clothing[name = " + self.name + \
               ", clean = " + str(self.clean) + \
               ", times_worn = " + str(self.times_worn) + \
               ",max_wears = " + str(self.max_wears) + \
               "]"
class Shirt(Clothing):
    def __init__(self, name, clean = True, times_worn = 0, max_wears = 1, shortsleeves = True):
        super().__init__(name,clean,times_worn, max_wears)
        self.shortsleeves = shortsleeves

    def hasShortSleeves(self):
        return self.shortsleeves
    def __str__(self):
        return "Shirt[" +super().__str__() + \
               ",shortsleeves= " + str(self.shortsleeves) + "]"
    


def main():
    """
    myJeans = Clothing("blue jeans", False)
    myJeans.wear()
    print(myJeans)
    myJeans.wash()
    print(myJeans)
    myShorts = Clothing("shorts")
    print(myJeans.getName())
    print(myShorts.isClean())
    """
    myclothes = []
    myclothes.append(Clothing("blue jeans", False))
    myclothes.append(Clothing("baseball cap", True, 20, 1000))
    myclothes.append(Clothing("jacket", True, 20, 100))
    myclothes.append(Shirt("t-shirt", True, 0,1,True))
    myclothes.append(Shirt("formal shirt", True, 0, 1, False))

    print("\n ***** Full Wardrobe *****")
    for i in range(len(myclothes)):
        print(myclothes[i])

    print("\n *****Clean Clothes*****")
    for i in range(len(myclothes)):
        if myclothes[i].isClean():
            print(myclothes[i])

    print("\n ********Dirty Clothes******")
    for i in range(len(myclothes)):
        if not myclothes[i].isClean():
            print(myclothes[i])

    print(" *******\n Shirts******")
    for i in range(len(myclothes)):
        if isinstance(myclothes[i], Shirt):
            print(myclothes[i])





if __name__ == "__main__":
    main()
      
