from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Conversation, Message
from django.shortcuts import render
import random

EMOCIONES = {
    "triste": "tristeza",
    "feliz": "alegría",
    "rabia": "enojo",
    "molesto": "enojo",
    "cansado": "cansado",
    "solo": "soledad",
    "ansioso": "ansiedad",
    "estresado": "estrés",
    "gracias": "agradecimiento",
    "te lo agradezco": "agradecimiento",
    "muchas gracias": "agradecimiento",
    "triste": "tristeza",
    "tiste": "tristeza",
    "deprimido": "tristeza",
    "llorando": "tristeza",
    "me duele": "tristeza",
    "nostálgico": "tristeza",
    "mal": "tristeza",
    "vacio": "tristeza",
    "feliz": "alegría",
    "contento": "alegría",
    "emocionado": "alegría",
    "bien": "alegría",
    "motivado": "alegría",
    "animado": "alegría",
    "enojado": "enojo",
    "rabia": "enojo",
    "furioso": "enojo",
    "molesto": "enojo",
    "fastidiado": "enojo",
    "frustrado": "enojo",
    "ansioso": "ansiedad",
    "nervioso": "ansiedad",
    "preocupado": "ansiedad",
    "tenso": "ansiedad",
    "inquieto": "ansiedad",
    "estresado": "estres",
    "abrumado": "estres",
    "saturado": "estres",
    "agobiado": "estres",
    "cansado": "cansado",
    "agotado": "cansado",
    "sin energía": "cansado",
    "quemado": "cansado",
    "solo": "soledad",
    "solitario": "soledad",
    "me siento aislado": "soledad",
    "nadie me entiende": "soledad",
    "suicid": "alerta",
    "matarme": "alerta",
    "no quiero vivir": "alerta",
    "quiero morir": "alerta",
    "lastimarme": "alerta",
    "hacerme daño": "alerta",
    "desaparecer": "alerta",
    "quitarme la vida": "alerta",
    "no valgo nada": "alerta",
    "ya no aguanto": "alerta",
    "todo sería mejor sin mí": "alerta",
    "gracias": "agradecimiento",
    "te lo agradezco": "agradecimiento",
    "muchas gracias": "agradecimiento",
    "grax": "agradecimiento",
    "ty": "agradecimiento",  # gamers 😂
    "gracias": "agradecimiento",
}

PALABRAS_ALARMA = [
    "matarme", "suicid", "no quiero vivir", "quiero morir",
    "hacerme daño", "lastimarme", "desaparecer", "quitarme la vida"
]

RESPUESTA_ALERTA = (
    "Lamento mucho que te sientas así. No estás solo. "
    "Quiero que hables con alguien que pueda ayudarte de verdad.\n\n"
    "📞 Línea 106 – Línea de Atención a la Vida (Colombia)\n"
    "📱 WhatsApp de apoyo emocional: 301 754 8933\n"
    "🆘 Línea Nacional 01 8000 113 113\n\n"
    "Estoy aquí contigo, pero por favor busca ayuda profesional también."
)

RESPUESTAS = {
    "tristeza": [
        "Lamento que te sientas triste. ¿Quieres hablar sobre ello?",
        "La tristeza es una emoción natural. Estoy aquí para escucharte.",
        "Si quieres, podemos hablar de lo que te hace sentir así.",
        "Lamento que te sientas así… ¿Quieres contarme qué pasó?",
        "Suena duro… Estoy aquí para escucharte."
    ],
    "alegría": [
        "¡Me alegra escuchar eso! ¿Qué te hace sentir tan feliz?",
        "¡Eso es genial! La felicidad es contagiosa.",
        "¡Qué bueno que te sientas así! ¿Quieres compartir más?",
        "¡Fantástico! La alegría es una emoción maravillosa.",
        "¡Me encanta escuchar noticias felices!"
    ],
    "enojo": [
        "Entiendo que estés molesto. ¿Quieres hablar sobre lo que te está causando enojo?",
        "El enojo es una emoción válida. Estoy aquí para escucharte.",
        "Si quieres, podemos hablar de lo que te hace sentir así.",
        "Lamento que te sientas así… ¿Quieres contarme qué pasó?",
        "Suena frustrante… Estoy aquí para escucharte."
    ],
    "ansiedad": [
        "La ansiedad puede ser abrumadora. ¿Quieres hablar sobre lo que te preocupa?",
        "Estoy aquí para escucharte. La ansiedad es una emoción común.",
        "Si quieres, podemos hablar de lo que te hace sentir así.",
        "Lamento que te sientas así… ¿Quieres contarme qué pasó?",
        "Suena difícil… Estoy aquí para escucharte."
    ],
    "soledad": [
        "La soledad puede ser difícil. ¿Quieres hablar sobre cómo te sientes?",
        "Estoy aquí para escucharte. La soledad es una emoción común.",
        "Si quieres, podemos hablar de lo que te hace sentir así.",
        "Lamento que te sientas así… ¿Quieres contarme qué pasó?",
        "Suena duro… Estoy aquí para escucharte."
    ],
    "estrés": [
        "El estrés puede ser abrumador. ¿Quieres hablar sobre lo que te preocupa?",
        "Estoy aquí para escucharte. El estrés es una emoción común.",
        "Si quieres, podemos hablar de lo que te hace sentir así.",
        "Lamento que te sientas así… ¿Quieres contarme qué pasó?",
        "Suena difícil… Estoy aquí para escucharte."
    ],
    "cansado": [
        "El cansancio puede afectar mucho. ¿Quieres hablar sobre lo que te está agotando?",
        "Estoy aquí para escucharte. El cansancio es una emoción común.",
        "Si quieres, podemos hablar de lo que te hace sentir así.",
        "Lamento que te sientas así… ¿Quieres contarme qué pasó?",
        "Suena agotador… Estoy aquí para escucharte."
    ],
    "desconocida": [
        "No estoy seguro de cómo responder a eso, pero estoy aquí para escucharte.",
        "Esa es una emoción interesante. ¿Quieres contarme más?",
        "No estoy familiarizado con esa emoción, pero estoy aquí para ti.",
        "Suena complicado… Estoy aquí para escucharte.",
        "Estoy aquí para ti, sin importar cómo te sientas.",
    ],
    "agradecimiento": [
        "Me alegra ayudarte 💛",
        "Aquí estoy cuando me necesites.",
        "Gracias a ti por confiar en mí.",
        "Estoy aquí contigo para lo que necesites."
    ],
}


def detectar_emocion(texto):
    if not texto:
        return "neutral"

    texto_lower = texto.lower()

    # 🔥 detectar palabras de riesgo
    for alarma in PALABRAS_ALARMA:
        if alarma in texto_lower:
            return "alarma"

    for palabra, emocion in EMOCIONES.items():
        if palabra in texto_lower:
            return emocion

    return "desconocida"

def generar_respuesta(emocion):
    return random.choice(RESPUESTAS.get(emocion, RESPUESTAS["desconocida"]))


@api_view(["POST"])
def chatbot(request):
    texto = request.data.get("message")

    if not texto:
        return Response({"error": "No se envió texto"}, status=400)

    emocion = detectar_emocion(texto)

    # ⚠ Respuesta especial si está MUY mal
    if emocion == "alarma":
        return Response({"response": RESPUESTA_ALERTA, "emotion": "alarma"})

    respuesta = generar_respuesta(emocion)
    return Response({"response": respuesta, "emotion": emocion})

def chat_view(request):
    return render(request, 'frontend/index.html')
