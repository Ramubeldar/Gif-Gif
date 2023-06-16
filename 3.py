import os
import imageio
import cv2

# Specify the input folder containing GIF files
input_folder = "input_folder"

# Specify the output video file
output_file = "output3.mp4"

# Get the list of GIF files in the input folder
gif_files = [filename for filename in os.listdir(input_folder) if filename.endswith(".gif")]

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = 30  # Adjust the frames per second as needed
output_video = cv2.VideoWriter(output_file, fourcc, fps, (640, 480))  # Adjust the frame size as needed

# Iterate over the GIF files and write frames to the output video
for gif_file in gif_files:
    gif_path = os.path.join(input_folder, gif_file)
    gif_frames = imageio.mimread(gif_path)

    # Resize the frames to match the output video size
    resized_frames = [cv2.resize(frame, (640, 480)) for frame in gif_frames]

    # Extract each frame from the GIF and write it to the video
    for frame in resized_frames:
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        output_video.write(frame_bgr)

# Release the video writer
output_video.release()
