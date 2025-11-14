#!/usr/bin/env python3
"""
Script para transcribir audio usando Whisper LOCAL (sin API key)
Uso: python transcribir_local.py
"""

import whisper
from pathlib import Path
import time

def transcribir_audio_local(ruta_audio, modelo="base"):
    """
    Transcribe un archivo de audio usando Whisper local.
    
    Modelos disponibles (de menor a mayor precisión y uso de recursos):
    - tiny: Muy rápido, menos preciso (~1GB RAM)
    - base: Balance entre velocidad y precisión (~1GB RAM)
    - small: Buena precisión (~2GB RAM)
    - medium: Muy buena precisión (~5GB RAM)
    - large: Máxima precisión (~10GB RAM)
    
    Args:
        ruta_audio (str): Ruta al archivo de audio
        modelo (str): Modelo de Whisper a usar (default: "base")
    
    Returns:
        dict: Resultado de la transcripción con texto y segmentos
    """
    archivo_audio = Path(ruta_audio)
    
    if not archivo_audio.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_audio}")
    
    print(f"📁 Archivo: {archivo_audio.name}")
    print(f"🤖 Cargando modelo Whisper '{modelo}'...")
    
    # Cargar modelo
    modelo_whisper = whisper.load_model(modelo)
    
    print(f"🎙️  Transcribiendo audio de 50 minutos...")
    print("⏳ Esto puede tardar varios minutos, ten paciencia...")
    
    inicio = time.time()
    
    # Transcribir con configuración optimizada para español
    resultado = modelo_whisper.transcribe(
        str(archivo_audio),
        language="es",
        verbose=True,  # Muestra progreso
        fp16=False  # Compatibilidad con CPUs sin CUDA
    )
    
    tiempo_total = time.time() - inicio
    minutos = int(tiempo_total // 60)
    segundos = int(tiempo_total % 60)
    
    print(f"\n✅ Transcripción completada en {minutos}m {segundos}s")
    
    return resultado


def guardar_transcripcion(resultado, directorio_salida):
    """Guarda la transcripción en archivo TXT."""
    directorio = Path(directorio_salida)
    
    # Guardar texto completo en TXT
    archivo_txt = directorio / "transcripcion.txt"
    with open(archivo_txt, "w", encoding="utf-8") as f:
        f.write(resultado["text"])
    
    # Estadísticas
    num_palabras = len(resultado["text"].split())
    duracion_audio = resultado["segments"][-1]["end"] if resultado["segments"] else 0
    
    print(f"\n{'='*60}")
    print(f"✅ TRANSCRIPCIÓN COMPLETADA")
    print(f"{'='*60}")
    print(f"📄 Archivo guardado en:")
    print(f"   {archivo_txt.absolute()}")
    print(f"\n📊 Estadísticas:")
    print(f"   - Duración: {duracion_audio/60:.1f} minutos")
    print(f"   - Palabras: {num_palabras}")
    print(f"   - Tamaño: {archivo_txt.stat().st_size / 1024:.1f} KB")
    print(f"{'='*60}")
    
    return archivo_txt


def main():
    # Configuración
    directorio_actual = Path.cwd()
    archivo_audio = directorio_actual / "CONVERSACION CAPITULO 4 TUTOR ESPECIALISTA.ogg"
    
    print("=" * 60)
    print("🎯 TRANSCRIPTOR DE AUDIO CON WHISPER LOCAL")
    print("=" * 60)
    
    # Selección de modelo
    print("\n📚 Modelos disponibles:")
    print("1. tiny   - Rápido, menos preciso")
    print("2. base   - Balance (RECOMENDADO para empezar)")
    print("3. small  - Buena precisión")
    print("4. medium - Muy buena precisión (más lento)")
    print("5. large  - Máxima precisión (muy lento)")
    
    modelos = {
        "1": "tiny",
        "2": "base",
        "3": "small",
        "4": "medium",
        "5": "large"
    }
    
    seleccion = input("\n🤔 Selecciona modelo (1-5) [default: 2]: ").strip() or "2"
    modelo = modelos.get(seleccion, "base")
    
    print(f"\n🚀 Iniciando transcripción con modelo '{modelo}'...\n")
    
    try:
        # Transcribir
        resultado = transcribir_audio_local(archivo_audio, modelo)
        
        # Guardar en TXT
        archivo_generado = guardar_transcripcion(resultado, directorio_actual)
        
        print(f"\n💡 Para ver el contenido:")
        print(f"   cat {archivo_generado.name}")
        print(f"   o abre el archivo con tu editor de texto favorito")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()