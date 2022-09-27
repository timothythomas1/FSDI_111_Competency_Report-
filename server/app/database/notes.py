from app.database import get_db

# The functions cursor(), execute(statement, ()), fetchall(), close()

def output_formatter(results): # Takes in a Tuple of Tuples and converts it into a mutable List of dictionaries
    out = []
    for result in results:
        entry = {
            "id": result[0],
            "title": result[1],
            "subtitle": result[2],
            "body": result[3],
            "created_at": result[4]
        }
        out.append(entry)
    return out # Returns a List of Dictionaries

def scan(): 
    statement = "SELECT * FROM notes"
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(statement, ())
    out = cursor.fetchall()
    cursor.close()
    return output_formatter(out) 

def select_by_id(pk):
    statement = "SELECT * FROM notes WHERE id=?" # name is mapped to the question mark into a Tuple 
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(statement, (pk, )) # trailing comma is necessary even if there is only one data input
    out = cursor.fetchall()
    cursor.close()
    return output_formatter(out)

def create(raw_json): # The question marks are used to prevent SQL injections AKA sanatizing the data
    statement = """
        INSERT INTO notes (
            title,
            subtitle,
            body
        ) VALUES (?, ?, ?)
    """
    conn = get_db()
    conn.execute(statement,
            (
                raw_json["title"],
                raw_json["subtitle"],
                raw_json["body"]
            )
        )
    conn.commit()
    conn.close()

def update(raw_json, pk):
    statement = """
        UPDATE notes
        SET title=?,
        subtitle=?,
        body=?
        WHERE id=?
    """
    conn = get_db()
    conn.execute(statement,
            (
                raw_json["title"],
                raw_json["subtitle"],
                raw_json["body"],
                pk
            )
        )
    conn.commit()
    conn.close()

def delete(pk):
    statement = "DELETE FROM notes WHERE id=?"
    conn = get_db()
    conn.execute(statement, (pk, ))
    conn.commit()
    conn.close()
