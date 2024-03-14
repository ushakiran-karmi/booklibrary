class Books:
    def __init__(self):
        self.name=""
        self.author=""
        self.price=0.0
        self.isbn=""
        
    def inputBookDetails(self):
        self.name=input("enter the book name:")
        self.author=input("enter the authoe name:")
        self.price=float(input("enter the book price:"))
        self.isbn=input("enter book ISBN number:")
        print(f"{self.name} book added successfully:")
        print("-"*20)
        
    def booksdisplay(self):
        print(f'book name : {self.name}')
        print(f'author name : {self.author}')
        print(f'book price : {self.price}')
        print(f'book ISBN NO : {self.isbn}')
        print("-"*20)
        
my_booklist=[]

while True:  
    choice=int(input("enter your choice \n1. Add book \n2. display book \n3.stop\n"))
    
    if choice==1:
        b=Books()
        b.inputBookDetails()
        my_booklist.append(b)   
        
    elif choice==2:
        for i in my_booklist:
            i.booksdisplay()
            
    elif choice==3:
        print("Thanks for using application")
        break 
    
    else:
        print("enter a valid option")       
            
            
