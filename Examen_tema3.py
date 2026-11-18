import streamlit as st
from PIL import Image,ImageOps,ImageFilter,ImageEnhance,ImageDraw
import io

st.set_page_config(page_title="ID_Gen Pro",layout="wide")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("🪪 ID-Gen Pro")
    st.caption("Proyecto Final: Generador de Identidad Corporativa")

with col1:
    st.header(":material/settings: Configuración")
    nombre = st.text_input("Nombre Completo")
    cargo = st.text_input("Cargo")
    empleado_id = st.text_input("Número de Empleado")

    st.subheader("🎨 Estética")
    color_marca = st.color_picker(
        "Color de la Marca",
        "#30458C"
    )

    st.subheader("📷 Multimedia")
    foto = st.file_uploader(
        "Subir foto de perfil",
        type=["jpg", "jpeg", "png"]
    )

if foto is not None:
    st.success("Fotografía cargada correctamente")
else:
    st.info("Por favor, sube una fotografía para generar el carnet")


with col2:
    col_vista, col_exportar = st.columns(2)
    
    with col_vista:
        st.subheader("Vista Previa")

        if foto is not None:
            carnet = Image.new("RGB", (400, 600), "white")
            draw = ImageDraw.Draw(carnet)

            draw.rectangle((0, 0, 400, 150), fill=color_marca)
            imagen = Image.open(foto)
            imagen = imagen.resize((150, 150))
            carnet.paste(imagen, (125, 100))
            draw.text((125, 280), nombre, fill="black")
            draw.text((125, 320), cargo, fill="gray")
            draw.text((125, 360), empleado_id, fill="black")

            st.image(carnet, use_container_width=True)

            buffer = io.BytesIO()
            carnet.save(buffer, format="PNG")

    with col_exportar:
        st.subheader("Exportar")

        if foto is not None:
            st.download_button(
                "📥 Descargar Credencial",
                data=buffer.getvalue(),
                file_name=f"carnet_{nombre}.png",
                mime="image/png"
            )    