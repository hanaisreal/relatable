from django.db import models
from post.models import Post

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=False)
    author_id = models.IntegerField(
        null=True, default=None)  # Null when deleted
    
    # Do not delete when parent deleted
    # Actually does not happen
    parent_comment = models.ForeignKey(
        'self', on_delete=models.PROTECT, related_name='replies', null=True)

    content = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "comment for {}, comment id {}".format(self.post.title, self.id)