import media 
import fresh_tomatoes

# listed below are a list of instances of the Movie class located in media.py 
# These instances are then put into a list which will be used to call a method 'open_movies_page' located in fresh_tomatoes.py

toy_story = media.Movie("Toy Story", "A story of aboy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
	"https://www.youtube.com/watch?v=JcpWXaA2qeg")

avatar = media.Movie("Avatar", "A marine on an alien planet", 
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
	"https://www.youtube.com/watch?v=6ziBFh3V1aM")

john_wick = media.Movie("John Wick", "A man out for revenge for the death of his dog", 
	"https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
	"https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

school_of_rock = media.Movie("School of rock", "Using rock to learn", 
	"https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
	"https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "About a rat chef in paris", 
	"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", 
	"https://www.youtube.com/watch?v=c3sBBRxDAqk&t=7s")

midnight_in_paris= media.Movie("Midnight in Paris", "Going back in time to meet authors",
	"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", 
	"https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games= media.Movie("Hunger Games", "A really real realty show",
	"https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg", 
	"https://www.youtube.com/watch?v=mfmrPu43DF8")

black_panther = media.Movie("Black Panther", "About a superhero from the African nation of Wakanda",
	"https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
	"https://www.youtube.com/watch?v=fsT5SyBLlIg")

avengers_infinty_war = media.Movie("Avengers: Infinity War", "A group of superheroes on a quest to save the world",
	"https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
	"https://www.youtube.com/watch?v=B65hW9YYY5A")

#Adding all the instances of the movie class into a single list as required by the method 'open_movies_page'
movies= [toy_story, avatar, john_wick,school_of_rock,ratatouille,midnight_in_paris,hunger_games, black_panther, avengers_infinty_war]

# calling the method 'open_movies_page' in order to create the webpage.
fresh_tomatoes.open_movies_page(movies)

