# PF_Python

# Proyecto de Suscripción a Planes de Inteligencia Artificial
# Descripción
# Este proyecto es una plataforma de suscripción que permite a los usuarios registrarse y acceder a su perfil. Los usuarios pueden ver los  detalles de su suscripción. Los administradores tienen la capacidad de agregar nuevos planes y gestionar los pagos realizados por los usuarios.

# Características
# Registro de usuarios: Los usuarios pueden registrarse proporcionando un correo electrónico, nombre, apellido, número de teléfono y dirección.
# Ver perfil: Los usuarios pueden acceder a sus detalles de perfil.
# Planes de suscripción: Los administradores pueden agregar, editar y eliminar planes de suscripción de IA.
# Gestión de pagos: Los administradores pueden ver, agregar y gestionar pagos realizados por los usuarios.
# Instalación:
# Clona el repositorio:
# git clone <https://github.com/LourdesAnzorena/PF_Python.git>
# Instala las dependencias:
# pip install -r requirements.txt
# Configura las variables de entorno:
# Crea un archivo .env en la raíz de tu proyecto y configura las siguientes variables:
# plaintext
# SECRET_KEY=
# DEBUG=True/False
# DATABASE_URL=postgres://usuario:contraseña@localhost:5432/nombre_db
# Aplicaciones de migración:
# python manage.py makemigrations
# python manage.py migrate
# Uso
# Ejecutar el servidor:
# python manage.py runserver
# Acceder al proyecto en tu navegador:
# Abre http://127.0.0.1:8000/inicio/ para ver la página de inicio.
# Accede a http://127.0.0.1:8000/registrarse/ para registrarte como nuevo usuario.
# Accede a http://127.0.0.1:8000/perfil/ para ver tu perfil 
# Accede a http://127.0.0.1:8000/pago/ para ver los comprobantes de pago 
# Accede a http://127.0.0.1:8000/agregar-pago/ para agregar un nuevo pago (solo para usuarios administradores).
# Roles y Accesos
# Usuario
# Registro: Puede registrarse proporcionando un correo electrónico, nombre, apellido, número de teléfono y dirección.
# Ver perfil: Accede a su perfil para ver su suscripción.
# Administrador
# Gestión de planes: Puede agregar, editar y eliminar planes de suscripción.
# Gestión de pagos: Ver y agregar pagos realizados por los usuarios.
# Contribuir
# Si deseas contribuir al proyecto, por favor, sigue estas instrucciones:

# Haz un fork del repositorio.
# Crea una nueva rama con tus cambios (git checkout -b nueva-rama).
# Realiza los cambios necesarios y realiza los tests correspondientes.
# Envía un pull request describiendo los cambios realizados.
# Contacto
# Si tienes preguntas o sugerencias, por favor contacta a:

# Lourdes Anzorena - lourdes@anzorena.com
# Repositorio de GitHub: GitHub
