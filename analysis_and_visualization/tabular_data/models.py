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
        csv_data = []
        reader = csv.DictReader(csv_file)
        for row in reader:
            csv_data.append(row)

        csv_content = '\n'.join([','.join(row.values()) for row in csv_data])

        self.csv_content = csv_content
        self.save()

        def __str__(self):
            return f"UploadedCSV {self.pk} by {self.user.email}"
