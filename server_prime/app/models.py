# Importing the BaseModel class from Pydantic to define data models.
from pydantic import BaseModel

# Importing the List class from the typing module to specify a list of items of a specific type.
from typing import List

# Defining a data model for the prime number generation request.
# This model will validate the incoming request data against the defined fields.
class PrimeRequest(BaseModel):
    method: str  # A string indicating the method to be used for prime number generation.
    start: int   # An integer marking the start of the range within which to find prime numbers.
    end: int     # An integer marking the end of the range within which to find prime numbers.

# Defining a data model for the response that will be sent back to the client.
# This model ensures that the response data conforms to the specified structure.
class PrimeResponse(BaseModel):
    primes: List[int]  # A list of integers representing the prime numbers found within the specified range.
    time_elapsed: float  # A float representing the time elapsed during the prime number generation process, in seconds.