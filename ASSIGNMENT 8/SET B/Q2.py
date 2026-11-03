from flask import Flask
import psycopg2

app = Flask(__name__)

def db_connect():
    return psycopg2.connect(
        dbname = 'library',
        user = 'postgres',
        password = 'root',
        host = 'localhost',
        port = '5432'
    )

# create books table
@app.route('/create_table')
def create_table():
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Books(
                bid SERIAL PRIMARY KEY,
                title VARCHAR(100),
                author VARCHAR(100),
                price INT
            );
        """)

        conn.commit()
        cur.close()
        conn.close()
        return "Books Table Created Successfully!"

    except Exception as e:
        return f"Error : {e}"

# Insert records in Books table
@app.route('/insert_records')
def insert_books():
    try:
        conn = db_connect()
        cur = conn.cursor()

        books = [
            ("Python Basics", "John Smith", 350),
            ("Flask Development", "David Miller", 450),
            ("SQL for Beginners", "Anita Sharma", 300),
            ("Web Development", "Robert Brown", 500),
            ("Data Science", "Priya Patil", 600)
        ]

        cur.executemany("INSERT INTO Books (title, author, price) VALUES(%s,%s,%s);", books)
        conn.commit()
        cur.close()
        conn.close()
        return "Records inserted successfully in Books table!"

    except Exception as e:
        return f"Error : {e}"

# Retrieve and display all books with their Author and Price.
@app.route('/display_books')
def display_books():
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("SELECT title, author, price FROM Books;")
        books = cur.fetchall()

        
        cur.close()
        conn.close()

        book_list = ""
        for book in books:
            books = [
    ("Python Programming", "Reema Thareja", 450),
    ("Let Us C", "Yashavant Kanetkar", 350),
    ("Java Programming", "Herbert Schildt", 650),
    ("Wings of Fire", "A.P.J. Abdul Kalam", 250),
    ("Database System Concepts", "Abraham Silberschatz", 700)
    ]
            ""
        return book_list

    except Exception as e:
        return f"Error : {e}"

if __name__ == '__main__':
    app.run(debug=True)