# 😎 Detector de Rostros en Tiempo Real

Este proyecto utiliza **OpenCV** y un modelo pre-entrenado de **Caffe** para detectar rostros en tiempo real usando la cámara de tu computadora.

---

## 🛠️ Tecnologías y Librerías

- 🐍 **Python 3.x**  
- 📸 **OpenCV** (`opencv-python`)  
- 🤖 **Modelo DNN Caffe**: `res10_300x300_ssd_iter_140000.caffemodel`  
- 📄 **Archivo Prototxt**: `deploy.prototxt`  

Se utiliza la API **DNN de OpenCV** para cargar el modelo Caffe y realizar la detección de rostros en tiempo real.

---

## 🚀 Instalación

1. Clonar este repositorio:

```bash
git clone https://github.com/mauripucheta1/Detector-de-Rostros.git
cd Detector-de-Rostros