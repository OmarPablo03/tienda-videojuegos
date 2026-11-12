# 🎮 Tienda de Videojuegos - Proyecto Django

Proyecto del Segundo Parcial - INF 560 Desarrollo Web Back-End

## 🛠️ Tecnologías

- **Backend:** Django 6
- **Base de datos:** SQLite (incluida con Django, no requiere instalación aparte)
- **Frontend:** HTML5 + Bootstrap 5 + Django Templates
- **Autenticación:** Sistema nativo de Django (contraseñas hasheadas con PBKDF2)
- **Variables de entorno:** python-dotenv

## 📋 Requisitos previos

- **Python 3.10 o superior** instalado (verifica con `python --version`).
- **Git** instalado (para clonar el repositorio).
- Una terminal (CMD, PowerShell o Git Bash).

## 🚀 Cómo arrancar el proyecto

Sigue estos pasos **en orden** desde la terminal:

### 1. Clonar el repositorio

```bash
git clone <URL_DE_TU_REPO>
cd tienda-videojuegos
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv .venv
En Windows (CMD o PowerShell): .venv\Scripts\activate
En Mac/Linux: source .venv/bin/activate
```

(Sabrás que está activo porque verás (.venv) al inicio de la línea de la terminal).

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Copia el archivo de ejemplo y renómbralo:

```bash
En Windows (CMD): copy .env.example .env
En Windows (PowerShell): Copy-Item .env.example .env
En Mac/Linux: cp .env.example .env
```

(Abre el archivo .env y, si quieres, cambia la SECRET_KEY por una propia).

### 5. Aplicar las migraciones (crear la base de datos)

```bash
python manage.py migrate
```

### 6. (Opcional) Crear un superusuario (Administrador)

```bash
python manage.py createsuperuser
```

(Sigue las instrucciones en pantalla. Este usuario tendrá acceso al panel de admin y podrá crear, editar y borrar videojuegos).

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

### 8. Abrir en el navegador

```bash
App principal: http://127.0.0.1:8000/
Panel de administración: http://127.0.0.1:8000/admin/
```
