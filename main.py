import os
import numpy as np
import cv2
import matplotlib.pyplot as plt


def open_image(file_name: str) -> np.ndarray:
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', file_name)
    return cv2.imread(file_path)


def get_mask(image: np.ndarray, t: int, acima: bool) -> np.ndarray:
    if acima:
        return image >= t
    else:
        return image < t


def print_histogram(image_in: np.ndarray, image_out: np.ndarray) -> None:
    hist_before = cv2.calcHist([image_in], [0], None, [256], [0, 256])
    hist_after = cv2.calcHist([image_out], [0], None, [256], [0, 256])
    plt.plot(hist_before, label='antes')
    plt.plot(hist_after, label='depois')
    plt.legend(loc='upper center')
    plt.show()


if __name__ == '__main__':
    file_name = 'escola.png'
    t = 100
    acima = True
    brilho = -100
    image_in = open_image(file_name)
    image_mask = get_mask(image_in, t, acima)
    image_out = np.clip(image_in + (image_mask * brilho), 0, 255).astype('uint8')
    cv2.imshow('Imagem de Entrada', image_in)
    cv2.imshow('Imagem de Saida', image_out)
    print_histogram(image_in, image_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    