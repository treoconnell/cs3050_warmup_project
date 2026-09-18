# Take parsed command and query firebase
# Take output from query and create movie object
# Send movie object/objects to GUI for display

from firebase_connection import FirebaseConnection

class Movie:
    def __init__(self, title, rating, year, box_office=None):
        self.title = title
        self.rating = rating
        self.year = year
        self.box_office = box_office # optional

connection = FirebaseConnection()
shawshank = connection.get_by_title("The Shawshank Redemption")
print(shawshank)

m1 = Movie(shawshank[0]['title'], shawshank[0]['rating'], shawshank[0]['year'], shawshank[0]['box_office'])        
print(m1.title)

rating_test = connection.get_by_rating(9.1, '>')
for item in rating_test:
    print(item)