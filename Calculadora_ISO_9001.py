import streamlit as st
import re # Importamos la librería para validaciones

# --- Configuración de la página ---
st.set_page_config(
    page_title="Calculadora ISO 9001",
    page_icon="⏱️"
)

# --- Título y Descripción ---
st.title('⏱️ Calculadora de Tiempo para Implementación ISO 9001:2015')
st.markdown("""
Esta calculadora te ayudará a estimar el tiempo necesario para tu proyecto de implementación de la Norma ISO 9001.

**Importante:** Por favor, introduce los datos considerando únicamente el **alcance de tu SGC (Sistema de Gestión de la Calidad)**.
""")

# --- Cuestionario ---
st.header("Cuestionario del Proyecto")

opciones_empleados = ('1 a 20', '21 a 50', '51 a 100', '101 a 500', '501 o más')
respuesta_empleados = st.selectbox('Número de empleados dentro del alcance:', opciones_empleados)

opciones_sedes = ('1', '2 a 5', '6 a 20', '21 o más')
respuesta_sedes = st.selectbox('Número de sedes físicas:', opciones_sedes)

opciones_docs = (
    'No, no tenemos información documentada.',
    'Sí, pero solo alguna información (listas de chequeo, instructivos, etc.).',
    'Sí, la mayoría de nuestra información relevante está documentada.'
)
respuesta_docs = st.selectbox('¿Tienes información documentada como mapas de procesos, procedimientos, etc.?', opciones_docs)

opciones_consultor = (
    'No, lo haremos por nuestra cuenta.',
    'Solo para algunas partes del proyecto.',
    'Sí, para todo el proyecto.'
)
respuesta_consultor = st.selectbox('¿Vas a contratar a un consultor o experto en ISO 9001?', opciones_consultor)

opciones_encargado = (
    'No, las tareas se asignarán sobre la marcha.',
    'Sí, una persona сon poca experiencia en proyectos, en su tiempo libre.',
    'Sí, una persona сon experiencia, pero que está bastante ocupada.',
    'Sí, un gestor de proyectos сon experiencia y tiempo dedicado.'
)
respuesta_encargado = st.selectbox('¿Tienes un empleado que coordinará y gestionará este proyecto?', opciones_encargado)

opciones_gerencia = (
    'No, el proyecto es una iniciativa de niveles inferiores.',
    'Nominalmente sí, pero no comprenden que deben participar e invertir recursos.',
    'Sí, la gerencia tiene objetivos claros y conoce los compromisos requeridos.'
)
respuesta_gerencia = st.selectbox('¿Cuentas con el apoyo de la alta dirección para este proyecto?', opciones_gerencia)

opciones_diseno = (
    'No, nuestra empresa no diseña ni desarrolla productos/servicios.',
    'Sí, nuestro negocio incluye el proceso de diseño y desarrollo.'
)
respuesta_diseno = st.selectbox('¿Tu negocio incluye diseño y desarrollo de productos o servicios?', opciones_diseno)

puntos_empleados = {'1 a 20': 1, '21 a 50': 2, '51 a 100': 6, '101 a 500': 8, '501 o más': 10}
puntos_sedes = {'1': 0, '2 a 5': 2, '6 a 20': 4, '21 o más': 6}
puntos_docs = {'No, no tenemos información documentada.': 3, 'Sí, pero solo alguna información (listas de chequeo, instructivos, etc.).': 1, 'Sí, la mayoría de nuestra información relevante está documentada.': 0}
puntos_consultor = {'No, lo haremos por nuestra cuenta.': 4, 'Solo para algunas partes del proyecto.': 2, 'Sí, para todo el proyecto.': 0}
puntos_encargado = {'No, las tareas se asignarán sobre la marcha.': 4, 'Sí, una persona сon poca experiencia en proyectos, en su tiempo libre.': 3, 'Sí, una persona сon experiencia, pero que está bastante ocupada.': 2, 'Sí, un gestor de proyectos сon experiencia y tiempo dedicado.': 0}
puntos_gerencia = {'No, el proyecto es una iniciativa de niveles inferiores.': 6, 'Nominalmente sí, pero no comprenden que deben participar e invertir recursos.': 3, 'Sí, la gerencia tiene objetivos claros y conoce los compromisos requeridos.': 0}
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

    st.session_state.meses_totales = meses_totales # Guardamos el resultado en el estado de la sesión

# --- Mostrar el resultado si ya fue calculado ---
if 'meses_totales' in st.session_state:
    meses = st.session_state.meses_totales
    st.header("Resultado de la Estimación")

    if meses > 12:
        st.error(f"**Estimación: {meses} meses**")
        st.warning("⚠️ **Atención:** Un proyecto de más de 24 meses tiene un alto riesgo de fracasar. Te recomendamos reevaluar las condiciones o buscar ayuda experta para optimizar el plan.")
    else:
        st.success(f"**El tiempo estimado para la implementación es de {meses} meses.**")
        st.metric(label="Tiempo Estimado", value=f"{meses} Meses")

    st.markdown("---")
    
    # --- NUEVA SECCIÓN: LLAMADO A LA ACCIÓN ---
    st.header("¿Quieres dar el siguiente paso?")
    st.write("Obtén una cotización detallada o agenda una reunión de 30 minutos sin costo para discutir tu proyecto.")

    # Opción 1: Agendar en Calendly
    st.link_button("🗓️ **Agendar una Reunión Ahora**", "https://calendly.com/rcabals/30min", type="primary")

    st.write("--- O ---")
    
    # Opción 2: Formulario de Cotización
    st.subheader("Solicita una Cotización")
    with st.form("cotizacion_form"):
        nombre = st.text_input("Tu Nombre Completo")
        email = st.text_input("Tu Correo Electrónico")
        telefono = st.text_input("Tu Teléfono (Ej: +56912345678)")
        
        submitted = st.form_submit_button("✅ Enviar y Solicitar Cotización")

        if submitted:
            # Validación simple
            if not nombre or not email or not telefono:
                st.warning("Por favor, completa todos los campos.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.warning("Por favor, introduce un correo electrónico válido.")
            else:
                st.success(f"¡Gracias, {nombre}! Hemos recibido tu solicitud. Te contactaremos a la brevedad en **{email}** o al teléfono **{telefono}**.")
                st.balloons()
                # NOTA: En una app real, aquí iría el código para enviar esta información
                # a una base de datos, un CRM o por correo electrónico.
                # Como Streamlit es 'frontend', solo mostramos un mensaje de éxito.
