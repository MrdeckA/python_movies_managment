class Friend:
    def __init__(self, name):
        self.name=name
        self.film_pretes = []


    def do_you_own(self, film):
        return "Non je n'ai rien de toi"
    

    def loan_movie(self, movie):
        self.film_pretes.append(movie)
        print(f"Moi {self.name} atteste que tu m'a preté {movie.name}")
