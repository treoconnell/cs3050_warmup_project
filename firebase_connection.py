import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseConnection:
    def __init__(self, db_id = "movies-remote", key_location = "firebase_key_PRIVATE.json"):
        cred = credentials.Certificate(key_location)                # generated as cs3050-warmup-e54d9-firebase-adminsdk-fbsvc-29129496a9.json
        firebase_admin.initialize_app(cred)                         # initialze the firebase app with credentials
        self.db = firestore.client(database_id = db_id)             # open the db for reading, kwarg database_id since the db has a name and is not `(default)`
    
    def clear_collection(self, collection_id = "movies"):
        self.db.recursive_delete(self.db.collection(collection_id)) # recursivly delete all documents from the collection, experimentally a noop for an empty collection

    def batch_write(self, document_list, collection_id = "movies"):
        batch = self.db.batch()                              # BATCH START
        for document_data in document_list:
            new_document = self.db.collection(collection_id).document()
            batch.set(new_document, document_data)    
        batch.commit()                                  # BATCH END