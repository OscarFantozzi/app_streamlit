import streamlit as st
import pyodbc

# criar a classe cliente
class customer:
    def __init__(self,name,email):
        customer.name  = name
        customer.email = email

# criando a função conexão
def connect_db():
    server = 'DESKTOP-J6PBL6B' 
    database = 'st_test_app' 
    username = 'teste' 
    password = '123456' 
    cnxn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};'
                          'Server=DESKTOP-J6PBL6B;'
                          'Database=st_test_app;'
                          'Trusted_Connection=yes;'
                          'UID={teste};'
                          'PWD=123456;'
                          'Encrypt=no'
                         )
    cursor = cnxn.cursor()
    return cursor

# insert database
def insert_into_db( cliente , cursor ):
    cursor.execute("""
    INSERT INTO customer (Nome, email) 
    VALUES (?,?)""",
    cliente.name,cliente.email)
    cursor.commit()
    
#========================================================================================================================================#


# header
st.header( 'Register Customers' )

with st.form(key = 'Customer_form', clear_on_submit = True ):
    # dados cadastro
    input_name = st.text_input(label = 'Insert your name')

    # dados cadastro
    input_email = st.text_input(label = 'Insert your email')

    # submit 
    button = st.form_submit_button(label = 'sign up')

if button:
    # cria conexão com cursor
    cursor = connect_db()
    
    # insere dados no bd
    customer.name  = input_name
    customer.email = input_email
    insert_into_db(customer,cursor)
    
    st.write("Sign up succesful")
    

