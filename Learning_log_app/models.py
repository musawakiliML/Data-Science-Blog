from tabnanny import verbose
from django.db import models

# Create your models here.


class Topic(models.Model):
    """ Creates the Topic model that stands as the category of the learning.

    Args:
        models (model): provides the methods of

    Returns:
        str : the string name of the of the model object
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """ Create the Entry model, that holds the log for the user as Specific learned information.

    Args:
        models (_type_): _description_
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        """Return strig representation of the model as the first 50 characters."""
        return f"{self.text[:50]}"
