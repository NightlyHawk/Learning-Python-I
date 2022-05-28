from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
          self.name = name
          self.age = age
          self.tracks = tracks
          self.score = score
    def getScore(self):    
        return self.score 
    
    def change_name(self, name):
        self.name = str(name)
    def getName(self):    
        return self.name    
    
    def change_age(self, age):
        self.age = int(age)
    def getAge(self):    
        return self.age    

    def add_track(self, track):
        self.track = list(track)
    def getTrack(self):    
        return self.track   

    def set_score(self, score):
        self.score = float(score)
    def get_score(self):    
        return self.score        
    
       
    # Retrieves instance variable    
      

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# # Expected methods
Bob.change_name("Peter")
print(Bob.getName())
Bob.change_age(34)
print(Bob.getAge())
Bob.add_track("UI/UX")
print(Bob.getTrack())   
Bob.getScore()
print(Bob.getScore())

