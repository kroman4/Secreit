from keras.preprocessing import image
from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
import Secreit
import tkinter.filedialog
import datetime as dt
import json
import time
import csv
import os

class Stage_Check:


    def __init__(self):
        with open('config.json') as json_file:
            self.data = json.load(json_file)
        self.debug = self.data['settings']['debug']
        self.open_in_excel = self.data['settings']['open_in_excel']
        self.use_graph = self.data['settings']['use_graph']
        self.ask_for_dir = self.data['settings']['ask_for_dir']
        self.images_location = self.data['settings']['images_location']


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


    def write_to_csv(self, data_set):
        '''
        writes results into CSV file.
        '''
        date = dt.datetime.now().strftime('%Y-%m-%d_%H-%M')
        filename = f"{date}_cell_stage_results.csv"
        rows = [['Filename', '%D', '%E', '%P', 'Probable Stage']]
        for data in data_set:
            rows.append([data['Filename'], data['D']+'%', data['E']+'%', data['P']+'%', data['Probable Stage']])
        print(f'Writing results to {filename}')
        with open(filename, 'w') as csvfile:
            writer = csv.writer(csvfile,  lineterminator = '\n')
            writer.writerows(rows)
        if self.open_in_excel:
            os.startfile(filename)


    def image_loop(self):
        '''
        Loops through images in specific folder.
        '''
        if self.ask_for_dir:
            tkinter.Tk().withdraw() # hides blank tkinter window that pop up otherwise
            self.images_location = tkinter.filedialog.askdirectory(initialdir="C:/", title="Select Save Directory")
        print(f'Stage check on images located in {self.images_location}')
        data_list = []
        overall_start= time.perf_counter() # stop time for checking elaspsed runtime
        for cell_image in os.scandir(self.images_location):
            data_list.append(self.main(cell_image))
            if self.debug:
                break
        print('')
        for entry in data_list:
            print(f"{entry['Filename']}\nD:{entry['D']}% E:{entry['E']}% P:{entry['P']}%")
            print(f"Probable Stage: {entry['Probable Stage']}")
        self.write_to_csv(data_list)
        overall_finish = time.perf_counter() # stop time for checking elaspsed runtime
        elapsed_time = round(overall_finish-overall_start, 2)
        print(f'Elapsed Runtime: {elapsed_time} seconds')


if __name__ ==  "__main__":
    App = Stage_Check()
    App.image_loop()
