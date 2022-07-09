from utils import load_json, save_as_json

DATA_SRC = "data/data.json"
COMMENTS_SRC = "data/comments.json"
BOOKMARKS_SRC = "data/bookmarks.json"


class MainDAO:

    def __init__(self,
                 data_path: str = DATA_SRC,
                 com_path: str = COMMENTS_SRC,
                 bookmarks_path: str = BOOKMARKS_SRC
                 ):
        self.data_path = data_path
        self.com_path = com_path
        self.bookmarks_path = bookmarks_path

    def posts_all(self) -> list[dict]:
        return load_json(self.data_path)

    def posts_by_user(self, user_name: str) -> list[dict]:
        """ Возвращает посты определенного пользователя

        :param user_name:
        :return:
        """
        if not isinstance(user_name, str):
            raise TypeError("user_name must be string")

        posts_list: list[dict] = load_json(self.data_path)
        if posts_list:
            users_posts = [post for post in posts_list if post["poster_name"] == user_name]
            if not users_posts:
                raise ValueError("User not found")
            return users_posts

    def posts_by_substring(self, substring: str) -> list:
        """ Возвращает список постов по ключевому слову

        :param substring:
        :return:
        """
        if not isinstance(substring, str):
            raise TypeError("substring must be string")

        result = []
        posts: list[dict] = load_json(self.data_path)
        for post in posts:
            content: str = post["content"]
            if substring.lower() in content.lower():
                result.append(post)
        return result

    def post_by_pk(self, pk: int) -> dict:
        """ Возвращает один пост по его идентификатору.

        :param pk:
        :return:
        """
        posts_list: list[dict] = self.posts_all()
        if posts_list:
            posts = [post for post in posts_list if post["pk"] == pk]
            if not posts:
                raise ValueError("Post does not exist")
            return posts[0]

    def comments_by_post_id(self, post_id: int) -> list | None:
        """ Возвращает комментарии определенного поста.

        :param post_id:
        :return:
        """
        if not isinstance(post_id, int):
            raise TypeError("post_id must be int")

        comments_list: list = load_json(self.com_path)
        if comments_list:
            posts = [post for post in comments_list if post["post_id"] == post_id]
            if not posts:
                raise ValueError("Post does not exist")

            comments = [comment for comment in posts if comment["comment"]]
            if not comments:
                return []
            return posts
        else:
            return None

    def load_bookmarks(self):
        return load_json(self.bookmarks_path)

    def save_bookmarks(self, pk: int, path: str):
        post = [self.post_by_pk(pk)]
        save_as_json(post, path)
