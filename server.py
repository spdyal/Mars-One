from flask import Flask, url_for, request, render_template

from data import db_session
from data.jobs import Jobs

app = Flask(__name__)


@app.route("/")
def work():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template("works_log.html", jobs=jobs)


if __name__ == '__main__':
    db_session.global_init('db/mars.db')
    app.run()

