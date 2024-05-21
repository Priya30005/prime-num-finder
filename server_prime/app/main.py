# Importing the FastAPI class to create an instance of the web application.
from fastapi import FastAPI

# Importing the 'primes' and 'executions' modules from the 'routers' package.
# These modules contain the APIRouter instances that define the routes for the prime number generation and execution details.
from .routers import primes,executions

# Creating an instance of the FastAPI application.
app = FastAPI()

# Including the routers from the 'primes' and 'executions' modules into the main application.
app.include_router(primes.router)
app.include_router(executions.router)
