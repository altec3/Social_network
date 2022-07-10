from flask import Blueprint, render_template, request, escape

from app.main.dao.main_dao import MainDAO
from app.bookmarks.dao.bookmarks_dao import BookmarksDAO

bp_main = Blueprint("bp_main", __name__, template_folder="templates")

main_dao = MainDAO()
bookmarks_dao = BookmarksDAO()


@bp_main.route("/")
def main_page():
    posts = main_dao.posts_all()
    bookmarks = bookmarks_dao.all_bookmarks()
    return render_template("index.html", posts=posts, bookmarks=bookmarks)


@bp_main.route("/posts/<int:pk>")
def post_page(pk: int):
    post = main_dao.post_by_pk(pk)
    comments = main_dao.comments_by_post_id(pk)
    return render_template("post.html", post=post, comments=comments)


@bp_main.route("/search/")
def search_page():
    target = request.args.get("s")
    if target:
        posts: list[dict] = main_dao.posts_by_substring(escape(target))
        if len(posts) > 10:
            posts = posts[:10]
        return render_template("search.html", target=target, posts=posts)
    else:
        return render_template("search.html")


@bp_main.route("/user/<username>")
def users_posts_page(username: str):
    posts = main_dao.posts_by_user(escape(username))
    return render_template("user-feed.html", posts=posts)
