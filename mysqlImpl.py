import mysql.connector


mydb = mysql.connector.connect(    # Connect to systemeDeChatBot
    host="localhost",
    port=3306,
    user="root",
    password="n_Naima_n@1",
    database="systemeDeChatBot"
)

print("Connected to:", mydb.server_info)

cursor = mydb.cursor()


"""cursor.execute("SHOW TABLES")   # Show tables in this database

print("\nTables in systemeDeChatBot:")
for table in cursor:
    print("-", table[0])"""


cursor.execute("""
create table if not exists user (            #user table
    id int auto_increment primary key,
    name varchar(50),
    email_adress varchar(50) unique,
    pass_word varchar(60),
    )
""")  


cursor.execute("""
create table if not exists session(           # session table
    session_id int auto_increment primary key,
    session_date date,
    user_id int,
    foreign key (user_id) references user(id))
""")               

cursor.execute("""
create table if not exists apiservice (          # table apiservice
    id int auto_increment primary key,
    nom_api varchar(100)
)
""")

mydb.commit()
cursor.close()
mydb.close()


      
    





