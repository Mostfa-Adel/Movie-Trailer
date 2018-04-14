class Movie():
    """
    this class for  creating movie instance that has instance
    variables: 1.title, poster url, trailer url
    """

    # movies_list will carry every instance of this class
    movies_list = []

    # the constructor recieves three parameters assigning them to
    # their instance variables: title, poster url, trailer url
    # insert_self_to_list() class function inserts every instance
    # to movies_list
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        Movie.insert_self_into_list(self)

    # when instantiate, add instance to movies_list
    def insert_self_into_list(self):
        self.movies_list.append(self)

    # this function recieves a list of movies data lists creating
    # instance of Movie class foreach list
    # considering the arrengment in every list 1.title,
    # 2.img url, 3.trailer url
    def instantiate_movies(movies_data):
        for movie in movies_data:
            Movie(movie[0], movie[1], movie[2])
