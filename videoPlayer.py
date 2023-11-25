import tkinter as tk
import vlc

def save_stream_to_file(media, outputFile):
    player = vlc.MediaPlayer()
    player.set_media(media)
    player.play()
    
    media.parse()
    media.get_mrl()
    
    with open(outputFile, 'wb') as f:
        while True:
            data = player.get_fps()
            if data:
                f.write(data)
            else:
                break
window = tk.Tk()       # Create the main window
window.title("Video Player")

frame = tk.Frame(window, width=900, height=500) # Create a Frame to hold the video
frame.pack()

instance = vlc.Instance("--no-xlib")# Create a VLC media player instance
player = instance.media_player_new() # Create a media player

######
#I created a local http server at the dir that the media file is located using:
# (python3 -m http.server <port>) -> This is a python3 module that creates a local server
#     that can be accessed in the local network by using the ip address of the pc in the network
#     and the port of the server(default:8000) 
media = instance.media_new('https://www.youtube.com/watch?v=imhon1dhyTA') # Set the stream/media... to be played
#src="http://192.168.43.37:81/stream"
media.get_mrl() #media resource locator prepares the media to be played

player.set_media(media) # the player is set to play the media chosen
player.set_xwindow(frame.winfo_id())# Attach the video player to the frame i created earlier to hold the video
player.play() # Play the video

#########
#controls for the video player
#other things along the way also that i gotta figure out.
#########

outputFile = 'fileStream.mp4'
save_stream_to_file(media, outputFile)

window.mainloop() # Run the GUI application
