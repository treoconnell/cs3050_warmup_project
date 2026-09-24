import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from google.cloud.firestore_v1.base_document import DocumentSnapshot

class FirebaseConnection:
    def __init__(self, db_id = "movies-remote", key_location = "firebase_key_PRIVATE.json"):
        cred = credentials.Certificate(key_location)                # generated as cs3050-warmup-e54d9-firebase-adminsdk-fbsvc-29129496a9.json
        firebase_admin.initialize_app(cred)                         # initialze the firebase app with credentials
        self.db = firestore.client(database_id = db_id)             # open the db for reading, kwarg database_id since the db has a name and is not `(default)`
    
    def clear_collection(self, collection_id = "movies"):
        self.db.recursive_delete(self.db.collection(collection_id)) # recursivly delete all documents from the collection, experimentally a noop for an empty collection

    def convert_float(self, string): # created convert float to catch any errors when converting rating string to float; some items dont have rating field
        try:
            return float(string)
        except (ValueError, TypeError):
            return None

    def convert_int(self, string):
        try:
            return int(string)
        except (ValueError, TypeError):
            return None

    def batch_write(self, document_list, collection_id = "movies"):
        batch = self.db.batch()                              # BATCH START

        for document_data in document_list:
            new_document = self.db.collection(collection_id).document()
            batch.set(new_document, document_data)    

            batch.set(new_document, {**document_data, 
            "rating": self.convert_float((document_data.get("rating"))),
            "box_office": self.convert_float((document_data.get("box_office"))),
            "year": self.convert_int((document_data.get("year")))
            }) # needed to convert to correct types to use operands
           

        batch.commit()                                  # BATCH END

    def get_by_title(self, movie_title, collection_id = "movies"):
        query = self.db.collection(collection_id).where(filter=FieldFilter("title", "==", movie_title))

        movie_items = [{**doc.to_dict()} for doc in query.stream()]

        if not movie_items:
            return None  

        return movie_items

    def get_by_rating(self, movie_rating, operator, collection_id = "movies"):
        query = self.db.collection(collection_id).where(filter=FieldFilter("rating", operator, movie_rating))
        movie_items = [{**doc.to_dict()} for doc in query.stream()]

        if not movie_items:
            return None  

        return movie_items

    
    def get_by_year(self, movie_year, operator, collection_id = "movies"):
        query = self.db.collection(collection_id).where(filter=FieldFilter("year", operator, movie_year))
        movie_items = [{**doc.to_dict()} for doc in query.stream()]

        if not movie_items:
            return None  

        return movie_items

    def get_by_box_office(self, movie_box_office, operator, collection_id = "movies"):
        query = self.db.collection(collection_id).where(filter=FieldFilter("box_office", operator, movie_box_office))
        movie_items = [{**doc.to_dict()} for doc in query.stream()]

        if not movie_items:
            return None  

        return movie_items




        