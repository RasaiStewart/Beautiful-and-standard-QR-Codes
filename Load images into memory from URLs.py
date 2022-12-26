from urllib.request import urlopen
import segno

beatle = segno.make('Ringo Starr', error='h')
url = 'https://media.giphy.com/media/HNo1tVKdFaoco/giphy.gif'
bg_file = urlopen(url)
beatle.to_artistic(background=bg_file, target='ringo.gif', scale=10)