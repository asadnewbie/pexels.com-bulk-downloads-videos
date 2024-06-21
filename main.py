import pexelsPy
import requests
from tqdm import tqdm

# Replace 'YOUR_API_KEY_HERE' with your actual Pexels API key
PEXELS_API = '4v8RhU2jRdMdWqzgmy58sHrA1GbbrtfgSDVXtOviJZ25XjIXvRgq1zl5'
api = pexelsPy.API(PEXELS_API)

pageNumbers = 1 
resultsPage = 2 

api.search_videos('mountains', page=pageNumbers, results_per_page=resultsPage)
videos = api.get_videos()

for data in tqdm(videos, desc='Downloading videos'):
    video_url = data.video_files[-1]['link']  # Get the highest quality video file
    filename = f"{data.id}.mp4"
    
    # Download the video file with progress bar
    with requests.get(video_url, stream=True) as r:
        total_size = int(r.headers.get('content-length', 0))
        with open(filename, 'wb') as f, tqdm(
                total=total_size, unit='B', unit_scale=True, desc=filename, initial=0, miniters=1) as bar:
            for data in r.iter_content(chunk_size=1024):
                size = f.write(data)
                bar.update(size)

    
