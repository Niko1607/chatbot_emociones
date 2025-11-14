# 🧠 Chatbot Emocional — Detección de Emociones con IA

Asistente conversacional capaz de detectar emociones en texto y responder de forma empática.

---

## 📌 Descripción del proyecto

Este proyecto es un chatbot emocional diseñado para analizar el mensaje del usuario, identificar la emoción presente y responder de forma empática, brindando apoyo emocional básico.

🔧 El sistema combina:

- **Django + Django REST Framework** para la API  
- **Frontend simple en HTML, CSS y JavaScript** tipo chat  
- **Detector de emociones** basado en coincidencia semántica (palabras clave)  
- **Módulo de respuestas empáticas dinámicas**  
- **Sistema de alertas** para palabras de riesgo (autolesiones o peligro)  
- **Base de datos MySQL** para guardar conversaciones y mensajes  

> ⚠️ Este chatbot NO reemplaza ayuda profesional, pero sirve como acompañante emocional básico.

---

## 🎯 Objetivos del proyecto

- 🧠 Identificar emociones principales en mensajes de texto  
- 💬 Generar respuestas automáticas empáticas  
- 🔄 Mantener conversaciones de forma fluida  
- 🗂️ Guardar historial de chats en base de datos  
- 🚨 Detectar palabras de alerta y enviar mensajes de ayuda reales  
- 🖥️ Crear una interfaz amigable para el usuario final  

---

## 🛠️ Tecnologías utilizadas

### 🔙 Backend

- 🐍 Python  
- 🌐 Django  
- 🔧 Django REST Framework  
- 🗄️ MySQL / MariaDB  
- 🗃️ Git & GitHub  

### 🔜 Frontend

- 🧾 HTML5  
- 🎨 CSS3  
- ⚙️ JavaScript (fetch API)  

### 🧪 Entorno

- 🧬 Entorno virtual con `venv`

---

## 🧩 Arquitectura del sistema

```
📂 chatbot_emociones
├── 📂 detector            # Proyecto Django
│    ├── settings.py
│    ├── urls.py
│    └── ...
├── 📂 api                 # App Django con la lógica del chatbot
│    ├── models.py         # Conversation y Message
│    ├── views.py          # Lógica del chatbot + detector
│    ├── urls.py
│    └── serializers.py    # (opcional)
├── 📂 frontend
│    ├── index.html
│    ├── style.css
│    └── script.js
└── README.md
```

---

## 🤖 Funcionamiento del Chatbot

🔍 El sistema analiza el mensaje y busca palabras relacionadas con una emoción usando un diccionario como:

```python
EMOCIONES = {
    "triste": "tristeza",
    "feliz": "alegría",
    "rabia": "enojo",
    "molesto": "enojo",
    "solo": "soledad",
    "ansioso": "ansiedad",
    "estresado": "estrés",
}
```

💬 Luego selecciona una respuesta aleatoria como:

```python
RESPUESTAS["tristeza"] → “Lamento que te sientas así. ¿Quieres contarme qué pasó?”
```

🚨 Si el usuario escribe palabras de riesgo como:

- "matarme", "suicid", "no quiero vivir", "lastimarme", etc…

🔔 El sistema devuelve un mensaje especial con líneas de ayuda reales.

⚠️ Sistema de alerta emocional (riesgo):

```python
PALABRAS_ALARMA = ["suicid", "matarme", "no quiero vivir", "desaparecer", ...]
```

📢 Y responde con:

- 📞 Línea 106 – Atención a la Vida (Colombia)
- 📱 WhatsApp: 301 754 8933
- 🆘 Línea Nacional 01 8000 113 113

---

## 💾 Base de datos

El sistema guarda:

- 🗨️ **Conversation**
  - id
  - fecha de creación

- 💬 **Message**
  - usuario/bot
  - texto
  - emoción detectada
  - conversacion_id

🔁 Esto permite reconstruir cualquier chat.

---

## 🚀 Cómo ejecutar el proyecto

1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Niko1607/chatbot_emociones.git
```

2️⃣ Crear el entorno virtual

```bash
python -m venv venv
```

3️⃣ Activar el entorno

- En Windows:
  ```bash
  venv\Scripts\activate
  ```
- En Linux/Mac:
  ```bash
  source venv/bin/activate
  ```

4️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

5️⃣ Configurar base de datos MySQL en `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "emociones_db",
        "USER": "root",
        "PASSWORD": "tu_pass",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

6️⃣ Migrar

```bash
python manage.py migrate
```

7️⃣ Ejecutar servidor

```bash
python manage.py runserver
```

8️⃣ Abrir el chat

Visita 🌐 [http://127.0.0.1:8000/api/chat/](http://127.0.0.1:8000/api/chat/)

---

## 🖥️ Vista del chatbot

- 💬 Interfaz minimalista
- 🧼 Burbujas de conversación
- 🔄 Scroll automático
- ⚡ Interacción en tiempo real

---

## 🌟 Características futuras

- 🤖 Integrar modelo de IA real (transformers, embeddings, etc.)
- 🧠 Mejores detecciones con NLP
- 👤 Historial por usuario
- 📱 Interfaz móvil
- 📊 Dashboard para psicólogos
- 📤 Exportar conversaciones

---

## 👨‍💻 Autor

**Nikotica** (Niko Moreno)  
💻 Desarrollador – Programador – Apasionado por IA y tecnología  
🔗 GitHub: [https://github.com/Niko1607](https://github.com/Niko1607)

---
## 👀 ¿Quieres ver el proyecto desplegado?

Accede aquí: [frontend-vercel-mm6cr6hwo-niko2745s-projects.vercel.app](https://frontend-vercel-mm6cr6hwo-niko2745s-projects.vercel.app)

## 📜 Licencia

Este proyecto es de uso académico y de aprendizaje.  
❌ No apto como reemplazo de asistencia psicológica profesional.
