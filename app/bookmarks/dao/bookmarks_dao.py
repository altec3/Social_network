from utils import load_json, save_as_json

BOOKMARKS_SRC = "data/bookmarks.json"


class BookmarksDAO:

    def __init__(self, bookmarks_path: str = BOOKMARKS_SRC):
        self.bookmarks_path = bookmarks_path

    def all_bookmarks(self) -> list | list[dict]:
        return load_json(self.bookmarks_path)

    def add_bookmark(self, post: dict) -> None:
        bookmarks = self.all_bookmarks()
        added_bookmarks = {bookmark["pk"] for bookmark in bookmarks}
        if post["pk"] not in added_bookmarks:
            bookmarks.append(post)
            save_as_json(bookmarks, self.bookmarks_path)

    def del_bookmark(self, post: dict) -> None:
        bookmarks = self.all_bookmarks()
        for ind, bookmark in enumerate(bookmarks):
            if bookmark["pk"] == post["pk"]:
                bookmarks.pop(ind)
                save_as_json(bookmarks, self.bookmarks_path)
