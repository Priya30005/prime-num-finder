from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends, Form
from fastapi.responses import HTMLResponse

# Importing models and database functions
from ..models import PrimeRequest, PrimeResponse
from ..database import get_db

# SQLAlchemy imports
from sqlalchemy.orm import Session
from sqlalchemy import text

import time
from datetime import datetime

# Importing prime number generation methods
from .prime_no_generator import brute_force_method, trial_division_method, miller_rabin_method, sieve_of_eratosthenes_method

# Create a FastAPI router
router = APIRouter()

# Function to write execution details to the database
def write_to_db(prime_no, request, start_time, db: Session):
    # Calculate end time and time elapsed
    end_time = time.time()
    time_elapsed = round(end_time - start_time, 6)
    timestamp_str = datetime.fromtimestamp(start_time).strftime('%H:%M:%S')

    # Insert execution details into the database
    db.execute(
        text("INSERT INTO executions (timestamp, range_start, range_end, time_elapsed, method, num_primes) VALUES (:timestamp, :range_start, :range_end, :time_elapsed, :method, :num_primes)"),
        {"timestamp": timestamp_str, "range_start": request.start, "range_end": request.end, "time_elapsed": time_elapsed, "method": request.method, "num_primes": len(prime_no)}
    )
    db.commit()

# Endpoint to generate prime numbers
@router.post("/primes", response_model=PrimeResponse)
def generate_primes(
    background_tasks: BackgroundTasks,
    start: int = Form(...),
    end: int = Form(...),
    method: str = Form(...),
    db_and_engine: tuple = Depends(get_db)
):
    # Unpack the database session from the tuple
    db, engine = db_and_engine
    request = PrimeRequest(start=start, end=end, method=method)
    start_time = time.time()

    # Choose prime number generation method based on the request
    if request.method == "brute_force":
        prime_no = brute_force_method(request.start, request.end)
    elif request.method == "trial_division":
        prime_no = trial_division_method(request.start, request.end)
    elif request.method == "miller_rabin":
        prime_no = miller_rabin_method(request.start, request.end)
    elif request.method == "sieve_of_eratosthenes":
        prime_no = sieve_of_eratosthenes_method(request.start, request.end)
    else:
        raise HTTPException(status_code=400, detail="Invalid method")

    # Add a background task to write execution details to the database
    background_tasks.add_task(write_to_db, prime_no, request, start_time, db)

    # Return the generated prime numbers and time elapsed
    return PrimeResponse(primes=prime_no, time_elapsed=time.time() - start_time)

# Homepage endpoint to provide a form for prime number generation
@router.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <html>
        <head>
            <title>Prime Number Generator</title>
        </head>
        <body>
            <h1>Prime Number Generator</h1>
            <form action="/primes" method="post">
                <label for="start">Start Range:</label>
                <input type="number" id="start" name="start" required><br><br>
                <label for="end">End Range:</label>
                <input type="number" id="end" name="end" required><br><br>
                <label for="method">Method:</label>
                <select id="method" name="method">
                    <option value="brute_force">Brute Force</option>
                    <option value="trial_division">Trial Division</option>
                    <option value="miller_rabin">Miller-Rabin</option>
                    <option value="sieve_of_eratosthenes">Sieve of Eratosthenes</option>
                </select><br><br>
                <input type="submit" value="Generate Primes">
            </form>
        </body>
    </html>
    """
    return html_content
