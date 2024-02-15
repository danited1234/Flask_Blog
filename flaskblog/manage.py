from run import db, Admin
import bcrypt
import os
import getpass
import sys
def add_super_user():
    salt=bcrypt.gensalt()
    loop=True
    while loop:
        if Admin.query.all():
            Yes_NO=input("A super User already exists want to create another?y/n\n")
            if 'y'  in Yes_NO.lower():
                username=input('add username\n')
            
                password=getpass.getpass('password')
                confirm_password=getpass.getpass("confirm_password")
                if password==confirm_password:
                    bytes=password.encode('utf-8')
                    hash=bcrypt.hashpw(bytes,salt)
                    user=Admin(username=username,password=hash)
                    db.session.add(user)
                    db.session.commit()
                    print("super user created")
                    loop=False
                else:
                    os.system("clear")
                    print("wrong password")
            else:
                loop=False
        else:
            username=input('add username\n')
            password=getpass.getpass('password\n')
            confirm_password=getpass.getpass("confirm_password\n")
            if password==confirm_password:
                bytes=password.encode('utf-8')
                hash=bcrypt.hashpw(bytes,salt)
                user=Admin(username=username,password=hash)
                db.session.add(user)
                db.session.commit()
                loop=False
            else:
                os.system("clear")
                print("wrong password")
def deleteUser():
    while True:
        if db.session.query(Admin).count()==0:
            print("No superuser exists create one first")
            break
        else:
            username=input("Enter username\n")
            password=getpass.getpass("Enter password")
            user=Admin.query.filter_by(username=username).first()
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
                db.session.delete(user)
                db.session.commit()
                break
            else:
                os.system("clear")
                print("wrong username or password entered")

if __name__=='__main__':
    string="""Usage:
python3 manage.py --help
python3 manage.py createsuperuser
python3 manage.py deletesuperuser
python3 manage.py runserver filename.py
""" 
    if len(sys.argv)<2:
        print(string)
        sys.exit(1)
    elif 'createsuperuser' in sys.argv[1]:
        add_super_user()
    elif 'deletesuperuser' in sys.argv[1]:
        deleteUser()
    elif 'runserver' in sys.argv[1]:
        if '.py' in sys.argv[2]:
            if sys.platform == 'win32' or sys.platform == 'cygwin':
                os.system(f"python {sys.argv[2]}")
            elif sys.platform == 'linux' or sys.platform == 'darwin':
                os.system(f"python3 {sys.argv[2]}")
            else:
                print(string)
        else:
            print(string)
    else:
        print(string)

