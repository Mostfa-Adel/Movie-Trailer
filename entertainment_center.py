import media
from tomatoes import fresh_tomatoes
# every list carry movie data, the first element in the list
# carry title of the movie, the second poster url and the third
# is youtube trailer url

avatar_data = ['Hulk',
               ('https://upload.wikimedia.org/wikipedia/en/8/88/The_'
                'Incredible_Hulk_poster.jpg'),
               'https://www.youtube.com/watch?v=xbqNb2PFKKA']

dispicable_me = ['Dispicable Me',
                 ('https://upload.wikimedia.org/wikipedia/en/d/db/'
                  'Despicable_Me_Poster.jpg'),
                 'https://www.youtube.com/watch?v=6DBi41reeF0']

dark_knight = ['Dark Knight',
               ('https://upload.wikimedia.org/wikipedia/en/8'
                '/8a/Dark_Knight.jpg'),
               'https://www.youtube.com/watch?v=EXeTwQWrcwY']

# movies_data list carry movies lists that will be passed to
# instantiate_movies class function, this function responsable
# for creating movie object for each list in movies_data,

movies_data = [avatar_data, dispicable_me, dark_knight]

# on instantiation the constructor adds the new object
# to class variable movies_list that will be used to be passed
# to open_movies_page function that responsable for opening
# the browser displaying our movies in their template

media.Movie.instantiate_movies(movies_data)

fresh_tomatoes.open_movies_page(media.Movie.movies_list)
