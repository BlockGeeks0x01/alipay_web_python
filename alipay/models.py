from django.db import models

# Create your models here.


class Order(models.Model):
    user_name = models.CharField(max_length=20, default='', db_column='user_name', verbose_name='creator')
    status = models.IntegerField(default=0, db_column='status', verbose_name='order status')
    create_time = models.DateTimeField(auto_now_add=True, db_column='create_time')

    class Meta:
        db_table = 'order'