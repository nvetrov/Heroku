# TODO Необходимо написать простой веб-сервер с помощью фреймворка Bottle. Все ошибки приложения должны попадать в
#  вашу информационную панель Sentry. Приложение должно размещаться на Heroku, иметь минимум два маршрута: /success,
#  который должен возвращать как минимум HTTP ответ со статусом 200 OK /fail, который должен возвращать "ошибку
#  сервера" (на стороне Bottle это может быть просто RuntimeError), то есть HTTP ответ со статусом 500

# heroku config:set APP_LOCATION=heroku
# git push heroku master
# heroku ps:scale web=1



import os

import sentry_sdk
from bottle import Bottle
from sentry_sdk.integrations.bottle import BottleIntegration

# with open("dsn", "r") as f:
#     your_dsn = f.read()

# your_dsn = input("Paste your dsn here:")

sentry_sdk.init(
    dsn="https://79a87c759b5247dd8bf8a9770cc74cf6@sentry.io/1832381",
    integrations=[BottleIntegration()]
)

app = Bottle()


def generate_message():
    return "Тестируе: /success  or /fail "


def success_message():
    return "Победа"


def fail_message():
    return "Ошибка"


@app.route("/success")
def success():
    html_success = """
    <!doctype html>
    <html lang="en">
      <head>
        <title>Heroku </title>
      </head>
      <body>
        <div class="container">
          <h1>This is success!</h1>
          <p>{}</p>        
        </div>
      </body>
    </html>
    """.format(
        success_message()
    )
    return html_success


@app.route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Heroku </title>
  </head>
  <body>
    <div class="container">
      <h1>Проверь меня!</h1>
      <p>{}</p>
    </div>
  </body>
</html>
""".format(
        generate_message()
    )
    return html


@app.route('/fail')
def fail():
    raise RuntimeError("There is an error!")


# app.run(host='localhost', port=8080)

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3, )
else:
    app.run(host='127.0.0.1', port=8080, debug=True)
