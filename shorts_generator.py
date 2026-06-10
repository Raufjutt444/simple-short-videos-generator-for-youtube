import subprocess
import os

def landscape_to_verticals(input_path, output_dir, num_clips=10):
    os.makedirs(output_dir, exist_ok=True)

    # Get video dimensions
    probe = subprocess.run([
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height",
        "-of", "csv=p=0",
        input_path
    ], capture_output=True, text=True)
    width, height = map(int, probe.stdout.strip().split(","))

    # Get duration
    duration_probe = subprocess.run([
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "csv=p=0",
        input_path
    ], capture_output=True, text=True)
    total_duration = float(duration_probe.stdout.strip())

    clip_duration = total_duration / num_clips
    crop_w = int(height * 9 / 16)
    max_offset = width - crop_w

    for i in range(num_clips):
        start_time = i * clip_duration
        x_offset = (width - crop_w) // 2

        output_path = os.path.join(output_dir, f"vertical_{i+1}.mp4")

        vf = (
    
    f"crop={crop_w}:{height}:{x_offset}:0,"
    f"scale=1080:1920,"
    f"drawtext="
    f"fontfile='arial.ttf':"
    f"text='Subscribe':"
    f"fontsize=60:"
    f"fontcolor=white:"
    f"x=(w-text_w)/2:"
    f"y=50:"
    f"box=1:"
    f"boxcolor=black@0.5:"
    f"boxborderw=10"
)

        subprocess.run([
            "ffmpeg", "-i", input_path,
            "-ss", str(start_time),
            "-t", str(clip_duration),
            "-vf", vf,
            "-c:v", "libx264",
            "-preset", "ultrafast",
            "-c:a", "copy",
            output_path
        ])
        print(f"Clip {i+1}: {start_time:.1f}s → {start_time+clip_duration:.1f}s ✓")

    print("All done!")

# Run it
landscape_to_verticals("YTDown_YouTube_WAIT-WHAT-Minecraft-7-S4_Media_ewvOFZyUTIc_001_1080p.mp4", "output_clips/", num_clips=10)