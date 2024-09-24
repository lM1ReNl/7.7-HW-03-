from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        posts_rating = self.posts.aggregate(pr=Coalesce(Sum('rating'), 0)).get('pr')
        comments_rating = self.user.comments.aggregate(cr=Coalesce(Sum('rating'), 0)).get('cr')
        posts_comments_rating = self.posts.aggregate(pcr=Coalesce(Sum('comment__rating'), 0)).get('pcr')

        self.rating = posts_rating * 3 + comments_rating + posts_comments_rating
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name

class Post(models.Model):
    article = 'AR'
    news = 'NE'
    CONTENTS = [
        (news, 'Новость'),
        (article, 'Статья')
    ]
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=2, choices=CONTENTS, default=news)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    category = models.ManyToManyField(Category, through='PostCategory')

    def like_post(self):
        self.rating += 1
        self.save()

    def dislike_post(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:124] + "..."

    def __str__(self):
        return f'{self.title}' # Модификация по модулю 6

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    rating = models.IntegerField(default=0)
    comment_timedate = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def like_comment(self):
        self.rating += 1
        self.save()

    def dislike_comment(self):
        self.rating -= 1
        self.save()