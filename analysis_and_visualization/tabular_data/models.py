from io import TextIOWrapper

from django.db import models
from django.utils import timezone
import csv
from auth_users.models import User


class UploadedTable(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    csv_content = models.TextField()
    title = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def save_csv_content(self, csv_file):
        csv_content = csv_file.read().decode('utf-8')

        # Store the CSV content in the text field
        self.csv_content = csv_content
        self.save()


        def __str__(self):
            return f"UploadedCSV {self.pk} by {self.user.email}"
