

import media
import fresh_tomatoes


#This is where we defined our movies, and there attributes.

wreckItRalph = media.Movie("Wreck-It Ralph", "A person who wrecks stuff feels bad about it",
                                 "http://cdn.collider.com/wp-content/uploads/wreck-it-ralph-poster-main-characters.jpg",
                                 "https://www.youtube.com/watch?v=87E6N7ToCxs")


johnWick = media.Movie("John Wick", "A person killed his dog so he will kill 76 people.",
                             "https://static1.squarespace.com/static/54aea10fe4b06532c83ba3f3/58336afde6f2e174305a4ee7/58336b18e6f2e174305a50b3/1479764772187/john-wick-54716f3d6a2c0.jpg",
                             "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")


howToTrainYourDragon = media.Movie("How to Train Your Dragon",
                                   "A boy trains a dragon.",
                                   "https://cityofcs.files.wordpress.com/2015/02/how-to-train-your-dragon-poster-11.jpg",
                                   "https://www.youtube.com/watch?v=oKiYuIsPxYk")


deadPool = media.Movie("DeadPool", "A mercenary with a mouth",
                             "https://s-media-cache-ak0.pinimg.com/originals/9c/c2/c1/9cc2c190f86819cfaeb26755482fc6a5.jpg",
                             "https://www.youtube.com/watch?v=ONHBaC-pfsk")


socialNetwork = media.Movie("Social Network",
                                 "A college freshman makes a program that revolutionizes the social network",
                                 "https://b1.filmpro.ru/c/436958.660xp.jpg",
                                 "https://www.youtube.com/watch?v=lB95KLmpLR4")

logan = media.Movie("Logan", "The wolverine goes on a killing spree.",
                          "https://s3.amazonaws.com/cgimg/t/g86/613386/1723155_large.jpg",
                          "https://www.youtube.com/watch?v=Div0iP65aZo")


#List of movies that we just defined

movies = [wreckItRalph, johnWick, howToTrainYourDragon, deadPool, socialNetwork, logan]
#Call on Fresh_tomatoes to run the HTML code.
fresh_tomatoes.open_movies_page(movies)
