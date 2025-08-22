from django.db import models


class Testimonial(models.Model):
    author = models.CharField(max_length=255, verbose_name="Имя клиента")
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="Источник отзыва")
    text = models.TextField(verbose_name="Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author} - {self.created_at.strftime('%Y-%m-%d')}"