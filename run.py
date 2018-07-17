"""
The File contains the script that starts the application
"""

# Run a application server.
from app.application import app
import urllib.parse as urlparse
import os

#import app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
