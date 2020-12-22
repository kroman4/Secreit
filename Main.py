from keras.preprocessing import image
from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
import Secreit
import os

class Phase_Check:


    def __init__(self):
        self.images_location = 'Cell Images'


    def main(self, cell_image):
        print(cell_image)
        model = Secreit.vgg_model("*/weights.hdf5")
        img = image.load_img(cell_image)

        plt.imshow(img)

        predict=Secreit.predict(img, model)
        print('D:'+str(round(predict[0]*100))+'%, E:'+str(round(predict[1]*100))+'%, P:'+str(round(predict[2]*100))+'%')

        imgd=image.array_to_img(Secreit.Cam(np.array(img), "D", model))
        imge=image.array_to_img(Secreit.Cam(np.array(img), "E", model))
        imgp=image.array_to_img(Secreit.Cam(np.array(img), "P", model))

        mpl.rcParams['figure.figsize'] = [20, 4]

        plt.subplot(1,4,1)
        plt.imshow(img)
        plt.title('D:'+str(round(predict[0]*100))+'%, E:'+str(round(predict[1]*100))+'%, P:'+str(round(predict[2]*100))+'%', fontsize=25)

        plt.subplot(1,4,2)
        plt.imshow(imgd)
        plt.title("D place", fontsize=25)

        plt.subplot(1,4,3)
        plt.imshow(imge)
        plt.title("E place", fontsize=25)

        plt.subplot(1,4,4)
        plt.imshow(imgp)
        plt.title("P place", fontsize=25)


    def image_loop(self):
        for cell_image in os.scandir(self.images_location):
            self.main(cell_image.path)


if __name__ == "__main__":
    App = Phase_Check()
    App.image_loop()
