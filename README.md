# 🖐️ MediaPipe Hand & Selfie Segmentation

이 저장소는 **MediaPipe**를 이용해 두 가지 컴퓨터 비전 기능을 구현한 예제입니다.

* **Hand Detector** (`hand_detector.py`) : 손의 위치와 관절을 실시간으로 추적
* **Selfie Segmentation** (`selfie_segmentation.py`) : 얼굴 및 인물 영역을 배경과 분리

---

## 🧰 환경 설정

### 1. 필수 패키지 설치

`requirements.txt` 파일을 이용해 필요한 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt
```

`requirements.txt` 내용:

```
opencv-python
mediapipe
```

---

## 📁 파일 설명

| 파일명                      | 설명                                                    |
| ------------------------ | ----------------------------------------------------- |
| `hand_detector.py`       | Mediapipe의 Hand Tracking 기능을 사용해 손 랜드마크를 인식하고 시각화합니다. |
| `selfie_segmentation.py` | Mediapipe의 Selfie Segmentation 모델을 이용해 배경을 흐리게 처리합니다. |
| `requirements.txt`       | 프로젝트 실행에 필요한 패키지 목록입니다.                               |

---

## ▶️ 실행 방법

### **1️⃣ Hand Detector 실행**

```bash
python hand_detector.py
```

* 기본적으로 `hand.mp4` 파일을 읽어 손을 탐지합니다.
* 카메라를 직접 사용하려면 코드의 다음 줄을 수정하세요:

  ```python
  # cap = cv2.VideoCapture(0)
  cap = cv2.VideoCapture("hand.mp4")
  ```

> ESC 키를 누르면 프로그램이 종료됩니다.

---

### **2️⃣ Selfie Segmentation 실행**

```bash
python selfie_segmentation.py
```

* 기본적으로 `face.mp4` 파일을 읽어 인물 분리를 수행합니다.
* 웹캠을 사용하려면 코드의 다음 줄을 수정하세요:

  ```python
  # cap = cv2.VideoCapture(0)
  cap = cv2.VideoCapture("face.mp4")
  ```

> ESC 키를 누르면 프로그램이 종료됩니다.

---

## 🎨 기능 요약

| 기능        | 설명                                       |
| --------- | ---------------------------------------- |
| **손 인식**  | Mediapipe Hands 모듈을 사용해 손가락 관절을 실시간 추적   |
| **인물 분리** | Mediapipe SelfieSegmentation으로 배경과 인물 분리 |
| **시각화**   | OpenCV를 이용해 결과 프레임을 실시간으로 화면에 표시         |
| **입력 선택** | 동영상 파일 또는 웹캠 입력 모두 지원                    |

---

## 📦 참고 자료

* [MediaPipe Hands 공식 문서](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)
* [MediaPipe Selfie Segmentation 공식 문서](https://developers.google.com/mediapipe/solutions/vision/selfie_segmentation)
* [OpenCV Python Documentation](https://docs.opencv.org/4.x/)

---

## 👨‍💻 작성자

* **프로젝트 이름:** MediaPipe Hand & Selfie Segmentation Demo
* **언어:** Python 3
* **라이브러리:** OpenCV, MediaPipe
