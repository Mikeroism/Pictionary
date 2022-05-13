""" This is for Chat class set up """

class Chat(object):
    def __init__(self,r):
        self.content = []
        self.round= r
    
    def chatUpdater(self,msg):
        self.content.append(msg)

    def chatGetter(self):
        return self.content 
    
    def __len__(self):
        return len(self.content)

    def __str__(self):
        return "".join(self.content)
    
    def __repr__(self):
        return str(self)