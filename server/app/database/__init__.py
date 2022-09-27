from flask import g # g = 'Global' Context variable that can be accessed anywhere in the application, so long as it's running.
import sqlite3

DATABASE_URL="notes.db"

# Helper function
def get_db():
    db = getattr(g, "_database", None) # Checks if g attribute of "_database" exists
    if not db: # if "_database" does not exist, then this creates a new table?
        db = g._database = sqlite3.connect(DATABASE_URL)
    return db # Returns a Tuple of Tuples
