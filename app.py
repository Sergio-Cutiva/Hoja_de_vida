import streamlit as st
import base64

# Configuración inicial de la página
st.set_page_config(page_title="CV | Sergio Cutiva", page_icon="📄", layout="centered")

def get_pdf_download_button(file_path, file_name):
    """Función para codificar el PDF y generar un botón de descarga en HTML."""
    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'''
        <a href="data:application/pdf;base64,{base64_pdf}" download="{file_name}" 
           style="background-color: #0E1117; color: white; padding: 0.6em 1.2em; 
                  text-decoration: none; border-radius: 4px; border: 1px solid #4B4B4B; 
                  font-weight: bold; display: inline-block; text-align: center;">
           Descargar Hoja de Vida (PDF)
        </a>
        '''
        return pdf_display
    except FileNotFoundError:
        return "<p style='color:red;'>El archivo PDF no se encuentra en el directorio.</p>"

# Cabecera
st.title("Sergio Amher Cutiva Medina")
st.markdown("**Ingeniero Electricista | Analista de Automatización | Desarrollador Python**")
st.markdown("📍 Bogotá, Colombia | 📱 +57 3208481087 | ✉️ sergiocutivam@gmail.com")
st.markdown("[LinkedIn](https://www.linkedin.com/in/sergio-cutiva-212320382) | [GitHub](https://github.com/SergioCutiva)")

st.markdown("---")

# Botón de descarga PDF (Debe existir el archivo 'Hoja_de_Vida_Sergio_Cutiva_Harvard.pdf' en la misma carpeta)
st.markdown(get_pdf_download_button("Hoja_de_Vida_Sergio_Cutiva_Harvard.pdf", "Sergio_Cutiva_CV.pdf"), unsafe_allow_html=True)

st.markdown("---")

# Resumen
st.header("Resumen Profesional")
st.write("""
Ingeniero Electricista y Analista de Automatización con experiencia destacada en el desarrollo de software (Python), integración de sistemas e ingeniería de potencia. Capacidad comprobada para diseñar herramientas de automatización de procesos corporativos, análisis de datos y extracción de información.
""")

# Experiencia
st.header("Experiencia Profesional")

st.subheader("Enel Colombia | Bogotá, Colombia")
st.markdown("*Ingeniero Electricista Pasante / Analista de Automatización* | Ene 2026 – Jun 2026")
st.write("""
- Desarrollo e implementación de "Telecontrol Inspection Tool", sistema automatizado para extraer datos e imágenes de correos de Outlook y generar reportes en Excel mediante Python y XlsxWriter.
- Ingeniería de herramientas de automatización con Pandas y win32com para la detección de cambios de estado en proyectos (PMS) y distribución automática de notificaciones.
- Automatización de flujos de trabajo en Salesforce mediante Selenium, agilizando la descarga masiva de reportes y consolidación de la Matriz de Equipos HSEQ.
- Creación de aplicaciones ejecutables independientes con PyInstaller implementando interfaces estandarizadas.
""")

st.subheader("Universidad Nacional de Colombia | Manizales, Colombia")
st.markdown("*Monitor Académico e Investigador* | 2021 – 2025")
st.write("""
- Monitor de Circuitos Eléctricos y Dispositivos, brindando soporte en simulaciones y diseños eléctricos.
- Miembro activo del Grupo de Investigación en Recursos Energéticos (GIRE) y GIPEM.
- Ponente seleccionado en la Red Regional de Semilleros de Investigación (RREDSI) 2022.
""")

# Educación
st.header("Educación")
st.write("**Pregrado en Ingeniería Eléctrica** | Universidad Nacional de Colombia | Graduación: Jun 2026")
st.write("**Curso de Inteligencia Artificial** | Ministerio TIC - Talento Tech | 2025")
st.write("**Diplomado en Instalaciones Fotovoltaicas** | GIPEM | 2023")

# Habilidades
st.header("Habilidades Técnicas")
st.write("- **Desarrollo y Automatización:** Python, C++, MATLAB, Selenium, Pandas, XlsxWriter, win32com, PyInstaller, Git, GitHub.")
st.write("- **Ingeniería Eléctrica:** Simulación de generadores/motores, diseño de subestaciones, flujo de cargas, diseño fotovoltaico.")
st.write("- **Idiomas:** Español (Nativo), Inglés (Avanzado - 80%).")