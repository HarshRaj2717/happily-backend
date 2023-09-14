from django.db import models

from authenticator.models import Users
# Create your models here.


class Posts(models.Model):
    created_by = models.ForeignKey(
        'authenticator.Users', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    content = models.TextField()
    total_votes = models.IntegerField(default=0)
    # TODO comments

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

    def downvote(self, user_key):
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
