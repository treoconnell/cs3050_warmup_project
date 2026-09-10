import firebase_admin
from firebase_admin import credentials, firestore
import json
import sys




def batch_commit_to_db(document_list, db_id="movies-remote", collection_id="movies"):
    cred = credentials.Certificate("firebase_key_PRIVATE.json") # generated as cs3050-warmup-e54d9-firebase-adminsdk-fbsvc-29129496a9.json
    firebase_admin.initialize_app(cred)                         # initialze the firebase app with credentials

    db = firestore.client(database_id=db_id)        # open the db for reading, kwarg database_id since the db has a name and is not `(default)`
    collection_ref = db.collection(collection_id)   # reference to the `movies` collection 

    db.recursive_delete(collection_ref)             # recursivly delete all documents from the collection, experimentally a noop for an empty collection

    # batch the writes so it doesn't take forever (since this is syncronous and not using the async framework, each of the 100-odd writes would be a transaction)
    # notably still has the per-read/write cost, just quicker to send the data
    batch = db.batch()                              # BATCH START
    for document_data in document_list:
            new_document = collection_ref.document()
            batch.set(new_document, document_data)    
    batch.commit()                                  # BATCH END

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Too few arguments, expected `python admin.py /path/to/data.json`")
    if len(sys.argv) > 2:
        print("Too many arguments, expected `python admin.py /path/to/data.json`")

    movies = []

    try: 
        with open(sys.argv[1]) as f:
            movies = json.load(f)
    except IOError as e:
        print("I/O error: ", e.strerror)
    
    try:
        batch_commit_to_db(movies)
    except Exception as e:
        print("Transaction error: ", e.strerror)
    
