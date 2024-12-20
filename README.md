# **Head Controlled Mouse**
> Hands-free mouse control using head movements and webcam input.

[![Python Version](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/downloads/release/python-3810/)
[![Watch the video](https://img.shields.io/badge/YouTube-Click%20to%20Watch-red)](https://youtu.be/your-video-link)

This project allows users to control the mouse pointer using head movements tracked via a webcam. It leverages **MediaPipe's Face Mesh** for facial landmark detection and maps these movements to cursor control.

---

## **Features**
- Tracks head motion in real-time using a webcam.
- Uses **MediaPipe Face Mesh** for precise landmark detection.
- Maps head motion to mouse pointer movements with adjustable sensitivity.
- Easy to use, with minimal setup and cross-platform compatibility.

---

## **Requirements**

- Python 3.8
- OpenCV
- MediaPipe
- PyAutoGUI

## **Instalation**

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

3. **Adjust sensitivity:**
   Modify `x_sensitivity_factor` and `y_sensitivity_factor` in the script for your preferences:
   ```python
   x_sensitivity_factor = 2.5
   y_sensitivity_factor = 3


## **Limitations**
- Requires a well-lit environment for accurate face detection.
- Webcam quality and frame rate can affect tracking performance.
- Designed primarily for single-user use; multi-face tracking is not supported.


## **Future Improvements**
- Add multi-face tracking for group applications.
- Improve sensitivity settings to adapt dynamically to user movements.
- Add voice commands for additional controls.



## **Top Contributors**

This project was entirely developed by:

<a href="https://github.com/ianedmosz">
  <img src="https://avatars.githubusercontent.com/u/ianedmosz?v=4" width="100" height="100" alt="Ian Moreno"/>
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## **Meta**

Created and maintained by **Ian E. Moreno-Salazar**.

- **Email**: [ian.moreno@tec.mx](mailto:ianeduardomoreno98@gmail.com )
- **GitHub**: [@ianedmosz](https://github.com/ianedmosz)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

