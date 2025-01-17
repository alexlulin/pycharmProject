import cv2
import numpy as np


def main():
    # 打开视频源，这里假设是摄像头，你可以尝试使用其他方法获取 QQ 视频通话的画面
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    # 读取第一帧
    ret, prev_frame = cap.read()
    if not ret:
        print("Error: Failed to read first frame.")
        return

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 将当前帧转换为灰度图
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 计算帧间差异
        frame_diff = cv2.absdiff(prev_gray, gray)
        _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
        motion_pixels = cv2.countNonZero(thresh)

        # 判断是否有运动
        if motion_pixels > 1000:
            print("Motion detected.")
        else:
            print("No motion detected.")

        # 更新前一帧
        prev_gray = gray

        # 显示视频画面
        cv2.imshow('Video', frame)

        # 按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()