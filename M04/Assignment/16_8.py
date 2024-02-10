from sqlalchemy import create_engine, MetaData, Table, select

# Connect to the database using SQLAlchemy
engine = create_engine('sqlite:///books.db')
metadata = MetaData()
books = Table('books', metadata, autoload=True, autoload_with=engine)

# Select the title column from the books table in alphabetical order
s = select([books.c.title]).order_by(books.c.title)

# Execute the query and print the results
conn = engine.connect()
result = conn.execute(s)

for row in result:
    print(row['title'])

# Close the connection
conn.close()
