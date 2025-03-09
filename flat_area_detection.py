import pyrealsense2 as rs
import numpy as np
import cv2

# Initialize RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
pipeline.start(config)

while True:
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    
    if not depth_frame:
        continue

    # Convert depth frame to numpy array
    depth_image = np.asanyarray(depth_frame.get_data())

    # Set a depth threshold (adjust 500, 1500 based on environment)
    min_depth = 500  # Minimum depth in mm (0.5m)
    max_depth = 1500  # Maximum depth in mm (1.5m)
    flat_area = cv2.inRange(depth_image, min_depth, max_depth)

    # Display result
    cv2.imshow("Flat Area Detection", flat_area)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

pipeline.stop()
cv2.destroyAllWindows()





