from keras.preprocessing import image
from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
import Secreit
import tkinter.filedialog
import os
import matplotlib.rcsetup as rcsetup
print(rcsetup.all_backends)

class Stage_Check:


    def __init__(self, debug=0, use_graph=1, ask_for_dir=0, def_images_location=''):
        self.debug = debug
        self.use_graph = use_graph
        self.ask_for_dir = ask_for_dir
        self.def_images_location = def_images_location


    def main(self, cell_image):
        '''
        Modified Secreit codde.
        Returns dictionary with analyzed information.
        '''
        model = Secreit.vgg_model('weights.hdf5')
        img = image.load_img(cell_image.path)
        data_set = {}

        plt.imshow(img)

        predict = Secreit.predict(img, model)

        filename = cell_image.name
        d_percent = str(round(predict[0]*100))
        e_percent = str(round(predict[1]*100))
        p_percent = str(round(predict[2]*100))

        Stages = {
            'D':'Diestrus',
            'E':'Estrus',
            'P':'Proestrus'
                }
        data_set['D'] = d_percent
        data_set['E'] = e_percent
        data_set['P'] = p_percent
        data_set['Probable Stage'] = Stages[list(filter(lambda x:x[1] == max(data_set.values()), data_set.items()))[0][0]]
        data_set['Filename'] = filename

        if self.use_graph == 1:
            imgd = image.array_to_img(Secreit.Cam(np.array(img), "D", model))
            imge = image.array_to_img(Secreit.Cam(np.array(img), "E", model))
            imgp = image.array_to_img(Secreit.Cam(np.array(img), "P", model))

            mpl.rcParams['figure.figsize'] = [20, 4]

            plt.subplot(1,4,1)
            plt.imshow(img)
            plt.title(f'D:{d_percent}% E:{e_percent}% + P:{p_percent}%', fontsize = 25)

            plt.subplot(1,4,2)
            plt.imshow(imgd)
            plt.title("D place", fontsize = 25)

            plt.subplot(1,4,3)
            plt.imshow(imge)
            plt.title("E place", fontsize = 25)

            plt.subplot(1,4,4)
            plt.imshow(imgp)
            plt.title("P place", fontsize = 25)

            plt.show
        return data_set


    def image_loop(self):
        '''
        Loops through images in specific folder.
        '''
        if self.ask_for_dir:
            tkinter.Tk().withdraw() # hides blank tkinter window that pop up otherwise
            self.def_images_location  = tkinter.filedialog.askdirectory(initialdir="C:/", title="Select Save Directory")
        print(f'Stage check on images located in {self.def_images_location}')
        data_list = []
        for cell_image in os.scandir(self.def_images_location):
            data_list.append(self.main(cell_image))
            if self.debug:
                break
        print('')
        for entry in data_list:
            print(f"{entry['Filename']}\nD:{entry['D']}% E:{entry['E']}% P:{entry['P']}%")
            print(f"Probable Stage: {entry['Probable Stage']}")
        # TODO Add .csv output format for results.


if __name__ ==  "__main__":
    App = Stage_Check(debug=0, use_graph=0, ask_for_dir=0, def_images_location='Cell Images')
    App.image_loop()
