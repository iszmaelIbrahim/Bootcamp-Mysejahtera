from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


# Create your models here.

class post(models.Model):
    text = models.TextField(max_length=300, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class vaccine(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='NA')
    age = models.CharField(max_length=100, default='NA')

    STATE_LIST = [
        ('Selangor','Selangor'),
        ('Perak','Perak'),
        ('Pahang','Pahang'),
        ('Johor','Johor'),
    ]
    state = models.CharField(
        null=True,
        choices= STATE_LIST,
        max_length=100
        )
    date = models.DateTimeField(null=True, blank=True)


class health(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='NA')
    age = models.CharField(max_length=100, default='NA')

    CHOICE_LIST = [
        ('Yes','Yes'),
        ('No','No'),
    ]
    fever = models.CharField(
        null=True,
        choices= CHOICE_LIST,
        max_length=100
        )
    Chills = models.CharField(
        null=True,
        choices= CHOICE_LIST,
        max_length=100
        )
    headache = models.CharField(
        null=True,
        choices= CHOICE_LIST,
        max_length=100
        )
    vomiting = models.CharField(
        null=True,
        choices= CHOICE_LIST,
        max_length=100
        )
    diarrhea = models.CharField(
        null=True,
        choices= CHOICE_LIST,
        max_length=100
        )

    def __str__(self):
        return f'{self.user.username}'


class location_qr(models.Model):
    
    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    qr_code = models.ImageField(upload_to='qr_code', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs ):
        data = self.name + " - " + self.address
        print (data)
        qrcode_img = qrcode.make(data)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class geolocation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=200, default='')
    regionName = models.CharField(max_length=200, default='')
    city =models.CharField(max_length=200, default='')
    zip = models.CharField(max_length=200, default='')
    latitude = models.CharField(max_length=200, default='')
    longitude = models.CharField(max_length=200, default='')
    country_code = models.CharField(max_length=200, default='')
    country_timezone = models.CharField(max_length=200, default='')
    location_date = models.DateTimeField(default=timezone.now)

    



