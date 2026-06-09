import os
from PIL import Image

def extract_frames(input_file, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        with Image.open(input_file) as im:
            print(f"Format: {im.format}, Size: {im.size}, Mode: {im.mode}")
            
            frame_count = 0
            while True:
                # Convert the image to RGB to save as high-quality JPEG to ensure browser compat and speed
                # Or we can save as webp. Since the source is webp, we save as webp.
                output_file = os.path.join(output_folder, f"frame_{frame_count:04d}.webp")
                
                # Pillow might complain if the mode is something weird, but usually it's fine for webp
                im.save(output_file, 'WEBP', quality=85)
                
                frame_count += 1
                
                # Print progress every 10 frames
                if frame_count % 10 == 0:
                    print(f"Extracted {frame_count} frames...")
                    
                try:
                    im.seek(im.tell() + 1)
                except EOFError:
                    break
                    
        print(f"Successfully extracted {frame_count} frames to {output_folder}")
    except Exception as e:
        print(f"Error extracting frames: {e}")

if __name__ == "__main__":
    extract_frames("index.webp", "frames")
