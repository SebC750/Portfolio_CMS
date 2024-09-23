#A Python wrapper for the ffmpeg library to convert image/video files.
from ffmpy import FFmpeg
#I wrote this program because I wanted to convert an animation of mine to mp4 since IG doesn't allow gifs to be uploaded. I'll probably add more conversion methods if I need to convert more files anyways but this script did the job just fine.

#The converter class is mean't to represent a converter that can convert many things. It's meant to be a singleton and depending on the user's choice, its reused for that purpose.
class Converter:
   def __init__(self):
      print("File converter created. ")
   def gif_to_mp4(self,file_name):
      print("Selected file: "+file_name)
      print("Converting from gif to mp4....")
      try:
         #Convert the input file and output the results.
         conversion_process = FFmpeg(
            inputs={file_name: None},
            #Using Instagram video configs to make it compatible. For some reason, the video wouldn't load on IG so I had to add the specific video codec, resolution etc..
            outputs={file_name[0:len(file_name)-4]+".mp4": '-c:v libx264 -pix_fmt yuv420p -b:v 1M -c:a aac -b:a 128k'}
         )
         conversion_process.run()
         print("Yay! Your file has been converted!")
      except Exception as e:
        print("ERROR MESSAGE: "+str(e))
#The menu options that are printed out continuously after every action.     
def menu():
   print("File converter: ")
   print("-------------------------")
   print("1) Convert from gif to mp4")
   print("2) Exit")
#The driver code. The program loops for as long as you don't choose to exit. 
def main():
   converter = Converter()
   choice = 0
   while(choice != 2):  
      menu()
      choice = int(input("Select file conversion type: "))
      if choice == 1:   
           try:
              file_name = input("Choose file to convert. Include the file extension: ")
              converter.gif_to_mp4(file_name)
           except Exception as e:     
              print("Sorry! No can do! ERROR MESSAGE: "+str(e))             
      if choice == 2:
            print("Goodbye!")
      
main()