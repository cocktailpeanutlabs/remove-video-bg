import gradio as gr
import cv2
import numpy as np
import time

from PIL import Image
from transparent_background import Remover

def doo(video, mode):
    if(mode == 'Fast'):
        remover = Remover(mode='fast')
    else:
        remover = Remover()
    cap = cv2.VideoCapture(video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    writer = None
    
    processed_frames = 0
    start_time = time.time()
    
    while cap.isOpened():
        ret, frame = cap.read()
    
        if ret is False:
            break

#        if time.time() - start_time >= 55:
#            print("GPU Timeout is coming")
#            cap.release()
#            writer.release()
#            return 'output.mp4'
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        img = Image.fromarray(frame).convert('RGB')
    
        if writer is None:
            writer = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, img.size)

        processed_frames += 1
        print(f"Processing: {processed_frames}")
        out = remover.process(img, type='green')
        writer.write(cv2.cvtColor(np.array(out), cv2.COLOR_BGR2RGB))
    
    cap.release()
    writer.release()
    return 'output.mp4'

title = "🎞️Video Background Removal tool🎥"

description = r"""Please note that if your video file is long (or having high amount of frames) the result may be shorter than input video because of the GPU timeout.<br>
In this case consider trying Fast mode."""

iface = gr.Interface(
    fn=doo, 
    inputs=["video", gr.components.Radio(['Normal', 'Fast'], label='Select mode', value='Normal', info= 'Normal is more accurate, but takes longer. | Fast has lower accuracy so the process will be faster.')], 
    outputs="video", title=title, description=description
)
iface.launch()
