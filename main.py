import tkinter
import customtkinter
from pytube import YouTube
import pytube.request

# Settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
pytube.request.default_range_size = 1024 * 1024 * 560 # BYTE

# TODO: fai repository

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("MP3 Downloader")

# Variables
url = tkinter.StringVar()
chunk_sizes = ["0.25MB", "0.5MB", "1MB", "9MB"]

# Functions
def updateChunkSize(size):
    chunk_size = 1024 * 1024 * float(size[0:-2])
    print(chunk_size) # TODO: continua funzione

def singleDownload():
    single_finish_label.configure(text="")
    single_finish_label.update()
    try:
        yt_link = single_link_entry.get()
        yt_object = YouTube(yt_link, on_progress_callback=singleProgress)
        audio = yt_object.streams.get_audio_only()
        audio.download(output_path="G:\\") # TODO: rendi settabile
        single_finish_label.configure(text=f"Downloaded - {yt_object.title}")
    except:
        single_finish_label.configure(text="Invalid link")

def singleProgress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded / total_size * 100
    print(percentage)
    single_progress_percentage.configure(text=f"{int(percentage)} %")
    single_progress_percentage.update()
    single_progress_bar.set(percentage/100)
    # single_progress_bar.update()

# UI Elements

# TODO: metti icona "?" che spiega come funziona (consigliato 9MB, ma più è alto ed è bassa la dimensione del file scaricato e più è a scatti la progress bar)
chunk_size_combobox = customtkinter.CTkComboBox(app, values=chunk_sizes, command=updateChunkSize)
chunk_size_combobox.set("0.5MB")
chunk_size_combobox.pack()
        
# - signle download
single_label = customtkinter.CTkLabel(app, text="Single Video URL:")
single_label.pack(padx=10)

single_link_entry = customtkinter.CTkEntry(app, width=350, textvariable=url) # TODO: eseguire funzione del tasto con Enter
single_link_entry.pack()

single_finish_label = customtkinter.CTkLabel(app, text="")
single_finish_label.pack()

single_progress_percentage = customtkinter.CTkLabel(app, text="0%")
single_progress_percentage.pack()

single_progress_bar = customtkinter.CTkProgressBar(app, width=400)
single_progress_bar.set(0)
single_progress_bar.pack()

single_download_button = customtkinter.CTkButton(app, text="Download", command=singleDownload)
single_download_button.pack(pady=10)

# - playlist download


# Run App
app.mainloop()