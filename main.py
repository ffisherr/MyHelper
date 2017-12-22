from tkinter import *
from tkinter import messagebox
from get_stat import ret_data
from pars_news import get_info


root = Tk()
root.geometry("700x300")
root.title("J.A.R.V.I.S")
en_letters=['A','a','B','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-']

def getting_data():

    def check():
        z=0
        if city.get()=='':
            z=1
        for h in city.get():
            if not (h in en_letters):
                z=1
        if z:
            messagebox.showerror("Translate","Пока что писать можно только на английском(((")
        else:
            save()
    
    def save():
        my_file = open("some.txt", "wb")
        my_file.write((city.get()).encode())
        my_file.close()
        data_from()

    def show_news():
        news = get_info()
        tnews=''
        for n in news:
            tnews = tnews +n+'\n'

        show_n(tnews) 

    def make_note():
        file = open("notes.txt", "a")
        file.write(note.get()+'\n')
        file.close()

    def clear_note():
        my_file = open("some.txt", "wb")
        my_file.close()

    show_news()
    city = StringVar()
    note = StringVar()
    text = Label(text="В каком городе смотрим погоду?")
    text_city = Label(text="Введите город:")
    input_note = Entry(textvariable=note)
    in_put = Entry(textvariable=city)
    button_note = Button(text="Создать заметку", command = lambda: make_note())    
    button_data = Button(text="Погода", command = lambda: check())
    button_news_yandex = Button(text="Новости", command = lambda: show_news())
    button_note = Button(text="Очистить заметки", command = lambda: clear_note())

    text.grid(row=0,column=0)
    text_city.grid(row=3,column=0)
    in_put.grid(row=5,column=0)
    button_data.grid(row=6,column=0)    
    button_news_yandex.grid(row=7,column=2)
    input_note.grid(row=8,rowspan=2,column=2)
    button_note.grid(row=10, column=2)


def data_from():
    f = open("some.txt", "rb")
    the_city = f.read().decode('utf-8')
    f.close()
    show(the_city)

def show_n(news):
    text_news = Label(text=news)
    text_news.grid(row=0,column=2,sticky="e")

def show(output):
    info = Label(text = ret_data(output))
    info.grid(row=8,column=0)



getting_data()
root.mainloop()