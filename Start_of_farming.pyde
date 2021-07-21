class Residence():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = 'hunting'
        self.stress = 0
        
    def display(self):
        if self.status == 'hunting':
            shapeMode(CENTER)
            fill(0, 255, 0)
            triangle(self.x, self.y - 3, self.x - 3, self.y + 3, self.x + 3, self.y + 3)
            ellipseMode(CENTER)
            noFill()
            ellipse(self.x, self.y, 30, 30)
            
        elif self.status == 'farming':
            shapeMode(CENTER)
            fill(255, 0, 0)
            triangle(self.x, self.y - 3, self.x - 3, self.y + 3, self.x + 3, self.y + 3)
            ellipseMode(CENTER)
            noFill()
            ellipse(self.x, self.y, 30, 30)
            
    def change(self):
        for Residence in residences:
            
            distence = sqrt((self.x - Residence.x)**2 + (self.y - Residence.y)**2)
            
            if Residence.status == 'hunting':
                if distence <= 30:
                    Residence.stress += 1
                    
                    if Residence.stress >= 100 :
                        if self.status == 'farming' and Residence.status == 'hunting':
                            Residence.status = 'farming'
                            break
                        elif self.status == 'hunting' and Residence.status == 'farming':
                            Residence.status = 'farming'
                            break
            elif Residence.status == 'farming':
                continue
                        

#main
RESIDENCE = 500

residences = []

for i in range(RESIDENCE):
    residences.append(Residence(x=random(0, 500), y=random(0, 500)))
    
residences[0].status = 'farming'
residences[1].status = 'farming'

def setup():
    frameRate(60)
    size(500, 500)
    
def draw():
    background(127)

    for residence in residences:
        residence.change()
        residence.display()