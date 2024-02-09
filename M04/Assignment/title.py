from sqlalchemy import create_engine, select, Table, MetaData

# Create an engine to the SQLite database
engine = create_engine('sqlite:///books.db')

# Initialize metadata
metadata = MetaData()

# Reflect books table
books = Table('books', metadata, autoload_with=engine)

# Select titles from books table, ordered alphabetically
query = select([books.c.title]).order_by(books.c.title)

# Execute the query
with engine.connect() as connection:
    result = connection.execute(query)

    # Fetch and print the result of the query
    for row in result.fetchall():
        print(row.title)
