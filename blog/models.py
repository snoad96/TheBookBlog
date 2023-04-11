from django.db import models
from django.utils import timezone
from users.models import User
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    cover = models.ImageField(null=True)
#   likes = models.ManyToManyField(User, default=None, blank=True)
#   updated = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    @property
    def number_of_likes(self):
        return self.likes.all().count()


class Meta:
    ordering = ['created_on']


class Member(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()


class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    post = models.ForeignKey(
    Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# class add_comment(request):
#    text = request.POST.post('text')
#    post = request.POST.post(Post, related_name='blogid', on_delete=models.CASCADE)
#  ...
# c = Comment.objects.create(body=text, post=post, ...=...)