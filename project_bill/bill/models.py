from django.db import models


class Account(models.Model):
    name = models.CharField(
        verbose_name='Имя пользователя',
        blank=False,
        max_length=200,
        help_text='Укажите имя пользователя'
    )

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(
        verbose_name='Имя сервиса',
        blank=False,
        max_length=200,
        help_text='Укажите имя сервиса'
    )

    class Meta:
        verbose_name = 'Сервис',
        verbose_name_plural = 'Сервисы'
        ordering = ['id'] 
    
    def __str__(self):
        return self.name


class Period(models.Model):
    month = models.CharField(
        verbose_name='Месяц',
        blank=False,
        max_length=200,
        help_text='Укажите месяц'
    )

    def __str__(self):
        return self.month


class Bill(models.Model):
    account_id = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Клиент'
    )
    period_id = models.ForeignKey(
        Period,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Период'
    )


class Bill_det(models.Model):
    bill_id = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        blank=False,
        related_name='bill_dets',
        verbose_name='Квитанция'
    )
    service_id = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Сервис'
    )
    value = models.DecimalField(
        verbose_name='Стоимость сервиса',
        blank=False,
        max_digits=12,
        decimal_places=2
    )

    class Meta:
        ordering = ['bill_id']

    def __str__(self):
        return '%s: %d' % (self.service_id, self.value)


class Bill_adj(models.Model):
    account_id = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Клиент'
    )
    bill_id = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Квитанция',
        related_name='bill_adj',
    )
    service_id = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Сервис'
    )
    value = models.DecimalField(
        verbose_name='Стоимость квитанции',
        blank=False,
        max_digits=12,
        decimal_places=2
    )


class Payment(models.Model):
    account_id = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Клиент'
    )
    period_id = models.ForeignKey(
        Period,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Период'
    )
    value = models.DecimalField(
        verbose_name='Стоимость квитанции',
        blank=False,
        max_digits=12,
        decimal_places=2
    )

class Balance(models.Model):
    account_id = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Клиент'
    )
    bill_id = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Квитанция',
        related_name='balance',
    )
    service_id = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Сервис'
    )
    value = models.DecimalField(
        verbose_name='Стоимость квитанции',
        blank=False,
        max_digits=12,
        decimal_places=2
    )    