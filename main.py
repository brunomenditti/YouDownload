import tkinter
import customtkinter
from pytube import YouTube
from tkinter import PhotoImage
import os

# Criando a pasta Downloads
download_directory = 'downloads'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)




def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        video.download(output_path=download_directory)
        video.download(output_path='downloads')
        finishLabel.configure(text="Downloaded!", text_color="white")
    except:
        finishLabel.configure(text="Download Error!", text_color="red")
    

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completion) / 100)

# System Settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

#Our app frame
app = customtkinter.CTk()
app.geometry("480x240")
app.resizable(False, False)
app.title("Youtube Video Downloader 1.0")
app.iconbitmap('youtube.ico')


# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insira o link...")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)



#Run app
app.mainloop()