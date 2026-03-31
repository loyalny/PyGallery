import cv2
import numpy as np
from pathlib import Path
import os

import extensions

import resources


def generate_preview(source_path, previews_dir, size):
    target_dir = Path(os.path.join(previews_dir, "previews")).resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    source = Path(source_path).resolve()
    final_path = target_dir / f"{source.stem}_preview.jpg"

    index = 2
    while final_path.exists():
        final_path = target_dir / f"{source.stem}_preview_{index}.jpg"
        index += 1

    error_icon =  ":/icons/icons/error_24dp_444746_FILL0_wght400_GRAD0_opsz24.png"

    image = None
    extension = source.suffix.lower()

    try:
        if extension in extensions.img_ext:
            img_array = np.fromfile(str(source), np.uint8)
            image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        elif extension in extensions.vid_ext:
            video = cv2.VideoCapture(str(source))

            total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            frame_to_read = 10 if total_frames > 10 else 0

            video.set(cv2.CAP_PROP_POS_FRAMES, frame_to_read)
            success, frame = video.read()
            if success:
                image = frame
            video.release()

        if image is None:
            return error_icon

        h, w = image.shape[:2]
        min_side = min(h, w)
        start_x = (w - min_side) // 2
        start_y = (h - min_side) // 2
        cropped = image[start_y:start_y + min_side, start_x:start_x + min_side]

        final_image = cv2.resize(cropped, (size, size), interpolation=cv2.INTER_AREA)

        is_success, buffer = cv2.imencode(".jpg", final_image, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
        if is_success:
            with open(final_path, "wb") as f:
                f.write(buffer)
            return final_path

    except (IOError, OSError, cv2.error):
        return error_icon

    return error_icon
