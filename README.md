# 🗓️ Sistema de Turnos para Profesionales (CLI)

Aplicación desarrollada en **Python** que simula un **sistema de gestión de turnos** para profesionales independientes (fisioterapeutas, dentistas, psicólogos, peluqueros, etc.) mediante una **interfaz de línea de comandos (CLI)**.

Este proyecto forma parte de mi **portfolio personal** y está orientado a practicar **Programación Orientada a Objetos**, **arquitectura por capas** y **lógica de negocio real**, sin usar frameworks ni bases de datos.

---

## 🚀 Funcionalidades

- ➕ Crear profesionales
- ➕ Crear clientes
- 📅 Crear citas con validación de solapamientos
- 📋 Ver agenda de un profesional (ordenada por fecha y hora)
- ❌ Cancelar citas existentes
- 💾 Persistencia de datos en archivos JSON

---

## 🧠 Reglas de negocio implementadas

- Un profesional **no puede tener dos citas**:
  - el mismo día
  - a la misma hora
- Las citas se identifican por:
  - profesional
  - fecha
  - hora de inicio
- Cada cita tiene una duración fija de **1 hora**
- Solo se pueden crear citas con:
  - profesionales existentes
  - clientes existentes

---

## 🧱 Arquitectura del proyecto

El proyecto está estructurado siguiendo una **arquitectura por capas**, separando claramente responsabilidades.

```bash
gestor-turnos/
│
├── main.py # Punto de entrada de la aplicación
│
├── ui/
│ └── cli.py # Interfaz de línea de comandos (CLI)
│
├── services/
│ └── turnos_service.py # Lógica de negocio
│
├── models/
│ ├── profesional.py # Modelo Profesional
│ ├── cliente.py # Modelo Cliente
│ └── cita.py # Modelo Cita
│
├── data/
│ ├── repository.py # Persistencia en JSON
│ └── turnos.json # Archivo de datos
│
└── README.md
```


### 📌 Responsabilidades por capa

- **Models**  
  Representan entidades del dominio y validan datos.
- **Services**  
  Contienen la lógica de negocio y las reglas del sistema.
- **Repository**  
  Se encarga únicamente de leer y escribir datos en JSON.
- **CLI**  
  Interactúa con el usuario y muestra resultados.

---

## ▶️ Cómo ejecutar el proyecto

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/gestor-turnos-python.git
```
### 2️⃣ Entrar en el directorio
```bash
cd gestor-turnos-python
```
### 3️⃣ Ejecutar la aplicación
```bash
python main.py
```

---

🛠️ Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos (POO)
- Manejo de fechas y horas (datetime)
- Persistencia con JSON
- Arquitectura por capas
- CLI (Command Line Interface)
- Git y GitHub

---

🔧 Posibles mejoras futuras

- Duración variable de las citas
- Horarios reales por profesional
- Filtro de agenda por día
- Tests automatizados
- Interfaz gráfica o API REST









