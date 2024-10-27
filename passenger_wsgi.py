import sys
import os

# Add the application directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask app
from app import app as application  # Ensure 'app.py' contains your Flask app
