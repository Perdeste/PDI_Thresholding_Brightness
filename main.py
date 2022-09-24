import os
import numpy as np
import cv2


def open_image(file_name: str) -> np.ndarray:
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', file_name)
    return cv2.imread(file_path)


def get_mask(image: np.ndarray, t: int, acima: bool) -> np.ndarray:
    if acima:
        return image >= t
    else:
        return image < t


if __name__ == '__main__':
    file_name = 'example_1.png'
    image_in = open_image(file_name)
    if type(image_in) != None:
        t = 120
        acima = True
        brilho = 50
        image_mask = get_mask(image_in, t, acima)
        image_out = np.clip(image_in + (image_mask * brilho), 0, 255).astype('uint8')
        cv2.imshow('Imagem de Entrada', image_in)
        cv2.imshow('Imagem de Saida', image_out)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f'Não foi possível carregar a imagem {file_name}')
    