from matplotlib import pyplot as plt


class Visualization:

    def draw_histogram(df):
        plt.hist(df['age'])
        return "a"
