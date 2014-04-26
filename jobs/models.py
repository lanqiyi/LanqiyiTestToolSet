from django.db import models


class Job(models.Model):
    pub_date = models.DateField()
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()

    def __str__(self):
        return "%s %s" % (self.pub_date, self.job_title)

    class Admin:
        list_display = ("put_date", "job_title", "job_description")