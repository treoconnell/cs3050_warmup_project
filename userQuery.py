# Take parsed command and query firebase
# Take output from query and create movie object
# Send movie object/objects to GUI for display

from firebase_connection import FirebaseConnection

class Movie:
    def __init__(self, title, rating, year, box_office):
        self.title = title
        self.rating = rating
        self.year = year
        self.box_office = box_office

class Query:
    def __init__(self, parsed_dictionary, connection):
        conditions = parsed_dictionary['conditions'] # arguments
        connectors = parsed_dictionary['connectors'] # and/or

        c = conditions[0]
        results = connection.get_generic(c['field'], c['op'], c['value']) or []

        if connectors: 
            second_condition = conditions[1]
            second_results = connection.get_generic(
                second_condition['field'],
                second_condition['op'],
                second_condition['value'],
            ) or []

            first_titles = [movie['title'] for movie in results] # keep track of movies in first argument
            second_titles = [movie['title'] for movie in second_results] # second argumment

            if connectors[0] == "and":
                results = [movie for movie in results if movie['title'] in second_titles] # check movie title meets both conditions

            elif connectors[0] == "or":
                new_movies = [movie for movie in second_results if movie['title'] not in first_titles] # movies not already in results
                results = results + new_movies # add the movies on right side of or condition

        self.movieObjects = []
        for movie in results:
            rating = movie.get('rating')
            box_office = movie.get('box_office')

            rating = "N/A" if rating is None else f"{rating}/10" # Changed these form GUI to userQuery in case rating or box office is NA
            box_office = "N/A" if box_office is None else f"${box_office}M"

            self.movieObjects.append(Movie(movie.get('title'), rating, movie.get('year'), box_office))

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