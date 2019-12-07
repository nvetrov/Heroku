# TODO Необходимо написать простой веб-сервер с помощью фреймворка Bottle. Все ошибки приложения должны попадать в
#  вашу информационную панель Sentry. Приложение должно размещаться на Heroku, иметь минимум два маршрута: /success,
#  который должен возвращать как минимум HTTP ответ со статусом 200 OK /fail, который должен возвращать "ошибку
#  сервера" (на стороне Bottle это может быть просто RuntimeError), то есть HTTP ответ со статусом 500

import sentry_sdk
from bottle import Bottle
from sentry_sdk.integrations.bottle import BottleIntegration

# with open("dsn", "r") as f:
#     your_dsn = f.read()

your_dsn = input("Paste your dsn here:")

sentry_sdk.init(
    dsn=your_dsn,
    integrations=[BottleIntegration()]
)

app = Bottle()


@app.route('/success')
def success():
    return


@app.route('/fail')
def fail():
    raise RuntimeError("There is an error!")


app.run(host='localhost', port=8080)
