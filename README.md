# usage:
- just run center_entertainment.py python file then browser will be opened with your lovely movies :)

## Add A Movie

in center_entertainment.py file make a a list for your movie data
this list will contain three elements: 1.title, 2.poster url 3.youtube trailer url 
and add this list to movies_data list


##more details
###center_entertainment.py:

just create a list of your movie data ['title','poster url','youtube trailer url']
add this list to `movies_data` list
`movies_data` list is passed to class function `instantiate_movies()` that will instantiate
a move instance foreach list in `movies_data` list
as instance instantiated, the instance will be inserted to `movies_list` class variable
`movies_list` class variable will be passed to `open_movies_page()`
`open_movies_page()` function recieves one parameter a list of `Movie` instances
it opens the browser displaying the movies in a template that written in fresh_tomatoes module

###media module:
in media module you will find movie class that has string attributes: 
1. title 
2. poster_url
3. movie_url
they recieves thier values by the constructor
in constructor the class function `insert_self_into_list()` is called it just
add the new instance to movies_list class variable

`instantiate_movies()` class function creates movie instances by a parameter 
a list of movies data lists 


### fresh_tomatoes:
this module provides ** `open_movies_page()` ** function that recieves one parameter 
a list of instances of movie class, it opens the browser displaying your 
favourite movies in html page



