from django.db import models

STATUS_CHOICES = [('AWAITING START', 'awaiting start'), ('IN PROGRESS', 'in progress'), ('DONE', 'done')]


class Bug(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='awaiting start', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='bugs', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
