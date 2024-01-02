import tkinter as tk
import vlc

window = tk.Tk()       # Create the main window
window.title("Video Player")

frame = tk.Frame(window, width=900, height=500) # Create a Frame to hold the video

frame.pack()

instance = vlc.Instance("--no-xlib")# Create a VLC media player instance
player = instance.media_player_new() # Create a media player

media = instance.media_new('penguins.mp4') # Set the stream/media... to be played

media.get_mrl() #media resource locator prepares the media to be played

player.set_media(media) # the player is set to play the media chosen
player.set_xwindow(frame.winfo_id())# Attach the video player to the frame i created earlier to hold the video

btn_play = tk.Button(window, text="Play", command=player.play)
btn_play.pack(side=tk.LEFT)

btn_pause = tk.Button(window, text="Pause", command=player.pause)
btn_pause.pack(side=tk.LEFT)

btn_stop = tk.Button(window, text="Stop", command=player.stop)
btn_stop.pack(side=tk.LEFT)

window.mainloop() # Run the GUI application