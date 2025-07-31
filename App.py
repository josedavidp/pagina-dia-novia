import streamlit as st
from PIL import Image
import random

# Configuración general
st.set_page_config(page_title="Feliz Día, Amor ❤️", layout="centered")

# Título y presentación
st.title("💖 ¡Feliz Día de la Novia! 💖")
st.markdown("## Para la persona más especial del mundo 🌹")

# Imagen principal
image = Image.open("imagenes/Pareja.JPEG")
st.image(image, caption="Te amo muchísimo 😘", width=400)

# Mensaje inicial
st.markdown("""
### 🌟 Mi Mensaje Para Ti
Hoy quiero recordarte lo increíble que eres. Tu sonrisa, tu ternura, y tu amor llenan mi vida de alegría.  
Gracias por estar a mi lado, por ser mi compañera, mi mejor amiga y mi motor de cada día.

**¡Feliz día, mi vida!**
""")

# Galería
st.markdown("### 🖼️ Algunos Momentos Juntos")

cols = st.columns(3)
images = ["imagenes/2021.jpg", "imagenes/Cuenca.jpg", "imagenes/Halloween.jpg"]
for i, img in enumerate(images):
    with cols[i]:
        st.image(img, use_container_width=True)

# Botón sorpresa
st.markdown("### 🎁 Una Sorpresita...")

if st.button("Haz clic para ver algo lindo 💌"):
    frase = random.choice([
        "Eres la mejor parte de mi vida.",
        "Tu amor me hace mejor cada día.",
        "No importa el lugar, mientras sea contigo.",
        "Te amo hoy, mañana y siempre ❤️",
        "Mi lugar favorito es donde estés tú."
    ])
    
    st.success(frase)

    # 🎈 Animación de corazones
    st.markdown("""
    <style>
    .hearts {
        font-size: 30px;
        animation: float 2s ease-in-out infinite;
    }
    @keyframes float {
        0% { transform: translateY(0); opacity: 1; }
        50% { transform: translateY(-20px); opacity: 0.7; }
        100% { transform: translateY(0); opacity: 1; }
    }
    </style>
    <div class="hearts">💖 💕 ❤️ 💓 💘</div>
    """, unsafe_allow_html=True)

    # 🎬 Video con tamaño reducido (manual)
    st.markdown("### 🎥 Mira este video:")
    st.video("https://drive.google.com/uc?export=download&id=1cmqTdsNer43w_pBKTaiH9Xij5sfjWu4T")
    
    # Si vas a desplegar en Streamlit Cloud, reemplaza esta línea por:
    # st.video("https://dl.dropboxusercontent.com/s/abc123xyz/mi_video.mp4")
    
    # 🎉 Animación adicional con globos
    st.balloons()

st.markdown("### 🧠 ¿Cuánto recuerdas de nosotros?")

p1 = st.radio("¿Dónde fue nuestra primera salida?", ["Parque", "Cine", "Comida Fit", "Tu casa"])
p2 = st.radio("¿Cuál es mi apodo para ti?", ["Karen", "Monse", "Mi niña", "Osita"])
p3 = st.radio("¿Qué día comenzamos nuestra relación?", ["14 de febrero", "21 de junio", "18 de diciembre", "5 de mayo"])

if st.button("Verificar mis respuestas ❤️"):
    correctas = (p1 == "Comida Fit") + (p2 == "Mi niña") + (p3 == "18 de diciembre")
    st.success(f"¡Adivinaste {correctas} de 3 preguntas! 🥰")
    if correctas == 3:
        st.balloons()

# Mensaje Oculto
st.markdown("### 🔐 Mensaje Secreto")

clave = st.text_input("Escribe la palabra mágica para desbloquear algo especial...")

if clave.lower() == "ratoncita":
    st.success("💖 Este amor que siento por ti no tiene límites. Gracias por existir.")
    st.image("imagenes/Sorpresa.jpg", width=300)


# Footer
st.markdown("---")
st.markdown("Hecho con amor por José y dedicado a mi hermosa novia. ❤️")
