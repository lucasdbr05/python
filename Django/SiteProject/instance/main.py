from fluminense import app
from fluminense import database

if __name__ == '__main__':
    with app.app_context():
        database.create_all()
    app.run(debug=True)
