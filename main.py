import re  # re-regular expression used to check for valid YouTube link
from pytube import YouTube  # pytube used to download video from YouTube


def on_progress(stream, chunk, bytes_remaining):
    """
    This function must takes 3 arguments, and display the progress of video in percentage.

    :param stream: object
    :param chunk: int
    :param bytes_remaining: int
    """

    # Get file_size using stream object
    file_size = stream.filesize
    # Gets the percentage of the file that has been downloaded.
    percent = (100 * (file_size - bytes_remaining)) / file_size
    # Displaying percentage
    print("{:00.0f}% downloaded".format(percent))


def check_youtube_link(link: str):
    """
    This function check whether the given link is a valid YouTube link or not.

    :param link: string
    :return: None or RE object
    """

    # Return None in case of invalid link
    return re.match("^https://www.youtube.com/.", link)


def download_video(link: str, path: str, choice: int):
    """
    This function take 3 arguments, and download the required video.
    :param link: string
    :param path: string
    :param choice: integer
    """

    # Making YouTube class object, display also the progress bar using on_progress function
    yt = YouTube(link, on_progress_callback=on_progress)
    stream = ""
    # Ask user about video format
    if choice == 1:  # Audio format
        stream = yt.streams.filter(only_audio=True).first()
    elif choice == 2:  # Video format
        stream = yt.streams.filter(file_extension="mp4").first()
    # Download the video and save it on given path
    path = stream.download(output_path=path)
    # display the final path where video has been saved!.
    print("Your video downloaded here: ", path)


def main():
    """
    A main function that control the main logic
    :return:
    """

    # Ask YouTube link from user
    youtube_link: str = input("Enter youtube link:\n")
    # check if YouTube link is valid
    if not check_youtube_link(youtube_link):
        print("Invalid Youtube Link")
        return
    # Ask for the directory to where video should be saved.
    path: str = input("Enter Directory Path:\n")
    # Ask user about video format, [Audio or Video]
    choice: int = int(input("Enter video type:\n1.Audio\n2.Video\n"))
    # Call the download function in last.
    download_video(youtube_link, path, choice)


# Main module
if __name__ == "__main__":
    # calling main function
    main()
