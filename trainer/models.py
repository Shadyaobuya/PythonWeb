from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from core.models import ModificationTrackingModel
from django_countries.fields import CountryField


# Create your models here.
class Gender(models.TextChoices):
    FEMALE = "Female"
    MALE = "Male"
    PREFER_NOT_TO_SAY = "Prefer not to say"


class Trainer(ModificationTrackingModel):
    first_name = models.CharField(
        max_length=30,
        null=False,
        help_text="First name of the Trainer",
    )

    last_name = models.CharField(
        max_length=30,
        null=False,
        help_text="Last name of the Trainer",
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
        help_text="Trainer's date of birth in the format YYYY-MM-DD",
    )

    nationality = CountryField(
        null=True,
        blank=True,
        help_text="Trainer's country of origin",
    )

    national_id = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text="National ID number, if applicable",
    )

    email = models.EmailField(
        max_length=50,
        null=False,
        blank=False,
        help_text="Email address of the Trainer",
    )

    phone_number = PhoneNumberField(
        max_length=30,
        null=True,
        blank=True,
        help_text="Phone number of the Trainer, including country code",
    )
    image = models.ImageField(
        upload_to="trainer_images/",
        null=True,
        help_text="Profile image of the Trainer",
    )
    company_name = models.CharField(max_length=30, null=True)

    gender = models.CharField(
        max_length=20, choices=Gender.choices, default=Gender.PREFER_NOT_TO_SAY
    )

    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}-{self.course}"
