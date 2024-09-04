import os
import cv2

#Carregar todas as imagens 
def load_images(folder, valid_extensions):
  images =[]
  for fileName in os.listdir(folder):
    _, ext = os.path.splitext(fileName)
    if ext.lower() in valid_extensions:
      images.append(os.path.join(folder, fileName))
  return images  

def create_video(images, output_file, frame_rate=0.5):
  if not images:
    raise ValueError("Nenhuma imagem encontrada para criar vídeo.")
  
  first_frame = cv2.imread(images[0])
  if first_frame is None:
    raise ValueError(f"Não foi possível carregar a imagem.")
  
  height, width, _ = first_frame.shape
  size = (width, height)

  out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, size)

  for image in reversed(images):
    frame = cv2.imread(image)
    if frame is not None:
      out.write(frame)

  out.release()

#Reproduz um vídeo até que a tecla de espaço seja pressionada.
def play_video(video_file):
  cap = cv2.VideoCapture(video_file)
  if not cap.isOpened():
    raise ValueError("Erro ao abrir arquivo de vídeo")
  
  while True:
    ret, frame = cap.read()  
    if not ret:
      break
  
    cv2.imshow('Nascer do Sol', frame)

    if cv2.waitKey(200) & 0xFF == ord(' '):
      break
  
  cap.release()
  cv2.destroyAllWindows()

def main():
  image_folder = "Images"
  output_video = "nascerDoSol.mp4"
  valid_extensions = ['.gif', '.png', '.jpg', '.jpeg', '.jfif']

  images = load_images(image_folder, valid_extensions)
  create_video(images, output_video)
  play_video(output_video)

if __name__ == "__main__":
  main()
