import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import yt_video_downloader as yt
import os
import time
import threading
import sys

class Application(tk.Frame):
    """
    PY YT Downloader application.

    Download a Youtube video or videos from a YT Playlist.
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """
        Create all application widgets.
        """

        # Change top-level window title
        self.winfo_toplevel().title("PY YT Downloader 1.0")

        # # Add main frame
        self.frm_main = ttk.Frame()
        self.frm_main.pack()


        #Add URL frame and widgets
        self.frm_inner_url_widgets = ttk.Frame(self.frm_main)

        self.lbl_yt_url = ttk.Label(self.frm_inner_url_widgets, text="Add Youtube video URL", anchor=tk.E)
        self.lbl_yt_url.pack(side=tk.LEFT, padx=5)

        self.etr_yt_url = ttk.Entry(self.frm_inner_url_widgets, width=100)
        self.etr_yt_url.pack(side=tk.LEFT, fill=tk.X)

        self.frm_inner_url_widgets.pack(padx=5, pady=5)


        # Add directory frame and widgets
        self.frm_inner_dir_widgets = ttk.Frame(self.frm_main)

        self.lbl_save_in_frm_yt_download = ttk.Label(self.frm_inner_dir_widgets, text="Save in", anchor=tk.E)
        self.lbl_save_in_frm_yt_download.pack(side=tk.LEFT, padx=5)

        self.icon = tk.PhotoImage(file=self.resource_path(r"icons\folder-24px.png"), width=15, height=15)

        self.btn_ask_dir = ttk.Button(self.frm_inner_dir_widgets, command=self.set_etr_download_dir_path_frm_yt_download, image=self.icon)
        self.btn_ask_dir.pack(side=tk.LEFT, fill=tk.X, anchor=tk.W)

        self.etr_download_dir_path_frm_yt_download = ttk.Entry(self.frm_inner_dir_widgets, width=100)
        self.etr_download_dir_path_frm_yt_download.insert(0, "Enter directory absolute path.")
        self.etr_download_dir_path_frm_yt_download.bind("<Button-1>", func=self.set_etr_download_dir_path_frm_yt_download_via_mouse_b1_event)
        self.etr_download_dir_path_frm_yt_download.pack(side=tk.LEFT, fill=tk.X)
        self.frm_inner_dir_widgets.pack(padx=5, pady=5)


        # Add download frame and widgets
        self.frm_inner_download_widgets = ttk.Frame(self.frm_main)

        self.btn_download_video = ttk.Button(self.frm_inner_download_widgets, text="Download video", 
                    command=self.btn_download_video_command)
        self.btn_download_video.pack()

        self.pbar_download_pbar = ttk.Progressbar(self.frm_inner_download_widgets, mode="indeterminate", length=200)
        self.pbar_download_pbar.pack(pady=6, fill=tk.X)

        self.frm_inner_download_widgets.pack(padx=5, pady=3)


        # Add status bar to master widget
        self.status_bar = ttk.Label(self.master, relief=tk.SUNKEN, anchor=tk.W, text="Ready to work...")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    

    def start_progress_bar(self):
        """
        Start the indeterminate progress bar.
        """
        self.pbar_download_pbar.start()
    
    def stop_progress_bar(self):
        """
        Stop the indeterminate progress bar.
        """
        self.pbar_download_pbar.stop()
        self.pbar_download_pbar.update()

    def wrapper_download_yt_video(self):
        """
        Call Youtube video downloader method from imported package.

        Gets parameters from entries and send them to the method. Downloads highest resolution possible by default.
        """

        # Disable button to prevent multiple calls
        self.btn_download_video["state"] = tk.DISABLED
        self.btn_download_video.update()

        # Progress bar handled by independent thread
        start_pbar = threading.Thread(target=self.start_progress_bar)
        start_pbar.start()


        try:
            url = self.etr_yt_url.get()
            dir_path = self.etr_download_dir_path_frm_yt_download.get()
            yt.download_yt_video(url, dir_path)
        except(FileNotFoundError):
            self.status_bar["text"] = "Invalid directory path."
            self.status_bar.update()
        except:
            self.status_bar["text"] = sys.exc_info()[1]
            self.status_bar.update()
        else:
            self.status_bar["text"] = "Download complete!"
            self.status_bar.update()
        finally:
            # Progress bar handled by independent thread
            stop_pbar = threading.Thread(target=self.stop_progress_bar)
            stop_pbar.start()

            time.sleep(2)

            self.status_bar["text"] = "Ready to work..."
            self.status_bar.update()

            # Reenable button
            self.btn_download_video["state"] = tk.NORMAL
            self.btn_download_video.update()
    
    def btn_download_video_command(self):
        """
        Update GUI and download video.
        """
        self.status_bar["text"] = "Attempting download, please wait..."
        self.status_bar.update()       

        download_task = threading.Thread(target=self.wrapper_download_yt_video)
        download_task.start()



    def set_etr_download_dir_path_frm_yt_download(self):
        """
        Set etr_download_dir_path_frm_yt_download variable using dialog window.
        """

        download_dir = filedialog.askdirectory()
        
        self.etr_download_dir_path_frm_yt_download.delete(0, len(self.etr_download_dir_path_frm_yt_download.get()))

        if not len(download_dir) == 0:
            self.etr_download_dir_path_frm_yt_download.insert(0, download_dir)
        else:
            self.etr_download_dir_path_frm_yt_download.insert(0, "Enter directory absolute path.")

    def set_etr_download_dir_path_frm_yt_download_via_mouse_b1_event(self, event):
        """
        Set etr_download_dir_path_frm_yt_download variable using dialog window when entry widget is clicked.
        """

        self.set_etr_download_dir_path_frm_yt_download()
    
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("480x150")
    root.resizable(False, False)
    app = Application(master=root)
    app.mainloop()