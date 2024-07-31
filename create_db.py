from app import create_app, db

app = create_app()

with app.app_context():
    # Crea tutte le tabelle nel database
    db.create_all()
    print("Database e tabelle creati.")
