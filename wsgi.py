from flask import Flask, render_template

from app.main.view import bp_main
from app.bookmarks.view import bp_bookmarks
from app.api.view import bp_get_json

app = Flask(__name__)

app.config.from_pyfile("config.py")
app.register_blueprint(bp_main)
app.register_blueprint(bp_bookmarks)
app.register_blueprint(bp_get_json)


@app.errorhandler(404)
def not_found_page(error):
    return render_template("error.html", title="Error 404 (Not found)", message=f"{error}"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("error.html", title="Error 500", message=f"{error}"), 500


if __name__ == "__main__":
    app.run()
