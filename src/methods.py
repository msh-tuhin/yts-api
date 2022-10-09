def fulldata(file, movies):
    with open(file, "w") as f:
        for movie in movies:
            for key in list(movie.keys()):
                f.write(key + '     :   ' + str(movie[key]) + "\n")
            f.write("\n\n-----------------------------------------\n\n")

def titlesonly(file, movies):
    with open(file, "w") as f:
        for movie in movies:
            f.write(movie['title'] + "\n")
            f.write("\n\n-----------------------------------------\n\n")

def getdata(file, movies, fields=['title']):
    with open(file, "w") as f:
        for movie in movies:
            for field in fields:
                if field not in list(movie.keys()):
                    continue
                f.write(field + "  :  " + str(movie[field]) + "\n")
            f.write("\n\n-----------------------------------------\n\n")
