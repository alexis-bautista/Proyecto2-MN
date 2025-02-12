# ☀️ Seguidor Solar - Proyecto 2 de Métodos Numéricos

Este repositorio contiene la simulación de un seguidor solar, desarrollada como parte del Proyecto 2 de Métodos Numéricos.

## 📌 Descripción
La Facultad de Ingeniería Mecánica de la Escuela Politécnica Nacional (EPN) dispone de varios sistemas de seguimiento solar. Uno de ellos es el objeto de estudio de este proyecto.

El objetivo es calcular los ángulos de control para un seguidor solar de 2 grados de libertad con el fin de maximizar la captación de luz solar.

### 🌞 ¿Qué es un seguidor solar?
Un seguidor solar es un sistema de orientación diseñado para maximizar la exposición de un panel solar a la luz del sol. Esto se logra cuando el panel se orienta perpendicularmente a la luz solar incidente.

>⚠️ IMPORTANTE:
A diferencia de otros seguidores solares, el de la EPN ajusta su orientación alrededor del ángulo de pitch en lugar del ángulo de yaw.

### 🔄 Ángulos de control en un seguidor solar de 2 grados de libertad
El seguidor solar se ajusta mediante los siguientes ángulos:

Roll (r): Ángulo de giro alrededor del eje que mira al norte.
Pitch (p): Ángulo de giro alrededor del eje que mira al este.

### 📍 Posición solar
La posición del sol en el cielo se mide con dos ángulos:

Elevación (θ): Ángulo del sol con respecto a su proyección en la superficie terrestre.
Azimut (α): Ángulo de la proyección del sol en la superficie con respecto al norte.

## 📥 Instalación
¡Instrucciones para utilizar este programa!

1. Clonar repositorio (varias maneras de realizarlo):
- Ejecutar el comando en la terminal de git bash: git clone https://github.com/alexis-bautista/Proyecto2-MN.git 
- Abrir el repositorio con GitHub Desktop desde el navegador.
- Descargar y descomprimir el archivo ZIP.

## 🚀 Uso

### 📦 Instalación de dependencias
Antes de ejecutar el programa, asegúrate de instalar todas las dependencias necesarias con el siguiente comando:

`pip install -r requirements.txt`

### ▶️ Ejecutar la simulación
🔹 Desde la terminal
Para iniciar la interfaz gráfica (GUI) del seguidor solar, ejecuta el siguiente comando en la terminal:
`python GUI.py`

🔹 Desde VS Code
Si prefieres ejecutar el programa desde Visual Studio Code, sigue estos pasos:

1. Abrir el proyecto en VS Code:
    
    Desde VS Code, ve a Archivo > Abrir carpeta... y selecciona la carpeta del proyecto.

2. Abrir GUI.py

    En el Explorador de Archivos de VS Code, busca y abre GUI.py.

3. Ejecutar el programa

    - Haz clic en el botón ▶️ "Run" en la parte superior derecha.

    - O presiona F5 si tienes configurado Python como depurador.

Esto abrirá la interfaz gráfica del seguidor solar directamente desde VS Code.


## 🛠️ Tecnologías utilizadas

**Lenguaje:** Python

**Interfaz gráfica:** Tkinter

**Bibliotecas:**

- matplotlib – Visualización de gráficos
- numpy – Cálculos numéricos
- pysolar – Cálculo de posición solar
- pytz – Manejo de zonas horarias
- tkcalendar – Selector de fechas en la interfaz gráfica
- datetime – Manejo de fechas y horas

## 👥 Integrantes
- ALEXIS BAUTISTA
- DAVID EGAS
- AUBERTIN OCHOA
- ERICK ROMERO