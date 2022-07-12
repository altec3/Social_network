from flask import Blueprint, jsonify
import logging

from app.main.view import main_dao
from loggers_conf import create_logger

create_logger()

logger = logging.getLogger('basic')

# logging.basicConfig(level=logging.INFO)
# logger_api = logging.getLogger("api")
# file_handler = logging.FileHandler("logs/api.log", encoding="utf-8")
# formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
# file_handler.setFormatter(formatter)
# logger_api.addHandler(file_handler)

bp_get_json = Blueprint("bp_get_json", __name__)


@bp_get_json.route("/api/posts/")
def get_json_posts():
    posts = main_dao.posts_all()
    if posts:
        logger.info(f"Запрос /api/posts/")
        return jsonify(posts)


@bp_get_json.route("/api/posts/<int:post_id>")
def get_json_post(post_id: int):
    post = main_dao.post_by_pk(post_id)
    if post:
        logger.info(f"Запрос /api/posts/{post_id}")
        return jsonify(post)
