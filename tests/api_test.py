class TestAPI:

    def test_get_json_posts_type(self, test_client):
        """ Проверяем тип возвращаемого значения """
        response = test_client.get('/api/posts', follow_redirects=True)
        list_posts = response.get_json()
        assert type(list_posts) == list, "get_json_posts -> возвращает не список"

    def test_get_json_posts_keys(self, test_client, correct_keys):
        """ Проверяем корректность ключей в словаре """
        response = test_client.get('/api/posts', follow_redirects=True)
        list_posts = response.get_json()
        for post in list_posts:
            assert list(post.keys()) == correct_keys, "get_json_posts -> не корректные ключи в словаре"

    def test_get_json_post_type(self, test_client):
        """ Проверяем тип возвращаемого значения """
        response = test_client.get('/api/posts/1', follow_redirects=True)
        post = response.get_json()
        assert type(post) == dict, "get_json_post -> возвращает не словарь"

    def test_get_json_post_keys(self, test_client, correct_keys):
        """ Проверяем корректность ключей в словаре """
        response = test_client.get('/api/posts/1', follow_redirects=True)
        post = response.get_json()
        assert list(post.keys()) == correct_keys, "get_json_post -> не корректные ключи в словаре"
