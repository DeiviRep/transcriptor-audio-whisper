# 🎙️ Transcriptor de Audio con Whisper

Transcribe archivos de audio de cualquier duración usando Whisper de OpenAI de forma **100% gratuita y local**.

## 📋 Características

✅ **Gratuito** - Sin necesidad de API keys  
✅ **Privado** - Procesa todo en tu máquina local  
✅ **Sin límites** - Transcribe audios de cualquier duración  
✅ **Offline** - Funciona sin conexión a internet (después de instalar)  
✅ **Preciso** - Optimizado para español  
✅ **Automático** - Genera el TXT automáticamente  

## 🚀 Instalación

### Requisitos previos
- Python 3.8 o superior
- ffmpeg

### Paso 1: Instalar ffmpeg
```bash
sudo apt update
sudo apt install ffmpeg
```

### Paso 2: Crear entorno virtual
```bash
cd /home/deivi/Documents/TESIS-DOCS/TRANSKIB
python3 -m venv venv
```

### Paso 3: Activar entorno virtual
```bash
source venv/bin/activate
```

### Paso 4: Instalar dependencias
```bash
pip install --upgrade pip
pip install openai-whisper
```

## 📝 Uso

### Ejecutar la transcripción
```bash
./venv/bin/python transcribir_local.py
```

### Seleccionar modelo
El script te preguntará qué modelo usar:

| Modelo | Velocidad | Precisión | RAM requerida | Recomendado para |
|--------|-----------|-----------|---------------|------------------|
| 1. tiny | ⚡⚡⚡⚡⚡ | ⭐⭐ | ~1GB | Pruebas rápidas |
| 2. base | ⚡⚡⚡⚡ | ⭐⭐⭐ | ~1GB | **Uso general** |
| 3. small | ⚡⚡⚡ | ⭐⭐⭐⭐ | ~2GB | Buena calidad |
| 4. medium | ⚡⚡ | ⭐⭐⭐⭐⭐ | ~5GB | Alta precisión |
| 5. large | ⚡ | ⭐⭐⭐⭐⭐ | ~10GB | Máxima calidad |

**Recomendación:** Empieza con el modelo `base` (opción 2).

### Resultado
El script genera automáticamente:
```
📄 transcripcion.txt
```

## 📂 Estructura del proyecto

```
TRANSKIB/
├── venv/                              # Entorno virtual
├── REUNION CON INGE ESPECIALISTA.ogg  # Tu archivo de audio
├── transcribir_local.py               # Script de transcripción
├── transcripcion.txt                  # Resultado generado
└── README.md                          # Este archivo
```

## ⏱️ Tiempos estimados

Para un audio de **50 minutos**:

- **tiny**: ~5-10 minutos
- **base**: ~15-25 minutos  ⭐ Recomendado
- **small**: ~25-40 minutos
- **medium**: ~40-60 minutos
- **large**: ~60-90 minutos

*Los tiempos varían según tu hardware*

## 🔧 Comandos útiles

### Ver el contenido del TXT
```bash
cat transcripcion.txt
```

### Editar el TXT
```bash
nano transcripcion.txt
# o
gedit transcripcion.txt
```

### Desactivar entorno virtual
```bash
deactivate
```

### Volver a activar entorno virtual
```bash
source venv/bin/activate
```

## ❓ Solución de problemas

### Error: "No module named 'whisper'"
Asegúrate de usar el Python del entorno virtual:
```bash
./venv/bin/python transcribir_local.py
```

### Error: "ffmpeg not found"
Instala ffmpeg:
```bash
sudo apt install ffmpeg
```

### El audio es muy largo
No hay problema, Whisper puede procesar audios de cualquier duración. Solo tardará más tiempo.

### Baja calidad de transcripción
Prueba con un modelo más grande (small, medium o large).

## 📊 Salida del script

Al finalizar verás:
```
============================================================
✅ TRANSCRIPCIÓN COMPLETADA
============================================================
📄 Archivo guardado en:
   /home/deivi/Documents/TESIS-DOCS/TRANSKIB/transcripcion.txt

📊 Estadísticas:
   - Duración: 50.0 minutos
   - Palabras: 7500
   - Tamaño: 45.2 KB
============================================================
```

## 🎯 Ejemplo de uso completo

```bash
# 1. Ir al directorio
cd /home/deivi/Documents/TESIS-DOCS/TRANSKIB

# 2. Activar entorno (si no está activado)
source venv/bin/activate

# 3. Ejecutar transcripción
./venv/bin/python transcribir_local.py

# 4. Seleccionar modelo (presiona 2 para 'base')
🤔 Selecciona modelo (1-5) [default: 2]: 2

# 5. Esperar... ⏳

# 6. Ver resultado
cat transcripcion.txt
```

## 📝 Notas

- El primer uso descargará el modelo seleccionado (~100-1500 MB según el modelo)
- Los modelos se guardan en cache, los siguientes usos serán más rápidos
- El script está optimizado para español
- Puedes transcribir el mismo audio con diferentes modelos para comparar

## 🤝 Soporte

Si tienes problemas:
1. Verifica que ffmpeg está instalado: `ffmpeg -version`
2. Usa el Python del entorno virtual: `./venv/bin/python`
3. Revisa que el archivo de audio existe: `ls -lh "REUNION CON INGE ESPECIALISTA.ogg"`

---

**Creado para transcribir reuniones de tesis de forma gratuita y privada 🎓**