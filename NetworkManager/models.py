from django.db import models


NULLABLE = {'blank': True, 'null': True}

class Contact(models.Model):
    email = models.EmailField(verbose_name='почта')
    country = models.CharField(verbose_name='страна', max_length=32)
    city = models.CharField(verbose_name='город', max_length=64)
    street = models.CharField(verbose_name='улица', max_length=128)
    house = models.CharField(verbose_name='номер дома', max_length=8)

    class Meta:
        verbose_name = 'Контактная информация'

    def __str__(self) -> str:
        return f"{self.country}"


class Product(models.Model):
    name = models.CharField(verbose_name='название продукта', max_length=64)
    model = models.CharField(verbose_name='название модели', max_length=64)
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class NetworkNode(models.Model):
    class NodeType(models.TextChoices):
        FACTORY = "FC", "Завод"
        RETAIL_NETWORK = "RN", "Розничная сеть"
        INDIVIDUAL_ENTREPRENEUR = "IE", "Индивидуальный предприниматель"

    name = models.CharField(verbose_name='название звена', max_length=128)
    contacts = models.ForeignKey(Contact, verbose_name='контакт', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    provider = models.ForeignKey('self', verbose_name='поставщик', **NULLABLE , on_delete=models.CASCADE)
    node_type = models.CharField(verbose_name='тип звена', choices=NodeType, max_length=128)
    debt = models.DecimalField(verbose_name='задолжность', decimal_places=2, max_digits=12)
    created_at = models.DateTimeField(verbose_name='дата и время создания',auto_now_add=True)

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'
