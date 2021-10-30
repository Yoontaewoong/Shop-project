from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    p_id = models.PositiveBigIntegerField(db_column='p_Id', primary_key=True)  # Field name made lowercase.
    p_title = models.TextField()
    p_image = models.TextField()
    p_lprice = models.PositiveIntegerField()
    p_brand = models.CharField(max_length=45, blank=True, null=True)
    p_category1 = models.CharField(max_length=45, blank=True, null=True)
    p_category2 = models.CharField(max_length=45, blank=True, null=True)
    p_category3 = models.CharField(max_length=45, blank=True, null=True)
    p_category4 = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.p_title


class Review(models.Model):
    r_title = models.CharField(max_length=200)
    r_text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    r_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.r_title


class ShopBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    s_ordered = models.BooleanField(default=False)
    s_amount = models.IntegerField(default=1)

    def __str__(self):
        return "[{}] {}".format(self.id, self.user.username)


class MyPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    m_emoney = models.PositiveIntegerField()

    def __str__(self):
        return "[{}] {}".format(self.id, self.user.username)


class Question(models.Model):
    q_author = models.CharField(max_length=20)  # 작성자
    q_title = models.CharField(max_length=200)
    q_content = models.TextField()
    q_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.q_title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    a_title = models.CharField(max_length=200)
    a_content = models.TextField()
    a_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.a_title


class Notice(models.Model):
    n_title = models.CharField(max_length=200)
    n_text = models.TextField()
    n_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.n_title
