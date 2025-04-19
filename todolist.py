print("Welcome to my to-do list bot program!")
print("This bot allows you to store to-do-list items with a due date!")
print("Then the program will relay that information to the discord server!")
print("Eventually, we will be able to add custom commands through discord to save to-do items!")
print("------------------------------------")

#GLOBAL VARIABLES

Menu_Choice = ""
ToDo_List = [
    ["Fix my phython code", 
    "April 25th"]
]


#FUNCTIONS
def ShowAllTodoItems(): 
    i = 0 
    for i in range(len(ToDo_List)): 
        print(i+1,".","Task -",ToDo_List[i][0])
        print("Task -",ToDo_List[i][1])
        i+=1
        if i < len(ToDo_List):
            print()
    CreateBorder()

def AddToDoItem(): 

    print("Adding task to To-Do List!")
    item = []
    task = input("Enter your task: ")
    duedate = input("Enter the due date: ")
    item.append(task)
    item.append(duedate)
    ToDo_List.append(item)
    print("Added task to To-Do List!")
    CreateBorder()


def PrintMenuItems(): 
    print("1) Add To-do Items")
    print("2) Show All To-do Items")
    print("3) Check one To-do Items by index")
    print("4) Remove A To-Do List")
    CreateBorder()

def CreateBorder():
    print("---------------------------------")

def RemoveItemFromIndex(): 
    i = 0 
    for i in range(len(ToDo_List)): 
        print(i+1,".","Task -",ToDo_List[i][0])
        print("Task -",ToDo_List[i][1])
        i+=1
    Choose_Index = int(input("What to-do list do you want to delete?\n (Warning! The first list starts at 0!) List: "))
    if Choose_Index < 0: 
        print("PLease put a valid number!")
    elif len(ToDo_List) < Choose_Index: 
        print("Please put a valid number! ")
    else:
        ToDo_List.pop([Choose_Index][0])
    print("It is done!")
    print(ToDo_List)
    print("---------------------------------")

    


def ShowItemFromIndex():

    Input_Index = int(input("What list do you want show? \nThe first list is 0!: "))
    if Input_Index < 0: 
        print("Please put a valid number!")
    elif len(ToDo_List) < Input_Index: 
        print("Please put a valid number!")
    else: 
        print(ToDo_List[Input_Index])
        CreateBorder()
    #show item from its index 
    #list: [oaifjeieajf] = 0 index 
    #print(the users input list)

def HandleUserMenuChoice(choice):
    match choice: 
        case "1": 
            AddToDoItem()
        case "2":
            ShowAllTodoItems()
        case "3":
            ShowItemFromIndex()
        case "4": 
            RemoveItemFromIndex()

    CreateBorder()

def GetUserMenuChoice(): 
    Menu_Choice = input("What do you want to do?")
    CreateBorder()
    return Menu_Choice


#RUNS AND COMMANDS

while True:
    PrintMenuItems() 
    HandleUserMenuChoice(GetUserMenuChoice())
   
