

from passlib.hash import pbkdf2_sha256
import hashlib
import sqlite3 



conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def make_hashes(password):
 
    return pbkdf2_sha256.hash(password, rounds=200000, salt_size=16)



# def check_hashes(password,hashed_text):
#     if pbkdf2_sha256.verify(password,hashed_text):     
#         return hashed_text
#     else:
#         return False


def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

create_usertable()
Vaibhav_pswd = make_hashes('zs_24693')
add_userdata('Vaibhav',Vaibhav_pswd)
Adnan_pswd = make_hashes('zs_10755')
add_userdata('Adnan',Adnan_pswd)
Matt_pswd = make_hashes('zs12345')
add_userdata('Matt',Matt_pswd)
Sagar_pswd = make_hashes('zs12345')
add_userdata('Sagar',Sagar_pswd)
Keith_pswd = make_hashes('zs_14131')
add_userdata('Keith',Keith_pswd)
other_pswd = make_hashes('zs12345')
add_userdata('other',other_pswd)


def check_hashes(username,password):
    
    if username == 'Vaibhav':
        if pbkdf2_sha256.verify(password,Vaibhav_pswd):     
            return Vaibhav_pswd 
    if username == 'Adnan':
        if pbkdf2_sha256.verify(password,Adnan_pswd):     
            return Adnan_pswd
    if username == 'Matt':
        if pbkdf2_sha256.verify(password,Matt_pswd):     
            return Matt_pswd
    if username == 'Keith':
        if pbkdf2_sha256.verify(password,Keith_pswd):     
            return Keith_pswd
    if username == 'Sagar':
        if pbkdf2_sha256.verify(password,Sagar_pswd):     
            return Sagar_pswd        
    if username == 'other':
        if pbkdf2_sha256.verify(password,other_pswd):     
            return other_pswd
    else:
        return False





