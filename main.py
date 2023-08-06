#importing PIL library to edit images
import PIL
#importing ArgumentParser from argparae to allow options to be passed in from the terminal
from argparse import ArgumentParser
#importing os to read directories(folders)
import os

#if statement checks if required folders exsist creates them if they dont.
def setup_workspace():

    #checks if imgs folder is in the project 
    if "imgs" not in os.listdir("./"):
        print("no imgs found creating folder")
        #creates a directory called imgs
        os.mkdir("imgs")
    #checks if edited_imgs folder is in the project
    if "edited_imgs" not in os.listdir("./"):
        print("no edited_imgs found creating folder")
        #creates a directery called edited_imgs
        os.mkdir("edited_imgs")


#begining of the program
def main(options):
    #sets up required folders
    setup_workspace()
    if options.h:
        print("help is on the way")

if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("--h", type = bool, default = False)
    main(args.parse_args())