#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import mediapipe as mp
import yt_dlp

# ================================
# YouTube 스트림 URL 입력
# ================================
def get_youtube_stream(url):
    """
    YouTube 링크로부터 OpenCV가 처리할 mp4 스트림 URL 반환
    """
    ydl_opts = {
        'quiet': True,             # 불필요한 로그 제거
        'format': 'best[ext=mp4]/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info['url']

youtube_url = "https://www.youtube.com/shorts/P9W0PTT300I?feature=share"
print("YouTube 스트림 URL 확인:", youtube_url)
video_stream = get_youtube_stream(youtube_url)

# ================================
# Mediapipe 손 인식 초기화
# ================================
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# ================================
# YouTube 영상 열기
# ================================
cap = cv2.VideoCapture(video_stream)

if not cap.isOpened():
    print("⚠️ YouTube 영상을 열 수 없습니다.")
    exit()

print("✅ YouTube 스트림 영상 시작 - ESC 눌러 종료합니다.")

# ================================
# 영상 프레임 처리
# ================================
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("⚠️ 영상 스트림 끝 또는 프레임을 읽지 못했습니다.")
        break

    # BGR -> RGB 변환
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    # ================================
    # 손 랜드마크 그리기
    # ================================
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_styles.get_default_hand_landmarks_style(),
                mp_styles.get_default_hand_connections_style()
            )

    # ================================
    # 영상 표시
    # ================================
    cv2.imshow('Mediapipe Hand Detector (YouTube)', image)

    if cv2.waitKey(5) & 0xFF == 27:  # ESC
        print("🔚 종료합니다.")
        break

# ================================
# 종료 처리
# ================================
cap.release()
cv2.destroyAllWindows()
