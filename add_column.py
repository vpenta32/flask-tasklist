from app import create_app, db
from sqlalchemy import text

app = create_app()

with app.app_context():
    # Aggiungi la nuova colonna 'done' alla tabella 'event'
    with db.engine.connect() as connection:
        connection.execute(text('ALTER TABLE event ADD COLUMN date DATE'))
    print("Colonna 'date' aggiunta alla tabella 'event'.")
