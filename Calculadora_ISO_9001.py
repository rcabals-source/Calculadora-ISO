import streamlit as st
import re
import requests # Librería para hacer peticiones web

# --- Configuración de la página ---
st.set_page_config(
    page_title="Calculadora ISO 9001",
    page_icon="⏱️"
)

# --- Título y Descripción ---
st.title('⏱️ Calculadora de Tiempo para Implementación ISO 9001:2015')
st.markdown("...") # El resto de tu descripción va aquí

# --- Cuestionario ---
# (Aquí va todo el código del cuestionario que no ha cambiado)
# ...
st.header("Cuestionario del Proyecto")

opciones_empleados = ('1 a 20', '21 a 50', '51 a 100', '101 a 500', '501 o más')
respuesta_empleados = st.selectbox('Número de empleados dentro del alcance:', opciones_empleados)
# ... (el resto de tus selectbox)
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
    'No, queremos que el consultor lo vea todo.'
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
puntos_docs = {'No, no tenemos información documentada.': 4, 'Sí, pero solo alguna información (listas de chequeo, instructivos, etc.).': 1, 'Sí, la mayoría de nuestra información relevante está documentada.': 0}
puntos_consultor = {'No, lo haremos por nuestra cuenta.': 4, 'Solo para algunas partes del proyecto.': 2, 'Sí, para todo el proyecto.': 0}
puntos_encargado = {'No, las tareas se asignarán sobre la marcha.': 6, 'Sí, una persona сon poca experiencia en proyectos, en su tiempo libre.': 4, 'Sí, una persona сon experiencia, pero que está bastante ocupada.': 2, 'No, queremos que el consultor lo vea todo.': 0}
puntos_gerencia = {'No, el proyecto es una iniciativa de niveles inferiores.': 6, 'Nominalmente sí, pero no comprenden que deben participar e invertir recursos.': 3, 'Sí, la gerencia tiene objetivos claros y conoce los compromisos requeridos.': 0}
puntos_diseno = {'No, nuestra empresa no diseña ni desarrolla productos/servicios.': 0, 'Sí, nuestro negocio incluye el proceso de diseño y desarrollo.': 1}


if st.button('**Calcular Tiempo Estimado**', type="primary"):
    # ... (cálculo de meses_totales igual que antes)
    meses_totales = 0
    meses_totales += puntos_empleados[respuesta_empleados]
    meses_totales += puntos_sedes[respuesta_sedes]
    meses_totales += puntos_docs[respuesta_docs]
    meses_totales += puntos_consultor[respuesta_consultor]
    meses_totales += puntos_encargado[respuesta_encargado]
    meses_totales += puntos_gerencia[respuesta_gerencia]
    meses_totales += puntos_diseno[respuesta_diseno]
    st.session_state.meses_totales = meses_totales


if 'meses_totales' in st.session_state:
    # ... (código para mostrar el resultado igual que antes)
    meses = st.session_state.meses_totales
    st.header("Resultado de la Estimación")

    if meses > 12:
        st.error(f"**Estimación: {meses} meses**")
        st.warning("⚠️ **Atención:** Un proyecto de más de 12 meses tiene un alto riesgo de fracasar. Te recomendamos reevaluar las condiciones o buscar ayuda experta para optimizar el plan.")
    else:
        st.success(f"**El tiempo estimado para la implementación es de {meses} meses.**")
        st.metric(label="Tiempo Estimado", value=f"{meses} Meses")

    st.markdown("---")
    
    st.header("¿Quieres dar el siguiente paso?")
    st.write("Obtén una cotización detallada o agenda una reunión de 30 minutos sin costo para discutir tu proyecto.")
    
    st.link_button("🗓️ **Agenda una reunión con Asesorías Cabal**", "https://calendly.com/rcabals/30min", type="primary")

    st.write("--- O ---")
    
    st.subheader("Solicita una Cotización")
    with st.form("cotizacion_form", clear_on_submit=True):
        # CAMBIO IMPORTANTE: Pega tu URL de Formspree aquí abajo
        FORMSPREE_ENDPOINT = "https://formspree.io/f/mwpnwlrj"

        nombre = st.text_input("Tu Nombre Completo")
        empresa = st.text_input("Nombre de tu Empresa")
        email = st.text_input("Tu Correo Electrónico")
        telefono = st.text_input("Tu Teléfono (Ej: +56912345678)")
        
        submitted = st.form_submit_button("✅ Enviar y Solicitar Cotización")

        if submitted:
            if not nombre or not empresa or not email or not telefono:
                st.warning("Por favor, completa todos los campos.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.warning("Por favor, introduce un correo electrónico válido.")
            else:
                try:
                    # 1. OBTENEMOS EL RESULTADO DE LA MEMORIA DE LA SESIÓN
                    meses_calculados = st.session_state.get('meses_totales', 'No calculado')
                    
                    # 2. AÑADIMOS LOS MESES A LOS DATOS QUE SE ENVÍAN
                    response = requests.post(
                        FORMSPREE_ENDPOINT,
                        headers={"Accept": "application/json"},
                        data={
                            "nombre": nombre, 
                            "empresa": empresa, 
                            "email": email, 
                            "telefono": telefono,
                            "meses_estimados": meses_calculados
                        }
                    )
                    if response.status_code == 200:
                        st.success("¡Gracias! Tu solicitud ha sido enviada. Te contactaremos a la brevedad.")
                        st.balloons()
                    else:
                        st.error("Hubo un error al enviar el formulario. Por favor, inténtalo de nuevo.")
                except Exception as e:
                    st.error(f"Ocurrió un error de conexión: {e}")


