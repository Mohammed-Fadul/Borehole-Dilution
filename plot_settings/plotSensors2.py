from plot_settings.plot_saver import *
import numpy as np


def sensors_plot(dc_data_cal, fc_data_cal):
    fig, ax = plt.subplots()

    x = np.array(dc_data_cal['Flourescense'])
    y = np.array(dc_data_cal['Concentration'])

    plt.scatter(x, y, label='DC data',
                c="blue", linewidths=2,
                marker="s", edgecolor="green",
                s=50)

    # FC data
    x2 = np.array(fc_data_cal['Flourescense'])
    y2 = np.array(fc_data_cal['Concentration'])

    plt.scatter(x2, y2, label='FC data',
                c="yellow", linewidths=2,
                marker="s", edgecolor="red",
                s=50)

    ax.set(xlabel='Flourescence(-) gain 1', ylabel='µg/L Uranine',
           title='LLF6 with FC14 and DC 17,8 m')
    ax.grid()

    # Linear regression line
    m, b = np.polyfit(x, y, 1)
    m2, b2 = np.polyfit(x2, y2, 1)
    plt.plot(x, m*x+b)
    plt.plot(x2, m2*x2+b2)

    plt.legend()
    save_plot(folder_path="Plots", plot=plt, name="Sensors Plot")
    return


def time_concentration_plot(test_dc, test_fc):
    fig, ax = plt.subplots()

    x = np.array(test_dc['Time'])
    y = np.array(test_dc["Flourscense"])
    y2 = np.array(test_fc["Flourscense"])

    plt.scatter(x, y, label='DC tracer',
                c="blue", linewidths=2,
                marker="s", edgecolor="green",
                s=5)
    plt.scatter(x, y2, label='FC tracer',
                c="pink", linewidths=2,
                marker="s", edgecolor="red",
                s=5)

    plt.plot(x, y)
    plt.plot(x, y2)

    ax.set(xlabel='time (s)', ylabel='c (µg/L)', yscale='log',
           title='Borehole Dilution Test')
    ax.grid(True)
    plt.legend()

    save_plot(folder_path="Plots", plot=plt, name="Time vs Concentration")


def velocity_plot(test_dc, test_fc):

    x = np.array(test_dc['Time'])
    y = np.array(test_dc["vf(m/s)"])
    z = np.array(test_fc["Uranine(mg/l)"])

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set(xlabel='time (s)', ylabel='velocity (m/s)', yscale='log', title='Borehole Dilution Test')
    ax1.plot(x, y, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('Uranine mg/l', color=color)
    ax2.plot(x, z, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()

    save_plot(folder_path="Plots", plot=plt, name="Velocity vs Concentration")
