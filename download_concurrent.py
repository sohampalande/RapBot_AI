import concurrent.futures
from genius import Genius
from pathlib import Path
import os
import sys
genius=Genius(sys.argv[1])
ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent
rappers = open(Path(ROOT_DIR, 'data', 'rappers.txt')).read().splitlines()
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
    executor.map(genius.scrape_artist, rappers)