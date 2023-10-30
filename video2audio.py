from pytube import YouTube
import os

def main():
    video_url = input('Enter YouTube video URL: ')

    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    location = stream.download(output_path=path)
    renametomp3 = path + yt.title + '.mp3'

    if os.name == 'nt':
        os.system('ren "{0}" "{1}"'.format(location, renametomp3))
    else:
        os.system('mv "{0}" "{1}"'.format(location, renametomp3))

if __name__ == '__main__':
    main()
