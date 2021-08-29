class Post:
    def __init__(self, posts):
        self.all_posts = posts

    def get_post(self, id_to_find):
        for post in self.all_posts:
            if int(post['id']) == int(id_to_find):
                return post

    def print_posts(self):
        print(self.all_posts)
