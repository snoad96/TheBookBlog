from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Members(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)


class Posts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
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
        odering = ['published_date']

    def __str__(self):
        return self.title

    def number_of_book_likes(self):
        return self.likes.count()
