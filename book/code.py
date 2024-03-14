class Books:
    def __init__(self):
        self.name=""
        self.author=""
        self.price=0.0
        self.isbn=""
        
    def inputBookDetails(self):
        self.name=input("Enter the book name:")
        self.author=input("Enter the author name:")
        self.price=float(input("Enter the book price:"))
        self.isbn=input("Enter book ISBN number:")
        print(f"{self.name} Book added successfully:")
        print("-"*20)
        
    def booksdisplay(self):
        print(f'Book name : {self.name}')
        print(f'Author name : {self.author}')
        print(f'Book price : {self.price}')
        print(f'Book ISBN NO : {self.isbn}')
        print("-"*20)
        
my_booklist=[]

while True:  
    choice=int(input("Enter your choice \n1. Add book \n2. Display book \n3.Stop\n"))
    
    if choice==1:
        b=Books()
        b.inputBookDetails()
        my_booklist.append(b)   
        
    elif choice==2:
        if len(my_booklist)==0:
            print("No books are available")
        else:
            for i in my_booklist:
                i.booksdisplay()
            
            
            
    elif choice==3:
        print("Thanks for using application")
        break 
    
    else:
        print("Enter a valid option")       
            
print(my_booklist)            
            
