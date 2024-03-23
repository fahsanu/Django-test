from django.db import models

transportation_mode_choices = [
    ('car', 'Car'),
    ('motorcycle', 'Motorcycle'),
    ('bus', 'Bus'),
    ('metro', 'Metro'),
    ('walk', 'Walk')
]

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Schedule(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    # date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    transportation_mode = models.CharField(
        max_length=20, choices=transportation_mode_choices)
    extra_prep_time = models.IntegerField()
    note = models.TextField()

    def __str__(self):
        return self.event_name