import pandas as pd
import os
import matplotlib.pyplot as plt

from constants import SURVEY_INPUT_FOLDER, SURVEY_FILENAME, SURVEY_OUTPUT_FOLDER, SURVEY_IMAGE_NAME
from index import generate_index

def plot_analysis(to_file):
    """plot graph for 4 parameters of the survey

    Parameters
    ----------
    to_file : bool
        True is the graphes are printed to an html file
        False if the graphes are ploted to the screen
    """

    # define filepaths
    current_path = os.path.abspath(os.getcwd())
    survey_input_path = os.path.join(current_path,SURVEY_INPUT_FOLDER)
    survey_filepath = os.path.join(survey_input_path,SURVEY_FILENAME)
    image_path = os.path.join(current_path,SURVEY_OUTPUT_FOLDER)
    image_filepath = os.path.join(image_path,SURVEY_IMAGE_NAME)


    df = pd.read_csv(survey_filepath, encoding='utf-8', sep=';')

    # Rename column
    df_sel = df[['OS ?','Version ?','Virtual ?','IDE ?']]
    df_sel.columns = ['Installed_OS','Python_Version','Used_Virtual_Env','Used_IDE']

    df_python_version = df_sel['Python_Version'].value_counts()
    df_virtual_env = df_sel['Used_Virtual_Env'].value_counts()
    df_installed_os = df_sel['Installed_OS'].value_counts()

    df_sel['Used_IDE'] = df_sel['Used_IDE'].apply(lambda x : x.split('/')[0])
    df_used_ide = df_sel['Used_IDE'].value_counts()

    fig = plt.figure(figsize=(20,20))
    fig.suptitle("Visualisation of Survey.csv file", fontsize=18)

    ax = fig.add_subplot(221)
    df_installed_os.plot.pie(ax = ax,autopct='%1.1f%%', startangle=90,explode = (0,0.15,0.15),fontsize=12)
    plt.title('Percentage of student\nusing the different IDE')
    plt.xlabel('')
    plt.ylabel('')

    a0 = fig.add_subplot(222)
    df_python_version.plot(ax = a0, kind = 'bar')
    plt.title('Number of student using the \n different Python version')
    plt.xlabel('Python Version')
    plt.ylabel('Number of student')

    a1 = fig.add_subplot(223)
    df_virtual_env.plot(ax = a1, kind = 'bar')
    plt.title('Number of student using \nthe different virtual environment')
    plt.xlabel('Virtual Environment')
    plt.ylabel('Number of student')
    a1.set_yticks(range(0,max(df_virtual_env),5))

    a2 = fig.add_subplot(224)
    df_used_ide.plot(ax = a2, kind = 'pie',autopct='%1.1f%%', startangle=270,explode = (0,0.15,0,0,0,0,0,0,0),fontsize=10)
    plt.title('Percentage of student\nusing the different IDE')
    plt.xlabel('')
    plt.ylabel('')

    if to_file == 'file':
        if not os.path.exists(image_path):
            os.makedirs(image_path)
        fig.savefig(image_filepath)
        generate_index(image_path,SURVEY_IMAGE_NAME)
    else:
        plt.show()
