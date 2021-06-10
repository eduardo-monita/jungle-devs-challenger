from django.apps import AppConfig


class PostsAppConfig(AppConfig):
    name = 'posts'
    verbose_name = 'Posts'

    def ready(self):
        import posts.signals