from django.db import models

#podemos aqui guarda las conversaciones y cada mensaje con su emocion detectada
class Conversation(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    ultima_emocion = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Conversación {self.id}"


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=10)  # "user" o "bot"
    texto = models.TextField()
    emocion = models.CharField(max_length=50, blank=True, null=True)
    respuesta_de_bot = models.TextField(blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.texto[:30]}"