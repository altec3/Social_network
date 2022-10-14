from flask import Blueprint, render_template, request, redirect

from app.bookmarks.dao.bookmarks_dao import BookmarksDAO
from app.main.dao.main_dao import MainDAO

bp_bookmarks = Blueprint("bp_bookmarks", __name__, template_folder="templates")

bookmarks_dao = BookmarksDAO()
main_dao = MainDAO()


@bp_bookmarks.route("/")
def bookmarks_page():
    bookmarks = bookmarks_dao.all_bookmarks()
    return render_template("bookmarks.html", posts=bookmarks)


@bp_bookmarks.route("/add/<int:pid>")
def add_bookmark(pid: int):
    post = main_dao.post_by_pk(pid)
    bookmarks_dao.add_bookmark(post)
    return redirect("/", code=302)


@bp_bookmarks.route("/del/", methods=["POST"])
def del_bookmark():
    pk = int(request.form.get("del"))
    post = main_dao.post_by_pk(pk)
    bookmarks_dao.del_bookmark(post)
    return redirect("/", code=302)
