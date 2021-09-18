import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

IMG_FOLDER = '/home/tuts/repos/tutss/calendar-tracker/img/'

class CalendarDataframe():
    def __init__(self, file_path, img_file):
        self.df = pd.read_csv(file_path)
        self.save_path = IMG_FOLDER + img_file[:-4] + '/' # last 3 chars are extension and .
        
        plt.style.use('ggplot')
        plt.rcParams["figure.figsize"] = (20,10)

        if not os.path.isdir(self.save_path):
            os.makedirs(self.save_path)


    def analysis(self):
        self.process_and_format()
        gb = self.sum_by_hours()
        self.make_plots(gb)

    def make_plots(self, df):
        self.barplot(df, 'summary', 'duration')
        self.pieplot(df, col='duration_per_cent', labels='summary')

    def sum_by_hours(self):
        gb = self.df.groupby('summary', as_index=False).sum()
        gb['duration_per_cent'] = (gb.duration / gb.duration.sum())*100
        return gb

    def process_and_format(self):
        self.df['summary'] = self.df.summary.str.lower()
        self.df['summary'] = self.df.summary.str.strip()

    def barplot(self, df, x, y):
        sns.barplot(data=df, x=x, y=y)
        plt.xticks(rotation=45)
        plt.savefig(f'{self.save_path}barplot.png')

    def pieplot(self, df, col, labels):
        plt.pie(df[col], labels=df[labels], rotatelabels=True)
        plt.savefig(f'{self.save_path}pieplot.png')
    