# create-video-py


## 💻 Sobre o projeto
Este projeto consiste em criar um vídeo a partir de uma sequência de imagens utilizando Python e OpenCV. As imagens são lidas de um diretório específico, processadas e combinadas em um vídeo que é salvo localmente. Após a criação, o vídeo é exibido até que a tecla de espaço seja pressionada.
## ⚙️ Funcionalidades
- [x] Ler todas as imagens do diretório Images.
- [x] Criar um vídeo a partir dessas imagens.
- [x] Salvar o vídeo como nascerDoSol.mp4.
- [x] Exibir o vídeo em uma janela. A janela permanecerá aberta e o vídeo será reproduzido e encerrado automáticamente ou até que a tecla de espaço seja pressionada.

### Pré-requisitos

- [Python 3](https://www.python.org/downloads/)
- [OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

Você pode instalar o OpenCV usando o seguinte comando:
  - pip install opencv-python

### Notas 
- Certifique-se de que todas as imagens no diretório tenham a mesma resolução para evitar problemas de dimensionamento no vídeo final.
- O frame rate (frame_rate =1) e o intervalo de exibição (cv2.waitKey(200)) podem ser ajustados para modificar a velocidade de transição entre as imagens.

### Contribuição  
- Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.


[![GitHub license](https://badgen.net/github/license/Naereen/Strapdown.js)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
