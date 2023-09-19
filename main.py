import pytube

video_url = input('What is the youtube link?: ')
yt = pytube.YouTube(video_url)

stream = yt.streams.get_highest_resolution()
print('Video is being downloaded...')
stream.download('Youtube Downloader/Video DL')
print('Your video is finished downloaded!')