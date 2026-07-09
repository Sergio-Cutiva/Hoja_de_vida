import streamlit as st
from fpdf import FPDF

# --- 1. DATOS CENTRALIZADOS ---
NOMBRE = "SERGIO AMHER CUTIVA MEDINA"
CONTACTO = "Bogotá, Colombia | +57 3208481087 | sergiocutivam@gmail.com"
LINKS = "linkedin.com/in/sergio-cutiva-212320382 | github.com/SergioCutiva"

RESUMEN = (
    "Candidato a Ingeniero Electricista enfocado en la ingeniería de datos, automatización de procesos "
    "y el desarrollo de soluciones tecnológicas corporativas. Experiencia comprobada en el despliegue de "
    "aplicativos web (dashboards), aplicación de inteligencia artificial para extracción de información y el "
    "cruce masivo de bases de datos. Habilidad integral combinando desarrollo de software (Python) con "
    "supervisión operativa en terreno y gestión de activos en el sector energético."
)

# --- 2. CLASE PARA GENERAR EL PDF (FORMATO HARVARD) ---
class ResumePDF(FPDF):
    def section_title(self, title):
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 8, title.upper())
        self.ln(8)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(3)

    def job_entry(self, title, date, company, location, bullets):
        self.set_font('helvetica', 'B', 11)
        self.cell(130, 6, title)
        
        self.set_font('helvetica', '', 11)
        self.cell(0, 6, date, align='R')
        self.ln(6) 
        
        self.set_font('helvetica', 'I', 11)
        self.cell(130, 6, company)
        
        self.set_font('helvetica', '', 11)
        self.cell(0, 6, location, align='R')
        self.ln(6) 
        self.ln(1) 
        
        self.set_font('helvetica', '', 10)
        for bullet in bullets:
            self.set_x(self.l_margin)
            self.multi_cell(0, 5, "- " + bullet)
        self.ln(4)

def generar_pdf():
    pdf = ResumePDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Encabezado
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 8, NOMBRE, align='C')
    pdf.ln(8)
    
    pdf.set_font('helvetica', '', 10)
    pdf.cell(0, 5, CONTACTO, align='C')
    pdf.ln(5)
    
    pdf.cell(0, 5, LINKS, align='C')
    pdf.ln(10)
    
    # Resumen
    pdf.section_title("Resumen Profesional")
    pdf.set_font('helvetica', '', 10)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, 5, RESUMEN)
    pdf.ln(4)
    
    # Experiencia
    pdf.section_title("Experiencia Profesional")
    bullets_enel = [
        "Ingeniería de datos (Python, Pandas) para la limpieza y cruce masivo de bases de datos operativas, integrando extracción automatizada (Selenium) desde sistemas como PMS y Salesforce.",
        "Desarrollo de aplicativos web y dashboards (Streamlit) para el análisis de información y la gestión logística en tiempo real de la flota vehicular, integrando notificaciones automáticas.",
        "Experiencia operativa en terreno realizando interventoría, inspección de redes de media tensión y validación financiera de presupuestos, actas de obra y cobros de firmas contratistas (Magnex, Deltec).",
        "Implementación de algoritmos analíticos para la extracción estructurada de datos técnicos (texto e imágenes) desde correos de telecontrol, facilitando la auditoría y toma de decisiones gerenciales.",
        "Desarrollo y empaquetado de automatizaciones independientes (PyInstaller) orientadas a la optimización del control de activos y seguimiento de mantenimientos programados."
    ]
    pdf.job_entry("Analista de Datos y Automatización / Pasante Mantenimiento Programado", "Ene 2026 - Jul 2026", "Enel Colombia", "Bogotá, Colombia", bullets_enel)
    
    bullets_unal = [
        "Monitor Académico de las asignaturas de Circuitos Eléctricos y Dispositivos, instruyendo a estudiantes en el uso de software de simulación y lenguajes de programación (C++, Python, MATLAB).",
        "Miembro activo del Grupo de Investigación en Recursos Energéticos (GIRE) y GIPEM, ejecutando estudios técnicos enfocados en energías renovables y optimización energética.",
        "Ponente seleccionado en la Red Regional de Semilleros de Investigación (RREDSI) 2022, exponiendo modelos computacionales de análisis eléctrico."
    ]
    pdf.job_entry("Investigador y Monitor Académico", "2021 - 2025", "Universidad Nacional de Colombia", "Manizales, Colombia", bullets_unal)
    
    # Educación
    pdf.section_title("Educación")
    pdf.job_entry("Pregrado en Ingeniería Eléctrica", "Graduación esperada: Ago 2026", "Universidad Nacional de Colombia", "", [])
    pdf.job_entry("Curso de Inteligencia Artificial", "2025", "Ministerio TIC - Talento Tech", "", ["Desarrollo de ChatBots, análisis de datos y proyectos de predicción analítica."])
    pdf.job_entry("Diplomado en Instalaciones Fotovoltaicas", "2023", "GIPEM - Grupo de investigación", "", ["Dimensionamiento, simulación de modelos teóricos y análisis de sistemas fotovoltaicos en zonas urbanas y rurales."])
    
    # Habilidades Técnicas
    pdf.section_title("Habilidades Técnicas")
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(55, 5, "Software y Automatización:")
    pdf.set_font('helvetica', '', 10)
    pdf.multi_cell(0, 5, "Python, C++, MATLAB, Selenium, Pandas, XlsxWriter, win32com, PyInstaller, Git, GitHub.")
    pdf.ln(2)
    
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(55, 5, "Ingeniería Eléctrica:")
    pdf.set_font('helvetica', '', 10)
    pdf.multi_cell(0, 5, "Simulación de generadores/motores, diseño de subestaciones, flujo de cargas, dimensionamiento fotovoltaico. Software especializado: ATP, ETAP, AutoCAD.")
    pdf.ln(2)
    
    return pdf.output()

# --- 3. INTERFAZ VISUAL EN STREAMLIT ---
st.set_page_config(page_title="CV | Sergio Cutiva", page_icon="📄", layout="centered")

st.title(NOMBRE)
st.markdown(f"📍 **Bogotá, Colombia** | 📱 **+57 3208481087** | ✉️ **sergiocutivam@gmail.com**")
st.markdown(f"🔗 **[LinkedIn](https://www.linkedin.com/in/sergio-cutiva-212320382) | [GitHub](https://github.com/SergioCutiva)**")

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
st.markdown("*Analista de Datos y Automatización / Pasante Mantenimiento Programado* | Ene 2026 – Jul 2026")
st.markdown("""
- Ingeniería de datos (Python, Pandas) para la limpieza y cruce masivo de bases de datos operativas, integrando extracción automatizada (Selenium) desde sistemas como PMS y Salesforce.
- Desarrollo de aplicativos web y dashboards (Streamlit) para el análisis de información y la gestión logística en tiempo real de la flota vehicular, integrando notificaciones automáticas.
- Experiencia operativa en terreno realizando interventoría, inspección de redes de media tensión y validación financiera de presupuestos, actas de obra y cobros de firmas contratistas (Magnex, Deltec).
- Implementación de algoritmos analíticos para la extracción estructurada de datos técnicos (texto e imágenes) desde correos de telecontrol, facilitando la auditoría y toma de decisiones gerenciales.
- Desarrollo y empaquetado de automatizaciones independientes (PyInstaller) orientadas a la optimización del control de activos y seguimiento de mantenimientos programados.
""")

st.subheader("Universidad Nacional de Colombia | Manizales, Colombia")
st.markdown("*Investigador y Monitor Académico* | 2021 – 2025")
st.markdown("""
- Monitor Académico de las asignaturas de Circuitos Eléctricos y Dispositivos, instruyendo a estudiantes en el uso de software de simulación y lenguajes de programación (C++, Python, MATLAB).
- Miembro activo del Grupo de Investigación en Recursos Energéticos (GIRE) y GIPEM, ejecutando estudios técnicos enfocados en energías renovables y optimización energética.
- Ponente seleccionado en la Red Regional de Semilleros de Investigación (RREDSI) 2022, exponiendo modelos computacionales de análisis eléctrico.
""")

st.header("Educación")
st.write("**Pregrado en Ingeniería Eléctrica** | Universidad Nacional de Colombia | Graduación esperada: Ago 2026")
st.write("**Curso de Inteligencia Artificial** | Ministerio TIC - Talento Tech | 2025")
st.write("**Diplomado en Instalaciones Fotovoltaicas** | GIPEM | 2023")

st.header("Habilidades Técnicas")
st.write("- **Software y Automatización:** Python, C++, MATLAB, Selenium, Pandas, XlsxWriter, win32com, PyInstaller, Git, GitHub.")
st.write("- **Ingeniería Eléctrica:** Simulación de generadores/motores, diseño de subestaciones, flujo de cargas, dimensionamiento fotovoltaico. Software especializado: ATP, ETAP, AutoCAD.")
