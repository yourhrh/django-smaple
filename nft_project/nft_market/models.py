from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=100)
    introduce = models.TextField()
    # TODO: Wallet information

    def __str__(self):
        return self.email


class Nft(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    min_price = models.IntegerField()
    introduce = models.TextField()
    image_url = models.TextField()
    # TODO : NFT information

    def __str__(self):
        return name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nft = models.ForeignKey(Nft, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.user.naem + '-' + self.nft.name