import sqlite3
import os
import time
from rgbprint import gradient_print, Color
from prettytable import PrettyTable

### Loading Function 
def typewriter(text, delay=0.1):
  for letter in text:
    print(letter, end='', flush=True)
    time.sleep(delay)
  print()

### Color Function
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


database_conn = sqlite3.connect("mydata.db") # database connection created !
curdb = database_conn.cursor() # create cursor !
curdb.execute(""" CREATE TABLE IF NOT EXISTS userdata(webname text, email text, username text, passw text) """) # table created

my_table = PrettyTable() # Table 

### MAIN 
def main():
    banner = colored(230, 230, 250,'''
█▀█ ▄▀█ █▀ █▀ █▀ ▄▀█ █ █ █▀▀
█▀▀ █▀█ ▄█ ▄█ ▄█ █▀█ ▀▄▀ ██▄''') ## Header Banner
    
    while True:
        os.system("cls")
        print(banner)
        gradient_print(
        "@amitgajare_\t Version 1.5", 
        start_color=Color.yellow, 
        end_color=Color.orange_red)

        gradient_print("\n1.Add\n2.Show\n3.Update\n4.Delete\n5.Show All\n6.Exit\n", start_color=Color.pink, end_color=Color.blue)
        options = input(colored(230, 230, 250, "Select Option > "))

        ###### Add Details
        if options == "1":
            webname = input(colored(255,20,147, "Website Name > " ))
            webname =  webname.lower()
            useremail = input(colored(124,252,0, "Email > " ))
            useremail =  useremail.lower()
            username = input(colored(244,154,96, "UserName > " ))
            userpass = input(colored(0,255,154, "PassWord > " ))
            userpass2 = input(colored(220,20,60, "PassWord Again > " ))

            if len(webname) != 0 and len(username) != 0 and len(userpass) != 0:
                if userpass==userpass2:
                    curdb.execute(" INSERT INTO userdata VALUES(?,?,?,?) ",[webname, useremail, username, userpass]) # data added
                    database_conn.commit()
                    os.system("cls")
                    colored(0,255,0, "Added Successfully...")
                    typewriter("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁", 0.01)
                    os.system("cls")
                else:
                    colored(220,20,60, "PassWord Not Match...")
            else:
                colored(220,20,60, "Please Fill All Details...")

        ###### Show Details
        elif options == "2":
            gradient_print("\n1.Primary Key\n2.WebName\n3.Back\n", start_color=Color.royal_blue, end_color=Color.powder_blue)
            search_by = input(colored(230, 230, 250, "Select Option > ")) or "3" # Default value is 3 for back

            if search_by == "1": # Search by primary key
                os.system("cls")
                pkey = input(colored(220,20,60, "Enter Primary Key > "))
                curdb.execute(f" SELECT rowid, * FROM userdata WHERE rowid={pkey} ")
                items = curdb.fetchall()
                my_table.field_names = ["Key", "Website", "Email", "Username", "Password"]

                for item in items:
                    data1 = item[0]
                    data2 = item[1]
                    data3 = item[2]
                    data4 = item[3]
                    data5 = item[4]
                    my_table.add_row([data1, data2, data3, data4, data5])

                os.system("cls")
                print(my_table)

            elif search_by == "2": # Search by website name
                os.system("cls")
                wkey = input(colored(220,20,60, "Enter Website Name > "))
                curdb.execute(f" SELECT rowid, * FROM userdata WHERE webname='{wkey}' ")
                items = curdb.fetchall()
                my_table.field_names = ["Key", "Website", "Email", "Username", "Password"]
                
                for item in items:
                    data11 = item[0]
                    data21 = item[1]
                    data31 = item[2]
                    data41 = item[3]
                    data51 = item[4]
                
                my_table.add_row([data11, data21, data31, data41, data51])
                os.system("cls")
                print(my_table)
            
            elif search_by == "3": # Back to the main function
                os.system("cls")
                main()
            
            clearsc = input(colored(100,149,237, "Press Any Key To Clear Screen "))

            if len(clearsc) !=0 :
                os.system("cls")
            else:
                os.system("cls")

        ###### Update Details
        elif options == "3":
            gradient_print("\n1.Update All\n2.Username\n3.Password\n4.Email\n5.Back\n", start_color=Color.golden_rod, end_color=Color.brown)
            selectop = input(colored(230, 230, 250, "Select Option > ")) or "5" # Default value is 5 for back

            if selectop == "1":  # All Details
                wkey = input(colored(220,20,60, "Enter Primary Key > "))
                user_update = input(colored(244,154,96, "New UserName > " ))
                pass_update = input(colored(0,255,154, "New PassWord > " ))
                email_update = input(colored(124,252,0, "New Email > " ))

                curdb.execute(f" UPDATE userdata SET username='{user_update}', passw='{pass_update}', email='{email_update}'  WHERE rowid={wkey} ")
                database_conn.commit()
                typewriter("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁", 0.01)
                os.system("cls")

            elif selectop == "2": # Username
                wkey = input(colored(220,20,60, "Enter Primary Key > "))
                user_update = input(colored(244,154,96, "New UserName > " ))

                curdb.execute(f" UPDATE userdata SET username='{user_update}' WHERE rowid={wkey} ")
                database_conn.commit()
                typewriter("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁", 0.01)
                os.system("cls")

            elif selectop == "3": # Password
                wkey = input(colored(220,20,60, "Enter Primary Key > "))
                pass_update = input(colored(0,255,154, "New PassWord > " ))

                curdb.execute(f" UPDATE userdata SET passw='{pass_update}' WHERE rowid={wkey} ")
                database_conn.commit()
                os.system("cls")

            elif selectop == "4": # Email
                wkey = input(colored(220,20,60, "Enter Primary Key > "))
                email_update = input(colored(124,252,0, "New Email > " ))

                curdb.execute(f" UPDATE userdata SET passw='{email_update}' WHERE rowid={wkey} ")
                database_conn.commit()
                os.system("cls")

            elif selectop == "5": # Back
                os.system("cls")
                main()
            else:
                os.system("cls")
                main()

        ### Delete Details
        elif options == "4":
            os.system("cls")
            colored(220,20,60, "--- Use Key To Delete Data ---\n")
            dkey = input(colored(220,20,60, "Enter Primary Key > "))
            curdb.execute(f" DELETE FROM userdata WHERE rowid={dkey} ")
            typewriter("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁", 0.01)
            os.system("cls")

        ### Show All Keys
        elif options == "5": 
            typewriter("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁", 0.02)
            os.system("cls")

            curdb.execute(" SELECT rowid, * FROM userdata ")
            items = curdb.fetchall()

            print("\n")
            
            for item in items:
                print("Key |", item[0], "| Website | ", item[1])
                print("---------------------------------------")
                
            clearsc = input(colored(100,149,237, "\n\nPress Any Key To Clear Screen "))

            if len(clearsc) !=0 :
                os.system("cls")
            else:
                os.system("cls")

        ### Exit Code
        elif options == "6":
            database_conn.close()
            os.system("cls")
            exit()
        else:
            os.system("cls")
            colored(220,20,60, "Please Enter Right Option...")


##### Login System Code Start Here

if os.path.exists("data.db"):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
else:
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute(" CREATE TABLE accounts(uname text, pwd text) ")

accOrLog = input("1. Login\n2. Signup\n3. Exit\n\n--> ") 

### Signup User
if accOrLog == "2":
    uname = input("Enter Username : ")
    upass = input("Password : ")
    upass2 = input("Conform Password : ")

    if upass == upass2:
        cur.execute(f" INSERT INTO accounts VALUES(?,?) ", [uname, upass])
        print("Account Successfully Created")
        conn.commit()
        typewriter("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁", 0.02)
        os.system("cls")
    else:
        print("Error")

### Login User
elif accOrLog == "1":
    uname = input("Enter Username : ")
    pwd = input("Enter Password : ")

    cur.execute(" SELECT * FROM accounts WHERE uname=? AND pwd=?", [uname, pwd])

    if cur.fetchone()==None:
        print("Wrong Details")
    else:
        typewriter("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁", 0.09)
        os.system("cls")
        main() #main
elif accOrLog=="3":
    exit()
else:
    print("Please Select Right Option...")

#### End Code 
