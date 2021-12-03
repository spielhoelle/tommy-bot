import os
import flask
from flask import render_template
import requests
from flask_apscheduler import APScheduler
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

print("TF Version:", tf.__version__)

if os.path.isfile("one_step/saved_model.pb") is True:
    model = tf.compat.v1.saved_model.load_v2("one_step", None)
else:
    print("No saved model")


def predict(text):
    states = None
    next_char = tf.constant(["Tommy says: "])
    result = [next_char]
    for n in range(100):
        next_char, states = model.generate_one_step(next_char, states=states)
        result.append(next_char)
    print(tf.strings.join(result)[0].numpy().decode("utf-8"))
    return tf.strings.join(result)[0].numpy().decode("utf-8")


app = flask.Flask(__name__, static_folder="../build", static_url_path=None)

scheduler = APScheduler()
times_run = 0
messages = []
scheduler.init_app(app)
scheduler.start()

INTERVAL_TASK_ID = "interval-task-id"


def interval_task():
    global messages
    global times_run

    response = requests.post(
        "https://api.telegram.org/" + os.getenv("TELEGRAM_BOT_ID") + "/getUpdates",
        {"offset": 1},
    )
    response.raise_for_status()
    jsonResponse = response.json()
    newMessages = []
    print("Run cronjob - messages currently in cache: ", len(messages))
    for eventuallyNewMessage in jsonResponse["result"]:
        fount = [
            x for x in messages if x["update_id"] == eventuallyNewMessage["update_id"]
        ]
        if len(fount) == 0:
            print("New message")
            print(eventuallyNewMessage)
            newMessages.append(eventuallyNewMessage)

    messages = jsonResponse["result"]
    print("#####################################jsonResponse")
    print(jsonResponse)
    if (
        len(newMessages) > 0
        and times_run != 0
        and "text" in jsonResponse["result"][-1]["message"]
    ):
        message = jsonResponse["result"][-1]["message"]["text"]

        str1 = " "
        prediction = predict(message)
        myobj = {"chat_id": "579817872", "text": prediction}
        if message == "yes":
            print("###########################")
            print("Bot will answer positive")
            print(" ")
            response = requests.post(
                "https://api.telegram.org/"
                + os.getenv("TELEGRAM_BOT_ID")
                + "/sendMessage",
                data=myobj,
            )
        else:
            print("###########################")
            print("Bot will answer negative")
            print(" ")
            response = requests.post(
                "https://api.telegram.org/"
                + os.getenv("TELEGRAM_BOT_ID")
                + "/sendMessage",
                data=myobj,
            )
    times_run += 1


scheduler.add_job(
    id=INTERVAL_TASK_ID, func=interval_task, trigger="interval", seconds=8
)


@app.route("/")
def home():
    return render_template("base.html", name="Tommy")


# Run the example
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
