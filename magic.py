
def zip_all_mov_in_cur_dir():
    import cv2
    start_index = 0
    files = os.listdir(os.getcwd())

    cap = cv2.VideoCapture()
    for f in files:
        tail = f.split('.').pop()
        if tail in ['mov', 'MOV', 'mp4']:
            new_name = str(start_index) + tail
            os.rename(f, new_name)
            cap.open(new_name)
            cap.set(cv2.CAP_PROP_POS_MSEC, 0)
            success, frame = cap.read()
            if success:
                cv2.imwrite('../img/' + str(start_index) + 'jpg', frame)
            # 加密压缩
            command = f'zip -P !@#zt1314lj716126 ../zip/{new_name}.zip {new_name}'
            os.system(command)
            start_index += 1
    cap.release()

