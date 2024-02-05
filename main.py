import tkinter
import customtkinter
from pytube import YouTube
import pytube.request
import time


# Settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
# pytube.request.default_range_size = 1024 * 0.5 # BYTE

# TODO: (opzioni (es. output path) salvate in un file di testo?)


# App frame
window = customtkinter.CTk()
window.geometry("720x480")
window.title("MP3 Downloader")


# Variables
url = tkinter.StringVar()
chunk_sizes = ["0.25MB", "0.5MB", "1MB", "9MB"]


# Functions
def updateChunkSize(size):
    chunk_size = 1024 * float(size[0:-2])
    # pytube.request.default_range_size = chunk_size
    print(pytube.request.default_range_size)

def download():
    download_finish_label.configure(text="")
    download_finish_label.update()
    # TODO: riattiva try and catch
    # try:
    yt_link = download_link_entry.get()
    yt_object = YouTube(yt_link, on_progress_callback=downloadProgress, on_complete_callback=lambda stream, path: downloadCompleted(start))
    audio = yt_object.streams.get_audio_only()
    start = time.time()
    audio.download(output_path="G:\\")
    download_finish_label.configure(text=f"Downloaded - {yt_object.title}")
    # except:
    #     download_finish_label.configure(text="Invalid link")
    download_finish_label.update()

def downloadProgress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded / total_size * 100
    single_progress_percentage.configure(text=f"{percentage:.2f} %")
    single_progress_percentage.update()
    single_progress_bar.set(percentage/100)
    # single_progress_bar.update()

def downloadCompleted(start):
    print("end")
    end = time.time()
    duration_label.configure(text=f"Last download duration: {(end - start):.2}s")
    duration_label.update()


# UI Elements
top_frame = customtkinter.CTkFrame(window)
option_section = customtkinter.CTkFrame(top_frame, corner_radius=0, fg_color="#2b2b2b")
info_section = customtkinter.CTkFrame(top_frame, corner_radius=0, fg_color="#2b2b2b")
main_frame= customtkinter.CTkFrame(window)

# - Options section
chunk_size_label = customtkinter.CTkLabel(option_section, text="Chunk size:")

# TODO: metti icona "?" che spiega come funziona (consigliato 9MB, ma più è alto ed è bassa la dimensione del file scaricato e più è a scatti la progress bar)
chunk_size_combobox = customtkinter.CTkComboBox(option_section, values=chunk_sizes, command=updateChunkSize)
chunk_size_combobox.set("0.5MB")

# - Info section
duration_label = customtkinter.CTkLabel(info_section, text="Last download duration: 0s") # TODO: metti durata


# TODO: metti output path selection
        
# - Download section
download_label = customtkinter.CTkLabel(main_frame, text="Video URL:")

download_link_entry = customtkinter.CTkEntry(main_frame, width=350, textvariable=url)

download_finish_label = customtkinter.CTkLabel(main_frame, text="")

single_progress_percentage = customtkinter.CTkLabel(main_frame, text="0%")

single_progress_bar = customtkinter.CTkProgressBar(main_frame, width=400)
single_progress_bar.set(0)

single_download_button = customtkinter.CTkButton(main_frame, text="Download", command=download)


# Layout
# - Top
top_frame.columnconfigure(0, weight=2)
top_frame.columnconfigure(1, weight=1)
top_frame.rowconfigure(0, weight=1)
top_frame.pack(fill="both")

option_section.grid(row=0, column=0, sticky="nesw", padx=10)
info_section.grid(row=0, column=1, sticky="nesw")
# option_section.pack(side="left", anchor="nw", fill="both", expand=True)
# info_section.pack(side="right", anchor="ne", fill="both", expand=True)

chunk_size_label.pack(anchor="w")
chunk_size_combobox.pack(anchor="w")

duration_label.pack(anchor="nw")

# - Main
main_frame.pack(fill="both", expand=True)
download_label.pack()
download_link_entry.pack()
download_finish_label.pack()
single_progress_percentage.pack()
single_progress_bar.pack()
single_download_button.pack()


# Run App
window.mainloop()