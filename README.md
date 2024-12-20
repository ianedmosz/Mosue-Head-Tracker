# **Head Controlled Mouse**
> Hands-free mouse control using head movements and webcam input.

[![Python Version](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/downloads/release/python-3810/)

This project allows users to control the mouse pointer using head movements tracked via a webcam. It leverages **MediaPipe's Face Mesh** for facial landmark detection and maps these movements to cursor control.

[![Watch the video](https://img.shields.io/badge/YouTube-Click%20to%20Watch-red)](https://youtu.be/your-video-link)

---

## **Features**
- Tracks head motion in real time using a webcam.
- Accurate mouse pointer control with adjustable sensitivity.
- Simple setup and cross-platform compatibility.

---

## **Installation**

### OS X & Linux:
```bash
conda create -n head_mouse python=3.8
conda activate head_mouse
pip install -r requirements.txt
```

### Windows: 

``` bash
conda create -n head_mouse python=3.8
conda activate head_mouse
pip install -r requirements.txt
```

## **Usage**

1. **Run the script:**
   ```bash
   python mouse_final.py
   ```
2. **Controls:**
- Move your head to control the mouse pointer.
- Press **'q'** to quit the application.


4. **Adjust sensitivity: Modify x_sensitivity_factor and y_sensitivity_factor in the script for your preferences:**
   - x_sensitivity_factor = 2.5.
   - y_sensitivity_factor = 3.


## **Meta**

Created and maintained by **Ian E. Moreno-Salazar**.

- **Email**: [ian.moreno@tec.mx](mailto:ianeduardomoreno98@gmail.com )
- **GitHub**: [@ianedmosz](https://github.com/ianedmosz)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

