# CRUD-Python-Flask

Este proyecto es una implementación de un CRUD (Crear, Leer, Actualizar, Borrar) usando Python, Flask y Supabase como base de datos.

## Requisitos Previos

Asegúrate de tener instalado Python 3.7 o superior en tu sistema.

## Configuración del Entorno

Sigue estos pasos para configurar y ejecutar el proyecto:

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local:

\`\`\`bash
git clone https://github.com/ClaudioLabbe/CRUD-Python-Flask.git
cd CRUD-Python-Flask
\`\`\`

### 2. Crear un Entorno Virtual

Crea un entorno virtual para la instalación de paquetes:

\`\`\`bash
python -m venv venv
\`\`\`

### 3. Activar el Entorno Virtual

Activa el entorno virtual:

- En Windows:

    \`\`\`bash
    .\\venv\\Scripts\\activate
    \`\`\`

- En macOS y Linux:

    \`\`\`bash
    source venv/bin/activate
    \`\`\`

### 4. Instalar Dependencias

Instala las dependencias necesarias:

\`\`\`bash
pip install flask supabase-py
\`\`\`

### 5. Configurar Supabase

Asegúrate de tener tu URL y clave de API de Supabase y configúralos en tu archivo \`Connection.py\`:

SUPABASE_URL = "TU_SUPABASE_URL"
SUPABASE_KEY = "TU_SUPABASE_KEY"

### 6. Ejecutar el Servicio

Levanta el servicio Flask:

\`\`\`bash
python app/app.py
\`\`\`

### 7. Probar el Servicio

Una vez que el servicio esté en funcionamiento, puedes probar los endpoints usando herramientas como \`curl\`, \`Postman\` o tu navegador web.

### Endpoints Disponibles

- **GET /users**: Obtiene todos los usuarios.
- **POST /create_user**: Crea un nuevo usuario. Ejemplo de cuerpo de solicitud:
    \`\`\`json
    {
        "name":"test",
        "last_name":"test",
        "email": "test@test.com"
    }
    \`\`\`

### Contribuir

Si deseas contribuir a este proyecto, por favor, sigue los pasos a continuación:

1. Haz un fork del repositorio.
2. Crea una nueva rama (\`git checkout -b feature/nueva-funcionalidad\`).
3. Realiza tus cambios y haz commit (\`git commit -am 'Añadir nueva funcionalidad'\`).
4. Haz push a la rama (\`git push origin feature/nueva-funcionalidad\`).
5. Abre un Pull Request.

---

¡Gracias por utilizar este proyecto! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o contactar al mantenedor del proyecto.

