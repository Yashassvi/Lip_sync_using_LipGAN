from pydub import AudioSegment
import os
import subprocess ,argparse ,cv2

parser = argparse.ArgumentParser(description="Arguments required to run the script.")
parser.add_argument('--model_path', type=str, help='Name of saved checkpoint to load weights from', required=True)
parser.add_argument('--face', type=str, help='Filepath of video/image that contains faces to use', required=True)
parser.add_argument('--audio', type=str, help='Filepath of .wav file to use as raw audio source', required=True)
parser.add_argument('--results_dir', type=str, help='Folder to save all results into', default='results/')
parser.add_argument('--fps', type=str, help='FPS of input video, ignore if image', default=25., required=False)

args = parser.parse_args()

def load_images_from_path(input_dir="output\faces"):
	images=[]
	for filename in os.listdir(input_dir):
		img=cv2.imread(os.path.join(input_dir,filename))
		if img is not None:
			images.append(img)
	return images

input_video="input/Kohli_input_video.mp4"
input_audio="input/Kohli-satish.mp3"

# Trimming video
#VideoEd.cut_video(input_file=input_video,from_time="00:00:00.000",to_time="00:00:00.020")

# Extracting frames from video
#VideoEd.extract_video(input_file=args.face, output_dir="output/images", fps=24)

# Denoising frames
#VideoEd.denoise_image_sequence(input_dir="output/images",factor=16)

# Detecting face
#Extractor.main(detector="s3fd",input_path="output/images",output_path="output/faces",face_type="whole_face")

# Input audio
aud=AudioSegment.from_mp3(input_audio)
input_audio=input_audio.split(".")[0]+".wav"
aud.export(input_audio,format="wav")


cmd="python batch_inference.py --checkpoint_path "+args.model_path+" --model residual --face "+args.face+" --fps "+args.fps+" --audio "+args.audio+" --results_dir "+args.results_dir
#os.system("cmd /c "+cmd)
new_dir=os.getcwd()+"\LipGAN"
os.chdir(new_dir)
subprocess.call(cmd, shell=True)