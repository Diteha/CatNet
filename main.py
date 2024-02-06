# Flask - библиотека для создания веб-сервера
from flask import Flask, request, render_template
from datetime import datetime
import json

app = Flask(__name__)
DATA_FILE = "data_001.json"


# Загружаем сообщения из файла
def load_messages():
  with open(DATA_FILE, "r") as json_file:
    data = json.load(json_file)  # data = {"all_messages":  [] }
    return data["all_messages"]
  json_file.close()


all_messages = load_messages()  # При старте сервера, загружаем сообщения из файла в переменную


#Стартовая страница
@app.route("/")
def hello_world():
  return render_template("form.html")


@app.route("/get_messages")
def get_messages():
  return {"messages": all_messages}


def add_message(image_users, id_sender,  id_room, text):
  new_message = {
    "image_users": image_users,
    "id_sender": id_sender,
    "id_room": id_room,
    "text": text,
    "time": datetime.now().strftime("%H:%M"),
  }
  # append - добавить элемент в список
  all_messages.append(new_message)
  save_messages()  # Сохраняем в файл


# Сохраняем сообщения в файл
def save_messages():
  with open(DATA_FILE, "w") as json_file:
    data = {"all_messages": all_messages}
    json.dump(data, json_file)


# API для отправки сообщений 
@app.route("/send_message")
def send_message():
  image_users = request.args["image_users"]
  id_sender = request.args["id_sender"]# ToDO: error here, sender vs name
  id_room = request.args["id_room"]
  text = request.args["text"]
  add_message(image_users, id_sender, id_room, text)
  return {"result": True}




  
app.run(host="localhost", port=4000)

