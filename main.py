from libraries import film, bibliothèque, friend

my_library = bibliothèque.Bibliothèque()
paul = friend.Friend('Paul')

blade = film.Film('Blade Runner', '1982', my_library, 'vhf')
alien = film.Film('Alien : Le 8ème Passager', '1979', my_library, 'vhf')
odysse = film.Film("2001 : L'Odyssée de l'espace", "1968", paul, "vhf")


my_library.add_movie(blade)
my_library.add_movie(alien)

my_library.display()