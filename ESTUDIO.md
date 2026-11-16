# Estudio de vídeo — guía para Pablo

Esta copia de OpenMontage es tu estudio de vídeo con un agente de Cursor. Tú describes el vídeo en español. El agente lee las instrucciones del repo, elige herramientas y arma el archivo final.

No hace falta saber GitHub de memoria. Esta página dice qué es cada pieza y cómo dejar el equipo listo. **No pongas claves de API en este archivo ni en el chat.** Si más adelante usas un servicio de pago, la clave va solo en un archivo `.env` local, que Git no sube.

## Qué es cada pieza

| Pieza | Para qué sirve |
| --- | --- |
| **Cursor** | El programa donde abres el repo y hablas con el agente. El agente lee `AGENT_GUIDE.md` y las skills antes de generar. |
| **OpenMontage** | El proyecto. Tiene pipelines (explicador, animación, etc.), herramientas en Python y el compositor de vídeo. |
| **Remotion** (`remotion-composer/`) | Vídeo hecho con React: títulos, números, gráficos, transiciones. Es gratis para empresas de hasta 3 personas. La licencia oficial está en [remotion.dev/docs/license](https://www.remotion.dev/docs/license). |
| **HyperFrames** | Otra forma de componer vídeo, con HTML y animación (GSAP). Sirve para motion graphics, promos y piezas que se sienten como una página animada. |
| **Skills** (`.agents/skills/` y `.claude/skills/`) | Manuales que el agente lee solo. Ahí están Remotion, HyperFrames, el skill de stickman y las diez reglas de movimiento (`motion-cinco-efectos`). |
| **Whisper** (`faster-whisper`, herramienta `transcriber`) | Pasa la voz a texto con el tiempo de cada palabra, para subtítulos y para sincronizar animaciones con la narración. |
| **Piper** | Voz en off gratis, en tu computador, sin internet. |
| **earshot** | El agente “escucha” el audio, lo critica y puede crear efectos de sonido con código. |
| **Stickman** | Skill para vídeos de monigote. El texto y los scripts ya están en el repo. El audio y las imágenes grandes se descargan aparte. |

## Abrir el repo en Cursor

1. Instala Cursor desde [cursor.com](https://cursor.com) si aún no lo tienes.
2. En Cursor: **File → Open Folder** y elige la carpeta de este repositorio (la que contiene `AGENT_GUIDE.md` y `ESTUDIO.md`).
3. Abre el chat del agente y pide el vídeo en español, por ejemplo: “Haz un explicador de 45 segundos sobre cómo agendar una hora en la clínica”.
4. El agente debe seguir `AGENT_GUIDE.md`. Para explicadores y motion graphics también aplica `.agents/skills/motion-cinco-efectos/SKILL.md` (revelado con máscara, movimiento encadenado, cámara que sigue, morph, sync con la narración, rebote, stagger, parallax, micro-movimiento y barra de luz).

Si GitHub te pide iniciar sesión, usa la cuenta con la que clonaste el repo. No hace falta crear ramas a mano si solo estás pidiendo vídeos al agente.

## Preparar el entorno (una vez)

Abre la terminal **dentro de la carpeta del repo**. En Cursor: **Terminal → New Terminal**.

### 1. Python (entorno virtual)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install piper-tts faster-whisper
```

En Windows el activate es `.venv\Scripts\activate`.

`make setup` hace el entorno, instala Python y también corre `npm install` en Remotion. Si prefieres los pasos sueltos, los de abajo alcanzan.

### 2. Remotion (Node)

Hace falta Node.js 22 o superior.

```bash
cd remotion-composer
npm install
cd ..
```

Eso instala Remotion y, entre otras, `lucide-react`, `three`, `@react-three/fiber` (línea 8, compatible con React 18), `@remotion/three` en la misma versión que Remotion, y `svgo`.

### 3. HyperFrames

```bash
npx hyperframes doctor
```

El comando revisa Node, FFmpeg y el navegador. Si algo falta, el mensaje dice qué instalar. La primera vez puede tardar porque `npx` descarga el paquete.

### 4. Voces de Piper en español

```bash
python -m piper.download_voices --download-dir ~/.piper/models es_MX-ald-medium
python -m piper.download_voices --download-dir ~/.piper/models es_ES-davefx-medium
```

- `es_MX-ald-medium` — español de México.
- `es_ES-davefx-medium` — español de España.

Dile al agente cuál quieres. Los archivos quedan en tu carpeta personal, no en Git.

### 5. earshot (crítica de audio y efectos)

Hace falta [uv](https://docs.astral.sh/uv/getting-started/installation/) y `ffmpeg` en el PATH. No usa GPU.

```bash
uv tool install "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"
earshot doctor --fetch
```

`earshot doctor --fetch` baja los modelos de earshot (pesan alrededor de 1 GB). El extra de crítica con Gemini es opcional y usaría una clave tuya; esta guía no la guarda. La instalación de arriba no la necesita.

Repo: [https://github.com/Leonxlnx/earshot](https://github.com/Leonxlnx/earshot).

### 6. Biblioteca del skill stickman (solo si vas a hacer monigotes)

El audio y las imágenes pesan unos 490 MB y no van en Git.

```bash
bash scripts/install-stickman-assets.sh
```

## Transcripción: modelo y idioma

Cuando el agente transcriba narración en español con Whisper local, tiene que usar:

- modelo **`small`**
- idioma **`es`**

El modelo por defecto de muchos tutoriales, **`small.en`**, está entrenado solo en inglés y **traduce** el audio al inglés. Para la clínica eso está mal. Ejemplo de llamada a la herramienta `transcriber`:

```text
model_size: small
language: es
```

## Remotion y el tamaño del equipo

Remotion es gratis para una empresa de hasta 3 personas. Mi Agenda Clínica entra en ese caso. Si el equipo crece, revisa la licencia antes de seguir publicando vídeos comerciales: [remotion.dev/docs/license](https://www.remotion.dev/docs/license).

## Si algo falla

- `python` no se reconoce: activa el entorno (`.venv`) o usa `python3`.
- `npx` no se reconoce: instala Node.js 22 y abre una terminal nueva.
- HyperFrames se queja de FFmpeg: instala FFmpeg y vuelve a correr `npx hyperframes doctor`.
- El vídeo “suena en inglés” aunque hablaste en español: la transcripción usó `small.en`. Pide rehacerla con modelo `small` e idioma `es`.
