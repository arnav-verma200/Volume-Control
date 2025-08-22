import mediapipe as mp
import cv2
import math as m

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

smooth_vol = 0
smoothing_factor = 0.1  # smaller = smoother

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands(4)
mpdraw = mp.solutions.drawing_utils

while True:
  suc, frame = cap.read()
  frame = cv2.flip(frame,1)
  frame = cv2.GaussianBlur(frame, (5, 5), 0)
  sf = 0.5
  h,w = frame.shape[:2]
  h2 = int(h*sf)
  w2 = int(w*sf)
  frame = cv2.resize(src=frame, dsize=(w2, h2), interpolation=cv2.INTER_CUBIC)

  frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  results = hands.process(frame_rgb)
  #print(results.multi_hand_landmarks)

  if results.multi_hand_landmarks:
      for handlms in results.multi_hand_landmarks: # handlms has the coordinates of each pt
          mpdraw.draw_landmarks(frame, handlms, mphands.HAND_CONNECTIONS)

          llm = []

          for id, lm in enumerate(handlms.landmark):
              #print(id, lm)
              h,w,_ = frame.shape
              cx, cy = int(lm.x*w), int(lm.y * h)
              llm.append([id,cx,cy])
            
          cv2.line(frame, (llm[4][1],llm[4][2]), (llm[8][1],llm[8][2]), (255,0,0), 2)
          dist = m.sqrt(((llm[4][1] - llm[8][1])**2)+((llm[4][2] - llm[8][2])**2))

          min_dist = 15
          max_dist = 150

          vol = (dist - min_dist) / (max_dist - min_dist)
          vol = max(0.0, min(1.0, vol))

          smooth_vol = smooth_vol + (vol - smooth_vol) * smoothing_factor

          volume.SetMasterVolumeLevelScalar(smooth_vol, None)
          cv2.putText(frame, f"Volume: {int(smooth_vol*100)}%", (50, 100),
          cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 23), 2)

  cv2.imshow("V", frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
        break
