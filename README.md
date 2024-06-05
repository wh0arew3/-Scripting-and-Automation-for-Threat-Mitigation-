# Scripting and Automation for Threat Mitigation

Este proyecto contiene un script en Python para la automatización de tareas relacionadas con la mitigación de amenazas. El script realiza un escaneo de puertos abiertos en una dirección IP, verifica vulnerabilidades comunes en esos puertos y genera un informe con los resultados.

## Requisitos

- Python 3.x
- nmap (debe estar instalado y en el PATH)
- Bibliotecas de Python: `python-nmap` y `requests`

## Instalación

### Paso 1: Instalar `nmap`

#### Windows

1. Descarga el instalador de `nmap` desde [nmap.org](https://nmap.org/download.html).
2. Ejecuta el instalador y sigue las instrucciones para instalar `nmap`.
3. Asegúrate de que la ruta de instalación de `nmap` esté en el PATH del sistema. Puedes agregarla manualmente si es necesario.

#### macOS

1. Si tienes `Homebrew` instalado, puedes instalar `nmap` con el siguiente comando:

    ```sh
    brew install nmap
    ```

2. Si no tienes `Homebrew`, puedes descargar el instalador desde [nmap.org](https://nmap.org/download.html) y seguir las instrucciones.

#### Linux

1. En distribuciones basadas en Debian/Ubuntu, puedes instalar `nmap` con el siguiente comando:

    ```sh
    sudo apt-get install nmap
    ```

2. En distribuciones basadas en Red Hat/Fedora, usa el siguiente comando:

    ```sh
    sudo yum install nmap
    ```

### Paso 2: Instalar las bibliotecas de Python

Ejecuta el siguiente comando para instalar las bibliotecas requeridas:

```
pip install python-nmap requests


