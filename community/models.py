from django.db import models

# Create your models here.


class Posts(models.Model):
    created_by = models.ForeignKey(
        'authenticator.Users', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    content = models.TextField()
    # TODO comments

    def __str__(self) -> str:
        return str(self.id)  # type: ignore
