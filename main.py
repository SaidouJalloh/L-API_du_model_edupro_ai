from app import app
import os
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8282))
    app.run(debug=True, host='0.0.0.0', port=port)