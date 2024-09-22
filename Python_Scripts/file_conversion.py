from ffmpy import FFmpeg
class Converter:
   def __init__(self):
      print("File converter created. ")
   def gif_to_mp4(self,file_name):
      print("Converting from gif to mp4....")
      try:
         conversion_process = FFmpeg(
            inputs={file_name: None},
            outputs={file_name+".mp4": None}
         )
         conversion_process.run()
         print("Yay! Your file has been converted!")
      except Exception as e:
        print("ERROR MESSAGE: "+str(e))
      
def menu():
   print("File converter: ")
   print("-------------------------")
   print("1) Convert from gif to mp4")
   print("2) Exit")

def main():
   converter = Converter()
   choice = 0
   while(choice != 2):  
      menu()
      choice = int(input("Select file conversion type: "))
      if choice == 1:   
           try:
              file_name = input("Choose file to convert. Do not forget the file: ")
              converter.gif_to_mp4(file_name)
           except Exception as e:     
              print("Sorry! No can do! ERROR MESSAGE: "+str(e))             
      if choice == 2:
            print("Goodbye!")
      
main()