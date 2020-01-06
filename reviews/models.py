from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models
# Create your models here.


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()

    accuracy = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    communication = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    cleanLiness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    location = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    check_in = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accuracy +
            self.communication +
            self.cleanLiness +
            self.location +
            self.check_in +
            self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "AVG"

    class Meta:
        ordering = ('-created',)
