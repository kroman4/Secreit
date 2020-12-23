import tkinter.filedialog
import os
import pprint

class Phase_Check:


    def __init__(self):
        self.debug = 0
        self.ask_for_dir = 0
        self.images_location = 'Cell Images'


    def main(self, cell_image):
        print(cell_image.name)
        if self.debug:
            return
        from keras.preprocessing import image
        from matplotlib import pyplot as plt
        import matplotlib as mpl
        import numpy as np
        import Secreit
        model = Secreit.vgg_model('weights.hdf5')
        img = image.load_img(cell_image.path)
        data_set = {}

        plt.imshow(img)

        predict = Secreit.predict(img, model)
        filename = cell_image.name
        d_percent = str(round(predict[0]*100))
        e_percent = str(round(predict[1]*100))
        p_percent = str(round(predict[2]*100))

        data_set['Filename'] = filename
        data_set['D'] = f'{d_percent}%'
        data_set['E'] = f'{e_percent}%'
        data_set['P'] = f'{p_percent}%'

        imgd = image.array_to_img(Secreit.Cam(np.array(img), "D", model))
        imge = image.array_to_img(Secreit.Cam(np.array(img), "E", model))
        imgp = image.array_to_img(Secreit.Cam(np.array(img), "P", model))

        mpl.rcParams['figure.figsize'] = [20, 4]

        plt.subplot(1,4,1)
        plt.imshow(img)
        plt.title(d_percent + e_percent + p_percent, fontsize = 25)

        plt.subplot(1,4,2)
        plt.imshow(imgd)
        plt.title("D place", fontsize = 25)

        plt.subplot(1,4,3)
        plt.imshow(imge)
        plt.title("E place", fontsize = 25)

        plt.subplot(1,4,4)
        plt.imshow(imgp)
        plt.title("P place", fontsize = 25)
        return data_set


    def image_loop(self):
        '''
        Loops through images in specific folder
        '''
        if self.debug:
            print('Running debug version of code. If you are expecting results, change self.debug to 0.')
        if self.ask_for_dir:
            tkinter.Tk().withdraw() # hides blank tkinter window that pop up otherwise
            self.images_location  = tkinter.filedialog.askdirectory(initialdir="C:/", title="Select Save Directory")
        print(f'Phase check on images located in {self.images_location}')
        data_list = []
        for cell_image in os.scandir(self.images_location):
            data_list.append(self.main(cell_image))
        pprint.pprint(data_list)
        # TODO Add .csv output format for results.


if __name__ ==  "__main__":
    App = Phase_Check()
    App.image_loop()
