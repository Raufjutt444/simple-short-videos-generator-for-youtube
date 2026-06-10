# Landscape to Vertical Video Converter

A Python script that converts a landscape video into multiple vertical (9:16) clips, perfect for TikTok, YouTube Shorts, and Instagram Reels.

## What it does
- Splits a long landscape video into multiple short vertical clips
- Crops from the center of the frame
- Adds a "Subscribe" text overlay at the top
- Outputs in 1080x1920 resolution

## Requirements

### 1. Python
Download from https://python.org  
Make sure to check "Add Python to PATH" during installation.

### 2. FFmpeg
Install via terminal:
```
winget install ffmpeg
```
Then restart your terminal.

### 3. Python package
```
python3 -m pip install ffmpeg-python
```

### 4. Font file
Copy `arial.ttf` from `C:\Windows\Fonts\` and paste it in the same folder as the script.

## How to use

1. Put your video in the same folder as the script
2. Edit the last line in `script.py` to match your filename and how many clips you want:
```python
landscape_to_verticals("your_video.mp4", "output_clips/", num_clips=10)
```
3. Run the script:
```
python script.py
```
4. Find your clips in the `output_clips/` folder

## Output
- Each clip is approximately 40-50 seconds long
- Vertical 9:16 format (1080x1920)
- "Subscribe" text overlay at the top
- Ready to upload to TikTok, Reels, or Shorts

## Folder structure
```
project/
├── script.py
├── arial.ttf
├── your_video.mp4
└── output_clips/
    ├── vertical_1.mp4
    ├── vertical_2.mp4
    └── ...
```
