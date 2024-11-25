class SerializeData:

  @staticmethod
  def serialize_movie(movie):
    """Serialize and create html tag for each item"""
    output = ''
    output += f'<li>\n'
    output += f'<div class="movie">\n'

    if "movienotes" in movie:
        output += f'<a href={movie["imdbmovielink"]} target="_blank"><img class="movie-poster" src={movie["poster"]}/><div class ="hide" >{movie["movienotes"]}</div></a>\n'
    else:
        output += f'<a href={movie["imdbmovielink"]} target="_blank"><img class="movie-poster" src={movie["poster"]}/></a>\n'
    output += f'<div class="movie-title">{movie["title"]}</div>\n'
    output += f'<div class="movie-year">{movie["year"]}</div>\n'
    output += f'<div class="movie-year">IMDB-Rating:{movie["rating"]}</div>\n'
    output += '</div>\n'
    output += '</li>'
    return output


  @staticmethod
  def write_newhtml(result):
    """with new generate data it creates new html file"""
    with open("_static/index_template.html", "r") as handle:
        html_content = handle.read()

    html_content = html_content.replace("__TEMPLATE_MOVIE_GRID__", result)
    html_content = html_content.replace("__TEMPLATE_TITLE__", "My Favorite movies")

    with open("_static/movie_website.html", "w") as handle1:
        handle1.write(html_content)