class User:     
    name=None     
    email=None    
    def __init__(self,name,email):    
        self.name=name   
        self.email=email    
    def __str__(self):   
         return "user:" + self.email   
    def send_email(self):     
        if self.email is not None:     
            print("sending email:" + self.email)     
        else:     
            print("Error")     

class Student(User):   
    def is_approved(self): 
        return self.score>=8 
    def __repr__(self): 
       return f"Student(name='{self.name}',email='{self.email}',id='{self.id}',score='{self.score}')" 
    def __str__(self):   
        return  "Student:"+str(self.id)+ ","+self.email  
    def __init__(self,   
        name=None,   
        email=None,   
        id=None,  
        score=None,  
    ):   

     super().__init__(name,email)   
     self.id=uuid.uuid4()   
     self.id=id  
     self.score=score  
