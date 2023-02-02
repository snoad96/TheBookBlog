from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Member(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()


class Posts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    publication_date = models.DateField()
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="book_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    book = CloudinaryField('image', default='placeholder', max_length=100)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='book_likes', blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def number_of_book_likes(self):
        return self.likes.count()


class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    post = models.ForeignKey(
        Posts, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# --Add in later

# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True)
