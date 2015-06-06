# website.py
# Created by: Vineeta Gupta
# Date: 5 June 2015
# Purpouse: This file is for instantiating all the movie objects and then
# call display_page.py to render the movies in an html page

import display_page
import movie

# Creating objects for my favourite movie
cars = movie.Movie(
    "Cars",
    "Story about live cars",
    "2006",
    "Pixar Animation Studios",
    "Walt Disney Pictures",
    "John Lasseter",
    "Golden Globe Award for Best Animated Feature Film",
    "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
    "https://www.youtube.com/watch?v=WGByijP0Leo"
    )
ratatouille = movie.Movie(
    "Ratatouille",
    "Anybody can cook",
    "2007",
    "Pixar Animation Studios",
    "Walt Disney Pictures",
    "Brad Bird",
    "Academy Award for Best Animated Feature",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk"
    )
tangled = movie.Movie(
    "Tangled",
    "Girl with long golden red hairs",
    "2010",
    "Walt Disney Animation Studios",
    "Walt Disney Pictures",
    "Nathan Greno & Byron Howard",
    "Best Original Song at the 83rd Academy Awards",
    "https://upload.wikimedia.org/wikipedia/en/a/a8/Tangled_poster.jpg",
    "https://www.youtube.com/watch?v=pyOyBVXDJ9Q"
    )
brave = movie.Movie(
    "Brave",
    "Girl with lot of courage",
    "2012",
    "Pixar Animation Studios",
    "Walt Disney Pictures",
    "Mark Andrews and Brenda Chapman",
    "Academy Award,the Golden Globe,and the BAFTA Award for Best \
    Animated Feature Film.",
    "https://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg",
    "https://www.youtube.com/watch?v=6CKcqIahedc"
    )
# Create an arrary of all my favourite movies
movies_list = [cars, ratatouille, tangled, brave]
# Call another python script to render the movies on an html page
display_page.open_movies_page(movies_list)

# EOF
