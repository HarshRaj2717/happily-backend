from django.db import models

from authenticator.models import Users

# Create your models here.


class Posts(models.Model):
    created_by = models.ForeignKey(
        'authenticator.Users', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.TextField(blank=False)
    content = models.TextField(blank=False)
    total_votes = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.id)  # type: ignore

    def upvote(self, user_key) -> dict[str, int]:
        """
        Upvotes the current Posts instance
        """
        user = Users.objects.get(api_token=user_key)
        vote, _ = Votes.objects.get_or_create(post=self, user=user)

        if vote.vote_value == -1:
            vote.vote_value = 1
            self.total_votes += 2
        elif vote.vote_value == 0:
            vote.vote_value = 1
            self.total_votes += 1
        else:
            vote.vote_value = 0
            self.total_votes -= 1
        vote.save()
        self.save()

        return {
            'user_new_vote_value': vote.vote_value,
            'post_total_votes': self.total_votes,
        }

    def downvote(self, user_key) -> dict[str, int]:
        """
        Downvotes the current Posts instance
        """
        user = Users.objects.get(api_token=user_key)
        vote, _ = Votes.objects.get_or_create(post=self, user=user)

        if vote.vote_value == 1:
            vote.vote_value = -1
            self.total_votes -= 2
        elif vote.vote_value == 0:
            vote.vote_value = -1
            self.total_votes -= 1
        else:
            vote.vote_value = 0
            self.total_votes += 1
        vote.save()
        self.save()

        return {
            'user_new_vote_value': vote.vote_value,
            'post_total_votes': self.total_votes,
        }

    def add_comment(self, user_key, content):
        """
        Creates a new comment
        """
        user = Users.objects.get(api_token=user_key)
        comment = Comments.objects.create(
            for_post=self,
            created_by=user,
            content=content,
        )
        comment.save()
        self.total_comments += 1

    def delete_comment(self, user_key, comment_id):
        """
        Deletes a comment
        """
        comment = Comments.objects.get(id=comment_id)
        assert comment.for_post == self
        assert Users.objects.get(api_token=user_key) == comment.created_by
        comment.delete()
        self.total_comments -= 1


class Votes(models.Model):
    post = models.ForeignKey(
        'community.Posts', on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'authenticator.Users', on_delete=models.CASCADE
    )
    vote_value = models.IntegerField(
        choices=[(1, 'UpVote'), (0, 'None'), (-1, 'DownVote')], default=0
    )

    class Meta:
        unique_together = ['post', 'user']

    def __str__(self) -> str:
        return str(f"{self.post}_{self.user}")


class Comments(models.Model):
    for_post = models.ForeignKey(
        'community.Posts', on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        'authenticator.Users', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)

    def __str__(self) -> str:
        return str(
            f"{self.id}=>{self.for_post}_{self.created_by}")  # type: ignore
