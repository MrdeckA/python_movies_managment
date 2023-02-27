class Bibliothèque:
    def __init__(self):
        self.liste_films = []

    def add_movie(self, movie):
        """Ajouter un film a ma bibliotheque"""
        self.liste_films.append(movie)
        

    def trier_film(self, parametre):
        if parametre == 'nom': 
            print('Triage par nom de Filù')

        elif parametre == 'date':
            print('Triage par date de sortie')
            

        elif parametre == 'type':
            print('Triage par type du film')

        else:
            print('Erreur de parametre')


    def get_random_film():
        return 'Film au Hasard'
    

    def get_loan_movies():
        print('Liste des films prêtés')


    def display(self):
        for film in self.liste_films:
            print(f"Je possède {film.nom}")



    

