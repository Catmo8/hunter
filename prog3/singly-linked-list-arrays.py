
class SinglyLinkedList:
    Data = []
    Link = []
    headPtr = 0

    def _init_(self, length):
        for i in range(length):
            self.FreeNodes.append(True)

    def GetNode(self):
        for i in self.FreeNodes:
            if self.FreeNodes[i] is True:
                return i
        return -1

 
#    def PrintLinkedList(self):


#    def InsertNode(self, newNode):


def PrintMenu():
    print()
    print("Enter the letter that corresponds to the desired singly-linked list operation:")
    print("A. Insert a new item (i.e., string) into the ordered singly-linked list.")
    print("B. Deleted a specified item (i.e., string) into the ordered singly-linked list.")
    print("C. Print all items (i.e., strings) in the ordered singly-linked list.")
    print("D. Print the Data array, Link array, FreeNodes array, and value of headPtr.")
    print("E. End Program.")
    print()


length = input("What size do you want this garbage to be?")

SinList = SinglyLinkedList(length)

while (True):
    PrintMenu()
    case = input().upper()
    if (case == 'A'):
        break
    elif (case == 'B'):
        break
    elif (case == 'C'):
        break
    elif (case == 'D'):
        break
    elif (case == 'E'):
        break
    else:
        print("Invalid option! Please enter A, B, C, D or E.")
