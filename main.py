from cgitb import text
from turtle import width
from tkinterweb import HtmlFrame #import the HTML browser
from tkinter import *
from PIL import Image, ImageTk
import pygame

pygame.mixer.init()

def play_song():
    pygame.mixer.music.load(r"C:\Users\Ryan\Documents\HotsGuiV3\soil.mp3")
    pygame.mixer.music.play(loops=0)

def search():
    global root
    root = Tk() #create the tkinter window
    root.title("Hotslogs Lightweight")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    character = search_bar.get()
    frame = HtmlFrame(root) #create HTML browser
    frame.load_website(f"https://www.hotslogs.com/Sitewide/TalentDetails?Hero={character}") #load a website
    frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    root.mainloop()


def tower_winrate():
    global root
    root = Tk() #create the tkinter window
    root.title("Towers of Doom")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    frame = HtmlFrame(root) #create HTML browser
    frame.load_website(f"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Towers%20of%20Doom") #load a website
    frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    root.mainloop()

def alterac_winrate():
    global root
    root = Tk() #create the tkinter window
    root.title("Alterac Pass")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    frame = HtmlFrame(root) #create HTML browser
    frame.load_website(f"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Alterac%20Pass") #load a website
    frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    root.mainloop()

def battlefield_winrate():
    global root
    root = Tk() #create the tkinter window
    root.title("Battlefield of Eternity")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    frame = HtmlFrame(root) #create HTML browser
    frame.load_website(f"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Battlefield%20of%20Eternity") #load a website
    frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    root.mainloop()

def blackheart_winrate():
    global root
    root = Tk() #create the tkinter window
    root.title("Blackheart's Bay")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    frame = HtmlFrame(root) #create HTML browser
    frame.load_website(f"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?GameMode=3&Map=Blackheart%27s%20Bay") #load a website
    frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    root.mainloop()

def braxis_winrate():
    global root
    root = Tk() #create the tkinter window
    root.title("Braxis Holdout")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    frame = HtmlFrame(root) #create HTML browser
    frame.load_website(f"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Braxis%20Holdout") #load a website
    frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    root.mainloop()

def curse_winrate():
    global root
    root = Tk() #create the tkinter window
    root.title("Cursed Hollow")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    frame = HtmlFrame(root) #create HTML browser
    frame.load_website(f"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Cursed%20Hollow") #load a website
    frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    root.mainloop()

def dragon_winrate():
    global root
    root = Tk() #create the tkinter window
    root.title("Dragon Shrine")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    frame = HtmlFrame(root) #create HTML browser
    frame.load_website(f"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Dragon%20Shire") #load a website
    frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    root.mainloop()
    
def garden_winrate():
    global root
    root = Tk() #create the tkinter window
    root.title("Garden of Terror")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    frame = HtmlFrame(root) #create HTML browser
    frame.load_website(f"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Garden%20of%20Terror") #load a website
    frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    root.mainloop()

def hanamura_winrate():
    global root
    root = Tk() #create the tkinter window
    root.title("Hanamura Temple")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    frame = HtmlFrame(root) #create HTML browser
    frame.load_website(f"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Hanamura%20Temple") #load a website
    frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    root.mainloop()

def infernal_winrate():
    global root
    root = Tk() #create the tkinter window
    root.title("Infernal Shrines")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    frame = HtmlFrame(root) #create HTML browser
    frame.load_website(f"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Infernal%20Shrines") #load a website
    frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    root.mainloop()

def spider_winrate():
    global root
    root = Tk() #create the tkinter window
    root.title("Tomb of the Spider Queen")
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    frame = HtmlFrame(root) #create HTML browser
    frame.load_website(f"https://www.hotslogs.com/Sitewide/HeroAndMapStatistics?Map=Tomb%20of%20the%20Spider%20Queen") #load a website
    frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    root.mainloop()






search_screen = Tk()
search_screen.title("HotsLogs Lightweight GUI")
search_screen.geometry("350x500")
search_label = Label(search_screen, text="Hero Build Lookup", font="Helvetica")
search_label.pack()
search_bar = Entry(search_screen, width=50)
search_button = Button(search_screen, text="Search", activebackground="light blue", command=search)
search_bar.pack(pady=25)
search_button.pack()




#Counter Picker from Hotslogs
counter_label = Label(search_screen, text="Winrate by Map", font="Helvetica", pady=15)
counter_label.pack()



#Buttons for Map winrates
alterac_button = Button(search_screen, text="Alterac Pass", activebackground="light blue", command=alterac_winrate)
alterac_button.pack()
battlefield_button = Button(search_screen, text="Battlefield of Eternity", activebackground="light blue", command=battlefield_winrate)
battlefield_button.pack()
blackheart_button = Button(search_screen, text="Blackheart's Bay", activebackground="light blue", command=blackheart_winrate)
blackheart_button.pack()
braxis_button = Button(search_screen, text="Braxis Holdout", activebackground="light blue", command=braxis_winrate)
braxis_button.pack()
curse_button = Button(search_screen, text="Cursed Hollow", activebackground="light blue", command=curse_winrate)
curse_button.pack()
dragon_button = Button(search_screen, text="Dragon Shrine", activebackground="light blue", command=dragon_winrate)
dragon_button.pack()
garden_button = Button(search_screen, text="Garden of Terror", activebackground="light blue", command=garden_winrate)
garden_button.pack()
hanamura_button = Button(search_screen, text="Hanamura Temple", activebackground="light blue", command=hanamura_winrate)
hanamura_button.pack()
infernal_button = Button(search_screen, text="Infernal Shrines", activebackground="light blue", command=infernal_winrate)
infernal_button.pack()
spider_button = Button(search_screen, text="Tomb of the Spider Queen", activebackground="light blue", command=spider_winrate)
spider_button.pack()
towers_button = Button(search_screen, text="Towers of Doom", activebackground="light blue", command=tower_winrate)
towers_button.pack()
music_button = Button(search_screen, text="Soil", activebackground="light blue", command=play_song)
music_button.pack()

search_screen.mainloop()