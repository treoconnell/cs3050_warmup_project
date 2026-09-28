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

class Query:
    def __init__(self, parsed_dictionary, connection):
        cond = parsed_dictionary['conditions'][0]
        movies = connection.get_generic(cond['field'], cond['op'], cond['value'])

        self.movieObjects = []
        for movie in movies or []:
            self.movieObjects.append(Movie(
                movie.get('title'),
                movie.get('rating'),
                movie.get('year'),
                movie.get('box_office'),
            ))

    def get_movies(self):
        return self.movieObjects
        
# connection = FirebaseConnection()
# m1 = connection.get_generic("Rating", ">", 9.0)
# print(m1)

""" 
shawshank = connection.get_by_title("The Shawshank Redemption")
print(shawshank)

m1 = Movie(shawshank[0]['title'], shawshank[0]['rating'], shawshank[0]['year'], shawshank[0]['box_office'])        
print(m1.title)

rating_test = connection.get_by_rating(9.0, '>')
print("By rating:")
for item in rating_test:
    print(item)

year_test = connection.get_by_year(1950, '<=')
print("By year:")
for item in year_test:
    print(item)

box_office_test = connection.get_by_box_office(400.0, '>=')
print("By box office:")
for item in box_office_test:
    print(item)
 """