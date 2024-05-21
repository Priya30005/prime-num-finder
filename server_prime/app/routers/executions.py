from fastapi import APIRouter, Depends  # APIRouter is used to create modular routes, Depends is used for dependency injection
from fastapi.responses import HTMLResponse  # HTMLResponse is used to create HTTP responses with HTML content

# SQLAlchemy is the Python SQL toolkit and Object-Relational Mapping (ORM) library that gives application developers the full power and flexibility of SQL.
from sqlalchemy import inspect  # inspect is used to get detailed information about SQLAlchemy objects
from sqlalchemy import text  # text is used to create textual SQL statements
from ..database import get_db
# Create a new router
router = APIRouter()

# Define a new route. This route responds to GET requests at the "/executions" URL. The response is of type HTML.
@router.get("/executions", response_class=HTMLResponse)
def get_table(db_engine: tuple = Depends(get_db)):  # The function depends on get_db to get a database session
    db, engine = db_engine  # Unpack the database session and engine from the tuple
    inspector = inspect(engine)  # Create an inspector for the engine
    table_name = 'executions'  # Define the table name
    columns = [column['name'] for column in inspector.get_columns(table_name)]  
    rows = db.execute(text("SELECT * FROM executions")).fetchall()  

     # Find the index of the num_primes column
    num_primes_index = columns.index('num_primes')

    # Start creating the HTML content for the table
    html_content = '''<table style="border:1px solid black; border-collapse: collapse;"><thead><tr>'''
    for column_name in columns:  
        # Add a table header with the column name
        html_content += f'''<th style="border:1px solid black; padding: 10px;">{column_name}</th>'''  
    html_content += "</tr></thead><tbody>"

    for row in rows:  
        html_content += "<tr>"
        num_primes_values = []  # List to collect num_primes values for this row
        for i, item in enumerate(row):
            # Collect 'num_primes' values
            if i == num_primes_index:
                num_primes_values.append(item)
                html_content += f'''<td style="border:1px solid black; padding: 10px;">{num_primes_values}</td>'''
            else:
                # Add a table cell with the item
                html_content += f'''<td style="border:1px solid black; padding: 10px;">{item}</td>'''
        
     
        html_content += "</tr>"
    
    html_content += "</tbody></table>"

    return html_content