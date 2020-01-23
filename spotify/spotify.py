import requests
import json
import spotipy
import spotipy.util as util
import os



#returns list with top artists and html picture
def top_artists(spotify_obj, amount, time):
    top_art_dict = spotify_obj.current_user_top_artists(amount, 0, time)

    art_list = top_art_dict.get('items')

    top_artists = []
    for art_dict in art_list:
        artist = art_dict.get('name')
        try:
            pic = art_dict.get('images')[0].get('url')
        except:
            pic = "None"
        top_artists.append([artist, pic])
    return top_artists


#gets top tracks and returns list of song, artists (as list), album picture, and song preview
def top_tracks(spotify_obj, amount, time):
    top_track_dict = spotify_obj.current_user_top_tracks(amount, 0, time)

    track_list = top_track_dict.get('items')

    top_tracks = []
    for track_dict in track_list:
        song = track_dict.get('name')
        pic = track_dict.get('album').get('images')[0].get('url')
        preview = track_dict.get('preview_url')
        artists = track_dict.get('artists')
        art_list = []
        for artist in artists:
            art_list.append(artist.get('name'))
        top_tracks.append([song, art_list, pic, preview])
    return top_tracks

def style_print(list_tup):
    for tup in list_tup:
        for i in tup:
            print(i)
        print('\n')


def format_top_artist_html(spotify_obj, time):
    top_art_list = top_artists(spotify_obj, 100, time)
    top_art_html = r'<table class="table table-striped table-dark" style="table-layout: fixed" >'

    num = 1
    for art in top_art_list:
        top_art_html += '<tr>'

        top_art_html += r'<td  class="numbering"> <div><h3 class="special">{}</h3></td>'.format(
            num)
        num += 1

        top_art_html += r'<td  class="results"> <div><img src="{}" alt="" ></img></div> <h4>{}</h4> </td>'.format(art[1], art[0])
        top_art_html += r'</tr>'
    top_art_html += r'</table>'

    return top_art_html

def format_top_tracks_html(spotify_obj, time):
    top_track_list = top_tracks(spotify_obj,100, time)
    top_track_html = r'<table class="table table-striped table-dark" style="table-layout: fixed">'

    num = 1
    for track in top_track_list:
        top_track_html += '<tr>'

        top_track_html += r'<td class="numbering"> <div><h3 class="even_special">{}</h3></td>'.format(
            num)
        num += 1

        artists_str = ''
        if len(track[1]) > 1:
            for art in track[1]:
                artists_str += art
                artists_str += ", "
        else:
            artists_str = track[1][0]

        top_track_html += r'<td class ="track_results"><img src="{}" alt=""><h4>{}</h4><h4 class="no_padding">{}</h4> <figure> <audio controls="controls" preload="auto" ><source src="{}" type="audio/mpeg"/> Your browser does not support the audio! </audio> </figure></td>'.format(track[2], track[0], artists_str, track[3],)


        top_track_html += r'</tr>'
    top_track_html += r'</table>'

    return top_track_html



def createHTMLFile(option, time, spotify_obj):

    if option == 'Artists':
        top_art_html = format_top_artist_html(spotify_obj, time)
    elif option == "Tracks":
        top_art_html = format_top_tracks_html(spotify_obj, time)


    filepath = '/home/cartealb/django_projects/aj_web/spotify/templates/spotify/spotify_user_list.html'
    f = open(filepath, 'w')

    logout_link = r'''{% url 'logout' %}?next={% url 'spotify:all' %}'''


    nav = '''<link rel="stylesheet"
  href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
  crossorigin="anonymous">

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
   crossorigin="anonymous"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
  crossorigin="anonymous"></script>

<script
  src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
  crossorigin="anonymous"></script>

<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/v4-shims.css">

  {% load static %}
  <link rel="shortcut icon" href="{%  static 'favicon.ico' %}">
<link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{% static 'css/html5reset.css' %}">
<link rel="stylesheet" href="{% static 'css/style2.css' %}">



<meta name="wa4e-version" value="2019-10:161EB">



<script type="text/javascript">
audiojs.events.ready(function() {
var ajso = audiojs.createAll();
var playPauseElems = [];
var audioJSes = document.getElementsByClassName("audiojs");
for(var i = 0;i < audioJSes.length;i++) {
    playPauseElems.push( audioJSes[i].getElementsByClassName('play-pause') );
}
for(var i = 0;i < playPauseElems.length;i++) {
    playPauseElems[i][0].addEventListener("click", function(event){ clickedPlayPause( event, ajso ); }, false );
}
});
function clickedPlayPause(event, ajso) {
    var currAudioJSwrapperID = event.target.parentNode.parentNode.id;
    var thisIndex = parseInt( currAudioJSwrapperID.substr(currAudioJSwrapperID.indexOf("audiojs_wrapper") + 15) );

    for(var i = 0;i < ajso.length;i++) {
        if ( i != thisIndex && ajso[i].playing ) ajso[i].pause();
    }

}
</script>




     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        {% load static %}
  <a style ="width:30%" class="navbar-brand" href="/"><img src="{% static 'images/spoti_stats_logo_hor.png' %}" id="logo" alt="Spoti Stats Logo"></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">


    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
      </li>

      <li class="nav-item dropdown" >
        <a class="nav-link dropdown-toggle" href="" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Top Artists
        </a>

        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <table>
            <tr>
            <td class="numbering">
                <div id="home_link_tabs">
          <a class="dropdown-item" href="long_term_artists">Long Term Artists</a>
          <a class="dropdown-item" href="medium_term_artists">Medium Term Artists</a>
          <!--<div class="dropdown-divider"></div> -->
          <a class="dropdown-item" href="short_term_artists">Short Term Artists</a>

        </div>
        </td>
        </tr>
        </table>

      </li>

      <li class="nav-item dropdown" >
        <a class="nav-link dropdown-toggle" href="" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Top Tracks
        </a>

        <table>
            <tr>
            <td class="numbering">
                <div id="home_link_tabs">

        <div class="dropdown-menu" aria-labelledby="navbarDropdown">

          <a class="dropdown-item" href="long_term_tracks">Long Term Tracks</a>



          <a class="dropdown-item" href="medium_term_tracks">Medium Term Tracks</a>



          <a class="dropdown-item" href="short_term_tracks">Short Term Tracks</a>



          </div>
          </td>
        </tr>
        </table>


      </li>


        <li class="nav-item active" >
                <a class="nav-link" href="{% url 'logout' %}?next={% url 'spotify:all' %}">Logout <span class="sr-only">(current)</span></a>
        </li>



    </ul>


  </div>





</nav>'''

    if time == "long_term":
            time_header_title = r'''<img src="{% static 'images/long_term_logo.png' %}" class="time_logo" alt="Long term">'''
    elif time == "medium_term":
        time_header_title = r'''<img src="{% static 'images/medium_term_logo.png' %}" class="time_logo" alt="Medium term">'''
    else:
        time_header_title = r'''<img src="{% static 'images/short_term_logo.png' %}" class="time_logo" alt="Short term">'''

    if option == 'Artists':
        type_header_title =r'''<img src="{% static 'images/your_top_artists_logo2.png' %}" class="type_logo" alt="Your Top Artists">'''
    else:
        type_header_title =r'''<img src="{% static 'images/your_top_tracks_logo2.png' %}" class="type_logo" alt="Your Top Tracks">'''

    full_header = type_header_title + time_header_title



    wrapper = r'''



    <!DOCTYPE html>
    <html lang="en">

    <head>

    <meta charset="UTF-8">
    <title>Your Music Stats</title>


    {}

    </head>
    <body>

            {}

    {}

    </body>

    <footer>

            <p>AJ Carter &copy; 2020</p>
            </footer>


    </html>
    '''.format(nav, full_header, top_art_html)

    f.write(wrapper)
    f.close()














    return wrapper