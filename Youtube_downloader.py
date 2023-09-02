from tkinter import ttk
from tkinter import*
from pytube import YouTube
from tkinter.messagebox import showinfo, showerror,askokcancel
from tkinter import filedialog
import threading

root = Tk()
root.geometry("520x300")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="Peach puff")


def Download():
	try:
		Youtube_link=video_Link.get()
		resolution="360p"
		resolution=resolution_var.get()
		download_folder=download_Path.get()
		if Youtube_link=="":
			showerror(title='Error',message="Please Insert the youtube link !!")
		elif download_folder=="":
			showerror(title='Error',message="Please choose the folder to save your video")
		else:
			try:
				def on_progress(stream, chunk, bytes_remaining):
					total_size=stream.filesize
					def get_formatted_size(total_size, factor=1024, suffix='B'):
						for unit in ["","K","M","G","T","P","E","Z"]:
							if total_size < factor:
								return f"{total_size:.2f}{unit}{suffix}"
							total_size /= factor
						return f"{total_size:.2f}Y{suffix}"

					formatted_size=get_formatted_size(total_size)
					bytes_downloaded=total_size-bytes_remaining
					percentage_completed=round((bytes_downloaded/total_size)*100)
					progress_bar['value']=percentage_completed
					progress_label.config(text=str(percentage_completed)+"%,file size"+formatted_size)
					root.update_idletasks()

				video=YouTube(Youtube_link,on_progress_callback=on_progress)
				video.streams.filter(res=resolution,file_extension='Mp4').first().download(download_folder)
				showinfo(title='Download Complete',message='Video has been Dowloaded succesfully')
				progress_label.config(text='')
				progress_bar['value']=0

			except:
			  	showerror(title="Download Error",message="Failed to download video for this resolution")
			  	progress_label.config(text='')
			  	progress_bar['value']=0
	except:
	 	showerror(title='Download Error',message="An error ocurred while trying to download the video The following could be the couse:\n"
	 				'->Invalid link\n'
	 				'->No internet connection\n'
	 				'make sure you have stable internet connection and the video link is valid')
	 	progress_label.config(text="")
	 	progress_bar['value']=0

def downloadThread():
    t2 = threading.Thread(target=Download)
    t2.start()

def Browse():
	download_Directory = filedialog.askdirectory(
		initialdir="YOUR DIRECTORY PATH", title="Save Video")
	download_Path.set(download_Directory)

video_Link = StringVar()
download_Path = StringVar()

head_label = Label(root, text="YouTube Video Downloader ",
					padx=15,
					pady=15,
					font="Stencil",
					bg="peach puff",
					fg="red")
head_label.grid(row=1,
					column=1,
					pady=10,
					padx=5,
					columnspan=3)

link_label = Label(root,
					text="YouTube link :",
					bg="salmon",
					pady=5,
					padx=5)
link_label.grid(row=2,
					column=0,
					pady=5,
					padx=5)

root.linkText = Entry(root,
						width=35,
						textvariable=video_Link,
						font="Arial 14")
root.linkText.grid(row=2,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)


destination_label = Label(root,
							text="Destination :",
							bg="salmon",
							pady=5,
							padx=9)
destination_label.grid(row=3,
						column=0,
						pady=5,
						padx=5)


root.destinationText = Entry(root,
								width=27,
								textvariable=download_Path,
								font="Arial 14")
root.destinationText.grid(row=3,
							column=1,
							pady=5,
							padx=5)


browse_B = Button(root,
				text="Browse",
					command=Browse,
					width=10,
					bg="bisque",
					relief=GROOVE)
browse_B.grid(row=3,
				column=2,
				pady=1,
				padx=1)

resolution_var=StringVar(root)
resolution_var.set("360p")
resolution_menu=OptionMenu(root, resolution_var, "144p","240p","360p","480p","720p","1080p")
resolution_menu.grid(row=4,column=1)

Download_B = Button(root,
						text="Download Video",
						command=downloadThread,
						width=15,
						bg="thistle1",
						pady=5,
						padx=15,
						relief=GROOVE,
						font="Georgia, 13")
Download_B.grid(row=5,
					column=1,
					pady=10,
					padx=20)

progress_label = Label(root, text="")
progress_label.grid(row=6,column=1)
progress_bar=ttk.Progressbar(root,orient='horizontal',length=300,mode='determinate')
progress_bar.grid(row=7,column=1)

root.mainloop()
