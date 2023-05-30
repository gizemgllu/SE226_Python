from tkinter import *
import mysql.connector
from datetime import datetime
from tkinter import messagebox


def setup_database():
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456"
    )

    cursorObject = dataBase.cursor()
    cursorObject.execute("CREATE DATABASE IF NOT EXISTS marveldatabase")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="marveldatabase",
        password="000000"
    )

    cursor = connection.cursor()

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL server version", db_Info)

        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database:", record)

        table = cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies_data (
                ID int(10) NOT NULL,
                MOVIE varchar(250) NOT NULL,
                DATE DATE,
                MCU_PHASE varchar(50),
                PRIMARY KEY (ID)
            )
        ''')
        print("movies_data table created successfully")

        cursor.execute("SHOW TABLES")
        for table_name in cursor:
            print(table_name)

        cursor.execute("SELECT COUNT(*) FROM movies_data;")
        row_count = cursor.fetchone()[0]

        if row_count > 0:
            print("Table already filled. Skipping data insertion.")
        else:
            with open('/Users/tareq2000mf/Documents/Uni/2nd year/SE226/Lab9/Marvel.txt', 'r') as file:
                for line in file:
                    line = line.strip().split()
                    movie_id = int(line[0])
                    movie_name = line[1]
                    movie_date = datetime.strptime(line[2], '%B%d,%Y').date()
                    formatted_date = movie_date.strftime('%Y-%m-%d')
                    mcu_phase = line[3]
                    cursor.execute("INSERT INTO movies_data (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)",
                                   (movie_id, movie_name, formatted_date, mcu_phase))
                print("Data inserted successfully")

        connection.commit()

        cursor.execute("SELECT * FROM movies_data;")
        data = cursor.fetchall()
        for x in data:
            print(x)

        connection.close()


def add_movie():
    popup_window = Toplevel(root)
    popup_window.title("Add New Movie")

    entry_text = Text(popup_window, height=5, width=30)
    entry_text.pack()

    def ok_btn_click():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            database="marveldatabase",
            password="000000"
        )
        cursor = connection.cursor()
        entry_data = entry_text.get("1.0", END).strip()
        for line in entry_data.splitlines():
            line = line.strip().split()
            movie_id = int(line[0])
            movie_name = line[1]
            movie_date = datetime.strptime(line[2], '%B%d,%Y').date()
            formatted_date = movie_date.strftime('%Y-%m-%d')
            mcu_phase = line[3]
            cursor.execute("INSERT INTO movies_data (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)",
                           (movie_id, movie_name, formatted_date, mcu_phase))
        connection.commit()
        print("Data inserted successfully")
        connection.close()
        list_all_movies()
        messagebox.showinfo("Movie Added", "The movie was added to the database successfully.")
        popup_window.destroy()

    ok_button = Button(popup_window, text="Ok", command=ok_btn_click)
    ok_button.pack(side=LEFT)

    def cancel_btn_click():
        popup_window.destroy()

    cancel_button = Button(popup_window, text="Cancel", command=cancel_btn_click)
    cancel_button.pack(side=LEFT)


def list_all_movies():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="marveldatabase",
        password="000000"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies_data;")
    data = cursor.fetchall()
    Data = {x[0]: (x[1], x[2], x[3]) for x in data}
    text_box.delete(1.0, END)
    for key, value in Data.items():
        text_box.insert(END, f"Key: {key}\n")
        text_box.insert(END, f"Value: {value}\n")
        text_box.insert(END, "-" * 82 + "\n")
    connection.close()


def find_data(event):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="marveldatabase",
        password="000000"
    )
    cursor = connection.cursor()
    ID = clicked.get()[1:-2]
    cursor.execute(f"SELECT ID, MOVIE, DATE, MCU_PHASE FROM movies_data WHERE ID = {ID}")
    movie_info = cursor.fetchall()
    connection.close()
    text_box.delete(1.0, END)
    text_box.insert(END, movie_info)


root = Tk()
root.title("Marvel Movies")
root.geometry("600x400")
root.resizable(False, False)

add_button = Button(text="Add", command=add_movie, height=2, width=15)
add_button.place(x=275, y=10)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="marveldatabase",
    password="000000"
)
cursor = connection.cursor()
cursor.execute("SELECT ID FROM movies_data")
IDs = cursor.fetchall()
connection.close()
options = []
for ID in IDs:
    options.append(ID)

clicked = StringVar(root)
clicked.set("ID")
dropdown = OptionMenu(root, clicked, *options, command=find_data)
dropdown.place(x=450, y=20)

text_box = Text(root, height=25, width=83)
text_box.place(x=5, y=60)

list_all_button = Button(root, text="LIST ALL", command=list_all_movies, height=2, width=15)
list_all_button.place(x=100, y=10)

root.mainloop()

