from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/contacts/')
def contacts():
    developer_name = "Nick"
    context = {'name': developer_name}
    return render_template('contacts.html', props=context)


if __name__ == '__main__':
    app.run(debug=True)
