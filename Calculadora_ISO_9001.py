import streamlit as st

# --- Configuración de la página ---
st.set_page_config(
    page_title="Calculadora ISO 9001",
    page_icon="⏱️"
)

# --- Título y Descripción ---
st.title('⏱️ Calculadora de Tiempo para Implementación ISO 9001:2015')
st.markdown("""
Esta calculadora te ayudará a estimar el tiempo necesario para tu proyecto de implementación de la Norma ISO 9001.

**Importante:** Por favor, introduce los datos considerando únicamente el **alcance de tu SGC (Sistema de Gestión de la Calidad)**. Si el alcance es menor que la empresa completa, no introduzcas los datos de toda la compañía.
""")
st.info("Nota: Tu información es privada y no será compartida con nadie.")

# --- Cuestionario ---

st.header("Cuestionario del Proyecto")

# 1. Número de empleados
opciones_empleados = ('1 a 20', '21 a 50', '51 a 100', '101 a 500', '501 o más')
respuesta_empleados = st.selectbox('Número de empleados dentro del alcance:', opciones_empleados)

# 2. Número de sedes
opciones_sedes = ('1', '2 a 5', '6 a 20', '21 o más')
respuesta_sedes = st.selectbox('Número de sedes físicas:', opciones_sedes)

# 3. Documentación existente
opciones_docs = (
    'No, no tenemos información documentada.',
    'Sí, pero solo alguna información (listas de chequeo, instructivos, etc.).',
    'Sí, la mayoría de nuestra información relevante está documentada.'
)
respuesta_docs = st.selectbox('¿Tienes información documentada como mapas de procesos, procedimientos, etc.?', opciones_docs)

# 4. Uso de consultor
opciones_consultor = (
    'No, lo haremos por nuestra cuenta.',
    'Solo para algunas partes del proyecto.',
    'Sí, para todo el proyecto.'
)
respuesta_consultor = st.selectbox('¿Vas a contratar a un consultor o experto en ISO 9001?', opciones_consultor)

# 5. Encargado del proyecto
opciones_encargado = (
    'No, las tareas se asignarán sobre la marcha.',
    'Sí, una persona con poca experiencia en proyectos, en su tiempo libre.',
    'Sí, una persona con experiencia, pero que está bastante ocupada.',
    'Sí, un gestor de proyectos con experiencia y tiempo dedicado.'
)
respuesta_encargado = st.selectbox('¿Tienes un empleado que coordinará y gestionará este proyecto?', opciones_encargado)

# 6. Apoyo de la gerencia
opciones_gerencia = (
    'No, el proyecto es una iniciativa de niveles inferiores.',
    'Nominalmente sí, pero no comprenden que deben participar e invertir recursos.',
    'Sí, la gerencia tiene objetivos claros y conoce los compromisos requeridos.'
)
respuesta_gerencia = st.selectbox('¿Cuentas con el apoyo de la alta dirección para este proyecto?', opciones_gerencia)

# 7. Diseño y desarrollo
opciones_diseno = (
    'No, nuestra empresa no diseña ni desarrolla productos/servicios.',
    'Sí, nuestro negocio incluye el proceso de diseño y desarrollo.'
)
respuesta_diseno = st.selectbox('¿Tu negocio incluye diseño y desarrollo de productos o servicios?', opciones_diseno)


# --- Lógica de Cálculo (basada en un sistema de puntos/meses) ---

# Cada opción suma una cantidad de meses. Valores más altos indican mayor complejidad.
puntos_empleados = {'1 a 20': 1, '21 a 50': 2, '51 a 100': 4, '101 a 500': 8, '501 o más': 10}
puntos_sedes = {'1': 0, '2 a 5': 1, '6 a 10': 4, '11 o más': 6}
puntos_docs = {'No, no tenemos información documentada.': 2, 'Sí, pero solo alguna información (listas de chequeo, instructivos, etc.).': 1, 'Sí, la mayoría de nuestra información relevante está documentada.': 0}
puntos_consultor = {'No, lo haremos por nuestra cuenta.': 4, 'Solo para algunas partes del proyecto.': 2, 'Sí, para todo el proyecto.': 0}
puntos_encargado = {'No, las tareas se asignarán sobre la marcha.': 4, 'Sí, una persona con poca experiencia en proyectos, en su tiempo libre.': 3, 'Sí, una persona con experiencia, pero que está bastante ocupada.': 2, 'Sí, un gestor de proyectos con experiencia y tiempo dedicado.': 0}
puntos_gerencia = {'No, el proyecto es una iniciativa de niveles inferiores.': 3, 'Nominalmente sí, pero no comprenden que deben participar e invertir recursos.': 2, 'Sí, la gerencia tiene objetivos claros y conoce los compromisos requeridos.': 0}
puntos_diseno = {'No, nuestra empresa no diseña ni desarrolla productos/servicios.': 0, 'Sí, nuestro negocio incluye el proceso de diseño y desarrollo.': 1}


# --- Botón de Cálculo y Visualización del Resultado ---

if st.button('**Calcular Tiempo Estimado**', type="primary"):
    meses_totales = 0
    meses_totales += puntos_empleados[respuesta_empleados]
    meses_totales += puntos_sedes[respuesta_sedes]
    meses_totales += puntos_docs[respuesta_docs]
    meses_totales += puntos_consultor[respuesta_consultor]
    meses_totales += puntos_encargado[respuesta_encargado]
    meses_totales += puntos_gerencia[respuesta_gerencia]
    meses_totales += puntos_diseno[respuesta_diseno]

    st.header("Resultado de la Estimación")

    if meses_totales > 24:
        st.error(f"**Estimación: {meses_totales} meses**")
        st.warning("⚠️ **Atención:** Si el proyecto excede los 14 meses, es muy probable que fracase. Se recomienda reevaluar las condiciones del proyecto, como conseguir más apoyo de la gerencia o asignar un líder de proyecto con tiempo dedicado.")
    else:
        st.success(f"**El tiempo estimado para la implementación es de {meses_totales} meses.**")
        st.metric(label="Tiempo Estimado", value=f"{meses_totales} Meses")


    st.markdown("""
    ---
    **Nota sobre la estimación:**
    Este cálculo se basa en una carga de trabajo normal, sin requerir que los empleados trabajen horas extra excesivas. Un proyecto de este tipo podría realizarse más rápido, pero implicaría descuidar otras tareas y aumentaría considerablemente el estrés del equipo de implementación.
    """)