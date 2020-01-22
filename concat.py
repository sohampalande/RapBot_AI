#concatenate the lyrics
import os
from pathlib import Path

ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent

data_folder = Path(ROOT_DIR, 'data')
artist_folders = os.listdir(data_folder)
 
training_data = []
#prepend all the lyrics with artist name and title
for artist_name in artist_folders:
    artist_folder = Path(data_folder, artist_name)
    if not os.path.isdir(artist_folder):
        continue
    text_files = os.listdir(artist_folder)
    for tf in text_files:
        with open(f'{artist_folder}/{tf}') as f:
            try:
                lines = [line for line in f.readlines()]
            except Exception:
                continue
            song_title = tf.split('.txt')[0]
            text = f'<<{artist_name} - {song_title}>>\n' + '\n'.join(lines)     #prepend lyrics with artist name and title
            training_data.append(text)                 #append lyrics to training data
            print(f'Songs added to training data: {len(training_data)}')
#join the lyrics with len 50 *** token into a single training file
join_string = f"\n{'*'*50}\n"
with open(Path(data_folder, 'rap_training_data.txt'), 'w') as f:
    f.write(join_string.join(training_data))