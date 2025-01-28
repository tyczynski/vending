import os
from app import app

if __name__ == '__main__':
    debug = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1']
    app.run(debug=debug)
