from django.db import models
from django.contrib.auth.models import User

# models is space for database storage - tables with columns, rows#
#User module in django handles users authorization#
#Many-to-one relationships by ForeignKey; eg. reported can be associated with lots of articles#
# but article can have only one Reporter object#

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length=200, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    complete = models.BooleanField(default = False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

