import pyttsx3
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init()     # инициализация движка

# зададим свойства
engine.setProperty('rate', 150)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)

engine.say("Привет, я голосовой ассистент! Если хотите узнать, на что я способна напишите в консоль 'Хочу' ")  # запись фразы в очередь

# очистка очереди и воспроизведение текста
engine.runAndWait()

if input().lower() == 'хочу':
    abil = open('abilities.txt', 'r', encoding='utf8')
    info = abil.read()
    engine.say(info)

    engine.runAndWait()


choice = input('1: Прочитать текст из файла \n'
               '2: Прочитать статью из Википедии \n'
               'Укажите цифру: ')


def say_file(file):
    text_file = open(f"{file}", "r", encoding='utf8')
    data = text_file.read()
    engine.say(data)

    engine.runAndWait()

    text_file.close()

def say_wiki(link):
    response = requests.get(link)

    soup = BeautifulSoup(response.content, 'lxml')
    p = soup.find_all("p")

    txt = list()

    for t in p:
        txt.append(t.text.strip())

    engine.say(''.join(txt))
    engine.runAndWait()



if __name__ == '__main__':
    if int(choice) == 1:
        say_file(input(r'Путь: '))
    if int(choice) == 2:
        say_wiki(input('Ссылка на статью: '))
