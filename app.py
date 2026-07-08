import streamlit as st
from fpdf import FPDF

# --- 1. DATOS CENTRALIZADOS ---
# Modifica esta sección cuando necesites actualizar tu hoja de vida
NOMBRE = "SERGIO AMHER CUTIVA MEDINA"
CONTACTO = "Bogotá, Colombia | +57 3208481087 | sergiocutivam@gmail.com"
LINKS = "linkedin.com/in/sergio-cutiva-212320382 | github.com/SergioCutiva"

RESUMEN = (
    "Ingeniero Electricista y Analista de Automatización con experiencia destacada en el desarrollo de "
    "software (Python), integración de sistemas e ingeniería de potencia. Capacidad comprobada para diseñar "
    "herramientas de automatización de procesos corporativos, análisis de datos y extracción de información. "
    "Enfoque orientado a resultados y optimización de eficiencia operativa mediante soluciones tecnológicas."
)

# --- 2. CLASE PARA GENERAR EL PDF (FORMATO HARVARD) ---
class ResumePDF(FPDF):
    def section_title(self, title):
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 8, title.upper(), ln=True)
        # Línea divisoria
        self.line(self.get_x(), self.get_y(), self.get_x() + 190, self.get_y())
        self.ln(3)

    def job_entry(self, title, date, company, location, bullets):
        self.set_font('helvetica', 'B', 11)
        self.cell(130, 6, title)
        self.set_font('helvetica', '', 11)
        self.cell(60, 6, date, ln=True, align='R')
        
        self.set_font('helvetica', 'I', 11)
        self.cell(130, 6, company)
        self.set_font('helvetica', '', 11)
        self.cell(60, 6, location, ln=True, align='R')
        self.ln(1)
        
        self.set_font('helvetica', '', 10)
        for bullet in bullets:
            self.multi_cell(0, 5, chr(149) + " " + bullet)
        self.ln(4)

def generar_pdf():
    pdf = ResumePDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Encabezado
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 8, NOMBRE, ln=True, align='C')
    pdf.set_font('helvetica', '', 10)
    pdf.cell(0, 5, CONTACTO, ln=True, align='C')
    pdf.cell(0, 5, LINKS, ln=True, align='C')
    pdf.ln(6)
    
    # Resumen
    pdf.section_title("Resumen Profesional")
    pdf.set_font('helvetica', '', 10)
    pdf.multi_cell(0, 5, RESUMEN)
    pdf.ln(4)
    
    # Experiencia
    pdf.section_title("Experiencia Profesional")
    bullets_enel = [
        "Desarrollo e implementación de 'Telecontrol Inspection Tool', un sistema automatizado para extraer datos e imágenes de correos de Outlook y generar reportes estructurados en Excel utilizando Python y XlsxWriter.",
        "Ingeniería de herramientas de automatización con Pandas y win32com para la detección de cambios de estado en proyectos (PMS) y distribución automática de notificaciones.",
        "Automatización de flujos de trabajo corporativos en Salesforce mediante Selenium, agilizando la descarga masiva de reportes y la consolidación de la Matriz de Equipos HSEQ.",
        "Creación y despliegue de aplicaciones ejecutables independientes utilizando PyInstaller, implementando interfaces estandarizadas y gestión de errores."
    ]
    pdf.job_entry("Ingeniero Electricista Pasante / Analista de Automatización", "Ene 2026 - Jun 2026", "Enel Colombia", "Bogotá, Colombia", bullets_enel)
    
    bullets_unal = [
        "Monitor de las asignaturas de Circuitos Eléctricos y Dispositivos, brindando soporte técnico y teórico a estudiantes en simulaciones y diseños eléctricos.",
        "Miembro activo del Grupo de Investigación en Recursos Energéticos (GIRE) y GIPEM, participando en estudios técnicos sobre energías renovables y optimización energética.",
        "Ponente seleccionado en la Red Regional de Semilleros de Investigación (RREDSI) 2022, exponiendo modelos de análisis eléctrico."
    ]
    pdf.job_entry("Monitor Académico e Investigador", "2021 - 2025", "Universidad Nacional de Colombia", "Manizales, Colombia", bullets_unal)
    
    # Educación
    pdf.section_title("Educación")
    pdf.job_entry("Pregrado en Ingeniería Eléctrica", "Jun 2026", "Universidad Nacional de Colombia", "", [])
    pdf.job_entry("Curso de Inteligencia Artificial", "2025", "Ministerio TIC - Talento Tech", "", ["Desarrollo de ChatBots, análisis de datos y proyecto de predicción de casos de dengue en el Caquetá."])
    pdf.job_entry("Diplomado en Instalaciones Fotovoltaicas", "2023", "GIPEM - Grupo de investigación", "", ["Dimensionamiento, simulación de modelos teóricos y análisis de sistemas fotovoltaicos en zonas urbanas y rurales."])
    
    # Habilidades
    pdf.section_title("Habilidades Técnicas")
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(55, 5, "Software y Automatización:")
    pdf.set_font('helvetica', '', 10)
    pdf.multi_cell(0, 5, "Python, C++, MATLAB, Selenium, Pandas, XlsxWriter, win32com, PyInstaller, Git, GitHub.")
    
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(55, 5, "Ingeniería Eléctrica:")
    pdf.set_font('helvetica', '', 10)
    pdf.multi_cell(0, 5, "Simulación de generadores/motores, diseño de subestaciones, líneas de transmisión, dimensionamiento fotovoltaico.")
    
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(55, 5, "Idiomas:")
    pdf.set_font('helvetica', '', 10)
    pdf.multi_cell(0, 5, "Español (Nativo), Inglés (Avanzado - 80%).")
    
    # Exportar PDF a bytes
    return pdf.output()

# --- 3. INTERFAZ VISUAL EN STREAMLIT ---
st.set_page_config(page_title="CV | Sergio Cutiva", page_icon="📄", layout="centered")

st.title(NOMBRE)
st.markdown(f"📍 **{CONTACTO}**")
st.markdown(f"🔗 **{LINKS}**")

# Botón de descarga interactivo
st.download_button(
    label="📥 Descargar Hoja de Vida en PDF",
    data=bytes(generar_pdf()),
    file_name="Sergio_Cutiva_CV.pdf",
    mime="application/pdf"
)

st.markdown("---")

st.header("Resumen Profesional")
st.write(RESUMEN)

st.header("Experiencia Profesional")
st.subheader("Enel Colombia | Bogotá, Colombia")
st.markdown("*Ingeniero Electricista Pasante / Analista de Automatización* | Ene 2026 – Jun 2026")
st.markdown("""
- Desarrollo e implementación de 'Telecontrol Inspection Tool', un sistema automatizado para extraer datos e imágenes de correos de Outlook y generar reportes estructurados en Excel utilizando Python y XlsxWriter.
- Ingeniería de herramientas de automatización con Pandas y win32com para la detección de cambios de estado en proyectos (PMS) y distribución automática de notificaciones.
- Automatización de flujos de trabajo corporativos en Salesforce mediante Selenium, agilizando la descarga masiva de reportes y la consolidación de la Matriz de Equipos HSEQ.
- Creación y despliegue de aplicaciones ejecutables independientes utilizando PyInstaller, implementando interfaces estandarizadas y gestión de errores.
""")

st.subheader("Universidad Nacional de Colombia | Manizales, Colombia")
st.markdown("*Monitor Académico e Investigador* | 2021 – 2025")
st.markdown("""
- Monitor de las asignaturas de Circuitos Eléctricos y Dispositivos, brindando soporte técnico y teórico a estudiantes en simulaciones y diseños eléctricos.
- Miembro activo del Grupo de Investigación en Recursos Energéticos (GIRE) y GIPEM, participando en estudios técnicos sobre energías renovables y optimización energética.
- Ponente seleccionado en la Red Regional de Semilleros de Investigación (RREDSI) 2022.
""")

st.header("Educación")
st.write("**Pregrado en Ingeniería Eléctrica** | Universidad Nacional de Colombia | Graduación: Jun 2026")
st.write("**Curso de Inteligencia Artificial** | Ministerio TIC - Talento Tech | 2025")
st.write("**Diplomado en Instalaciones Fotovoltaicas** | GIPEM | 2023")

st.header("Habilidades Técnicas")
st.write("- **Software y Automatización:** Python, C++, MATLAB, Selenium, Pandas, XlsxWriter, win32com, PyInstaller, Git, GitHub.")
st.write("- **Ingeniería Eléctrica:** Simulación de generadores/motores, diseño de subestaciones, flujo de cargas, dimensionamiento fotovoltaico.")
st.write("- **Idiomas:** Español (Nativo), Inglés (Avanzado - 80%).")
