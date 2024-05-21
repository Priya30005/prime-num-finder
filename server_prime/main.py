# Importing the uvicorn module, which is an ASGI server implementation.
# It serves as the web server to run the FastAPI application.
import uvicorn

# Importing the 'app' instance from the 'main' module of the 'app' package.
# This 'app' is the FastAPI application that has been created and configured.
from app.main import app

# A common Python idiom to ensure the code runs only when the script is executed directly, not when imported.
if __name__ == "__main__":
    # Running the Uvicorn server with the FastAPI application.
    # The host '0.0.0.0' makes the server accessible on all network interfaces,
    # and port 8000 is the default port for web applications.
    uvicorn.run(app, host="0.0.0.0", port=8000)
