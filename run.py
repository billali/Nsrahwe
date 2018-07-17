"""
The File contains the script that starts the application
"""

# Run a application server.
from app.application import app
from app.config import APP_PORT, APP_HOST, DEBUG

#import app
if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT, debug=DEBUG)
