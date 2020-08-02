from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    #create one profile for one user + if user is deleted then delete its profile as well
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #upload image here + default image set + where profile pic will be saved
    pimage = models.ImageField(default="default.jpg", upload_to='profilt_pics')

    # but if print like that only it will show object so use below code to make it more descriptive
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        #resize image at the time of save . save is bulit in function we are just changing few things
        img =Image.open(self.pimage.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.pimage.path)
