import pyttsx3

engine = pyttsx3.init()     # инициализация движка

# зададим свойства
engine.setProperty('rate', 150)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)

engine.say("Привет, я голосовой ассистент! На данный момент я могу прочитать текст из файла, просто укажите мне путь до него")  # запись фразы в очередь

# очистка очереди и воспроизведение текста
engine.runAndWait()
file = input(r'Путь: ')

def say_file(file):
    text_file = open(f"{file}", "r", encoding='utf8')
    data = text_file.read()
    engine.say(data)
    engine.runAndWait()
    text_file.close()

if __name__ == '__main__':
    say_file(file)