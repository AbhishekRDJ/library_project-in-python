import datetime
def issue_book():
    print()
    print("_________________________________________________________________________________________________")
    obj=open("Issued_file.txt","a")
    name=input(" Enter the Student Name :")
    en=input(" Enter the Student Enrollment number :")
    
    book=input(" Enter the book Number :")
    Issue_date = datetime.date.today()
    idate=str(Issue_date.day)+"/"+str(Issue_date.month)+"/"+str(Issue_date.year)
    return_date="NR"
    obj.write(str(name)+" | "+str(en)+" | "+str(book)+" | "+str(idate)+" | "+str(return_date))
    print("Book Issued....")
    print("_________________________________________________________________________________________________")
    obj.close()
    

def return_book():
    print()
    print("_________________________________________________________________________________________________")
    S_en=input(" Enter the Enrollment Number :")
    book_Number=input(" Enter the BOOK number :")
    fobj=open("Issued_file.txt" , "r+")
    ALL_lines=fobj.readlines()
    
    got = False
    for i, line in enumerate(ALL_lines):
        ls3=line.strip().split(" | ")
        if ls3[1]==S_en and ls3[2]==book_Number:
            rd=str(datetime.date.today())
            ls3[4]=rd
            ALL_lines[i] = " | ".join(ls3) + "\n"
            got = True
            print("BOOK is Returned....")
            break
    
    print()
    
    if got:
        fobj=open("Issued_file.txt","w")
        fobj.writelines(ALL_lines)
    else:
        print("---- Student of this Detail are not found ----")
    print("_________________________________________________________________________________________________")
    fobj.close()

def view_not_ret_books():
    print()
    print("_________________________________________________________________________________________________")
    
    fobj = open("Issued_file.txt", "r")
    for find in fobj:
        ls = find.split(" | ")
        if ls[4] == "NR\n":
            print(ls[0], ls[1], ls[2],"not Return", sep=" | ")
        
    print()
    print("_________________________________________________________________________________________________")
    fobj.close()


def add_new_book():
    print()
    print("_________________________________________________________________________________________________")
    obj=open("All_book.txt", "a")
    book_name=input(" Enter Book Name which you want add to library :")
    book_number=input(" Enter book number :")
    book_author=input(" Enter book Author :")
    book_publication=input(" Enter book Publication :")

    obj.write(str(book_name)+" | "+str(book_number)+" | "+str(book_author)+" | "+str(book_publication)+"\n")
    print("Book added....")
    print("_________________________________________________________________________________________________")
    obj.close()
    

def add_new_stud():
    print()
    print("_________________________________________________________________________________________________")
    obj=open("All_Studnet.txt" , "a")
    new_studnet=input(" Enter New Student Name :")
    new_studnet_en=input(" Enter New Student Enrollment Number :")
    new_studnet_mobile_number=input(" Enter New Student Mobile Number :")
    email = input("Enter email id : ")
    obj.write(str(new_studnet)+" | "+str(new_studnet_en)+" | "+str(new_studnet_mobile_number)+" | "+str(email)+"\n")
    
    print("_________________________________________________________________________________________________")
    print("New Student added....")
    obj.close()


def search_book():
    print()
    print("_________________________________________________________________________________________________")
    Book_Name=input(" Enter the Book Name : ")
    Fobj=open("All_book.txt" , "r")
    for i in Fobj:
        ls2=i.split(" | ")
        if ls2[0]==Book_Name:
            print()
            print("---------------- Book Is Present ----------------")
            break
    else:
        print("---------------- Book is NOT present ----------------")
    print()
    print("_________________________________________________________________________________________________")  
    
         
def search_stud():
    print()
    print("_________________________________________________________________________________________________")
    enr = input(" Enter Enrollment Number : ")
    fobj = open("All_Studnet.txt", "r")
    for search in fobj:
        ls = search.split(" | ")
        if ls[1] == enr:
            print(" Name :", ls[0])
            print(" Mobile Number :", ls[2])
            print(" Email Address :", ls[3])
            break
    else:
        print("No such Student Found..")
    print()
    print("_________________________________________________________________________________________________")
    fobj.close()
    

def book_history():
    print()
    print("_________________________________________________________________________________________________")
    fobj=open("Issued_file.txt" , "r")
    book_number=input(" Enter the BOOK Number :")
    print("- - - - - - - - - - - - - - -")
    print("BOOK Issued by -")
    for bh in fobj:
        ls=bh.split(" | ")
        if ls[2]==book_number:
            
            print("-",ls[0])
       
    print("_________________________________________________________________________________________________")
    fobj.close()
    
    
def stud_history():
    print()
    print("_________________________________________________________________________________________________")
    fobj=open("Issued_file.txt" , "r")
    Studnet_en=input(" Enter the Student Enrollment Number :")
    print("- - - - - - - - - - - - - - -")
    print("BOOK Issued by This Student :-")
    for bh in fobj:
        ls1=bh.split(' | ')
        
        if ls1[1]==Studnet_en:
            print((ls1[0]) ,"-" , " |          ",ls1[3],"           | ",ls1[4])
        
    print("_________________________________________________________________________________________________")
    fobj.close()
    

while True:
    
    input()
    print("_________________________________________________________________________________________________")
    print("-----------------------------")

    print("Select operation")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - View Not Returned Books")
    print("4 - Add New Book")
    print("5 - Add New Student")
    print("6 - Search Book")
    print("7 - Search Student")
    print("8 - Book History")
    print("9 - Student History")
    print("0 - EXIT")
    ch = int(input("Provide your choice : ") )
    if ch==1: issue_book()
    elif ch==2: return_book()
    elif ch==3: view_not_ret_books()
    elif ch==4: add_new_book()
    elif ch==5: add_new_stud()
    elif ch==6: search_book()
    elif ch==7: search_stud()
    elif ch==8: book_history()
    elif ch==9: stud_history()
    elif ch==0: exit(0)
