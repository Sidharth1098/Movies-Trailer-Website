# stores details of movies and displays them on website.
import fresh_tomatoes
import media

# Creating various instances for the class movie
ramleela = media.Movie(
        "Ramleela",
        """Ram and Leela, passionately in love with each other,
        realize that the only way to stop the bloodshed between
        their respective clans, Rajari and Sanera, is to sacrifice
        their own lives.""",
        "ramleela.jpg",
        "https://www.youtube.com/watch?v=StphRCLkx6Q")

yeh_jawani_hai_deewani = media.Movie(
                   "Yeh Jawani Hai Deewani",
                   """Kabir and Naina bond during a trekking trip. Before Naina
                   can express herself, Kabir leaves India to pursue his career
                   They meet again years later, but he still cherishes his
                   dreams more than bonds.""",
                   "yjhd.jpg",
                   "https://www.youtube.com/watch?v=Rbp2XUSeUNE")

padmavat = media.Movie(
                   "Padmavat",
                   """She was a woman of unprecedented beauty. And the 'Johar
                   Kund' in Chittorgarh where Rani Padmavati performed 'jauhar'
                   (custom of self-immolation by women) more than seven hundred
                   years ago is a place as significant as, the Western Wall or
                   the Ka'bah in Mecca.""",
                   "padmavat.jpg",
                   "https://www.youtube.com/watch?v=8YaF2m7hCx0")

rangroot = media.Movie(
                "Sajjan Singh Rangroot",
                """This film is based on Sikh regiments that went to the front
                lines during WWI.""",
                "rangroot.jpg",
                "https://www.youtube.com/watch?v=n7YddfDo4N0")

bahubali_2 = media.Movie(
                   "Bahubali 2:The Conclusion",
                   """When Bhallaladeva conspires against his brother to become
                   the king of Mahishmati, he has him killed by Katappa and
                   imprisons his wife. Years later, his brother's son returns
                   to avenge his father's death.""",
                   "bahubali.jpg",
                   "https://www.youtube.com/watch?v=G62HrubdD6o")

annabelle = media.Movie(
                   "Annabelle:Creation",
                   """Former toy maker Sam Mullins and his wife, Esther, are
                   happy to welcome a nun and six orphaned girls into their
                   California farmhouse. Years earlier, the couple's 7-year-old
                   daughter Annabelle died in a tragic car accident. Terror
                   strikes when one child sneaks into a forbidden room and find
                   a seemingly innocent doll that appears to have a life of its
                   own.""",
                   "annabelle.jpg",
                   "https://www.youtube.com/watch?v=KisPhy7T__Q")

# Creating an array called movies
movies = [
    ramleela, yeh_jawani_hai_deewani, padmavat, rangroot, bahubali_2,
    annabelle]

# using the python fresh tomatoes for opening our website.
fresh_tomatoes.open_movies_page(movies)

