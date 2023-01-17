from pytube import YouTube

def dowloader(video_url):
    youtubeobject = YouTube(video_url)
    youtubeobject = youtubeobject.streams.get_highest_resolution()
    try:
        youtubeobject.download()
    except:
        print('Error, please insert normal address ')
    print('Video dowload')


video_url = input('Put your video here: ')
dowloader(video_url)
