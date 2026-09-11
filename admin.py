import json
import sys
from firebase_connection import FirebaseConnection

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Too few arguments, expected `python admin.py /path/to/data.json`")
        raise SystemExit()
    if len(sys.argv) > 2:
        print("Too many arguments, expected `python admin.py /path/to/data.json`")
        raise SystemExit()

    movies = []

    try: 
        with open(sys.argv[1]) as f:
            movies = json.load(f)
    except IOError as e:
        print("I/O error: ", e.strerror)
        raise SystemExit()
    
    try:
        connection = FirebaseConnection()
        connection.clear_collection()
        connection.batch_write(movies)
    except Exception as e:
        print("Transaction error: ", e)
    
