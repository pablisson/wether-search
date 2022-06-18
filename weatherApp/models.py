from django.db import models
from uuid import uuid4

class ClimaTempo(models.Model):
    """
    Classe que representa a tabela ClimaTempo do banco de dados.
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    data = models.DateField(auto_now=True)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    pressao = models.DecimalField(max_digits=5, decimal_places=2)
    humidade = models.DecimalField(max_digits=5, decimal_places=2)
    vento = models.DecimalField(max_digits=5, decimal_places=2)
    umidade = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Clima Tempo'
        verbose_name_plural = 'Climas Tempo'
        ordering = ['-created_at']
        db_table = 'clima_tempo'
        managed = True
        default_permissions = ()
        permissions = (
            ('view_climatempo', 'Can view clima_tempo'),
        )