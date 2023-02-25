from tracer_tests.tracertests import *
import pandas as pd
from file_utils.sensor_data_file import SensorPairData
import math as mt
from plot_settings.plotSensors2 import *
from logging_parameters.checker import *
import numpy as np


def darcys_velocity_each_second(field_data, m, b):
    """
    :param field_data: data from the field experiment (fluorescense every second )
    :param m: slope of the sensor's equation
    :param b: intercept of the sensor's equation
    :return: Data frame containing the final Darcy's velocity
    """
    # creation of an empty dictionary with headers names
    sol_dict = {"Time": [],
                "Flourscense": [],
                "Uranine(mg/l)": [],
                "ln(c/c0)": [],
                "vf(m/s)": []
                }
    # instanciation of the class Tracer as a variable named a
    a = Tracer()
    # iteration loop over the fluorescense readings
    for i, flo in enumerate(list(field_data["fluorescense"])):
        # excluding not numerical input
        if not str(flo).lower() == "nan":
            logging.info("PROCESSING AT TIME {0} CONCENTRATION {1}".format(str(field_data["dilution time (s)"][i]),
                                                                           str(field_data["fluorescense"][i])))
            # excluding appending time and Flourscense values
            sol_dict["Time"].append(field_data["dilution time (s)"][i])
            sol_dict["Flourscense"].append(field_data["fluorescense"][i])

            # calculating and appending Uraninine values only if the Flourscense value is greater than the measurement device accuracy
            if sol_dict["Flourscense"][i] <= a.acc:
                logging.info("Fluorescence value {0} is less than the accuracy, then it is replaced by 0.001".format(
                    str(sol_dict["Flourscense"][i])))
                sol_dict["Uranine(mg/l)"].append(0.001)
            elif sol_dict["Flourscense"][i] > a.acc:
                sol_dict["Uranine(mg/l)"].append((sol_dict["Flourscense"][i])*m + b)

            # calculating ln(c/c0) while avoiding negatine values for the natural log
            # also avoiding deviding by zero
            if sol_dict["Uranine(mg/l)"][i] < 0.00:
                logging.info("Uranin value {0} is negative, so it's replace by np.nan".format(
                    str(sol_dict["Uranine(mg/l)"][i])))
                sol_dict["ln(c/c0)"].append(np.nan)
            else:
                try:
                    sol_dict["ln(c/c0)"].append(np.log(sol_dict["Uranine(mg/l)"][i]/a.c))
                except ZeroDivisionError as e:
                    logging.warning('Division error occurred: ', e)
                    return sol_dict["ln(c/c0)"].append(np.nan)
            sol_dict["vf(m/s)"].append(a.calculate_vf(sol_dict["ln(c/c0)"][i], sol_dict["Time"][i]))
    # returning of the calculations as panda data-frame
    return pd.DataFrame(sol_dict)

def darcys_velocity_averaged(dataframe):
    """
    :param dataframe: the values of Darcy's velocity as an output from the above function (darcys_velocity_each_second)
    :return: averaged dacy velocity, the upper and lower 25% values are excluded == 50% percentile range
    """
    l = dataframe["vf(m/s)"].__len__()
    velocity_column = dataframe["vf(m/s)"]
    average_velocity = (velocity_column[mt.ceil(l / 4):mt.ceil(3 * l / 4)]).mean()
    return average_velocity

@logger
def main():
    sensor_pair = SensorPairData(
        name="Main Sensor Pair",
        filepath="Input_data_workbook/All_Data.xlsx"
    )
    # instantiation of class objects, attributes
    df_time_v_conc_dc = sensor_pair.dc_data.data
    df_time_v_conc_fc = sensor_pair.fc_data.data
    df_time_con_cal_dc = sensor_pair.dc_cal_data.data
    df_time_con_cal_fc = sensor_pair.fc_cal_data.data
    # finding calibration equation
    calibration_test_data = sensor_pair.check_calibration()

    dc_b, dc_m = calibration_test_data["DC"]
    logging.info(f'DC Regression Line is y = {calibration_test_data["DC"][0]} * x {calibration_test_data["DC"][1]}')
    fc_b, fc_m = calibration_test_data["FC"]
    logging.info(f'FC Regression Line is y = {calibration_test_data["FC"][0]} * x {calibration_test_data["FC"][1]}')

    # calculating Darcy's Velocity for both sensors
    logging.debug(f'Calculating Darcy Velocity from DC sensors')
    df_darcys_vel_dc = darcys_velocity_each_second(df_time_v_conc_dc, dc_m, dc_b)
    logging.debug(f'Calculating Darcy Velocity from FC sensors')
    df_darcys_vel_fc = darcys_velocity_each_second(df_time_v_conc_fc, fc_m, fc_b)

    logging.info("Darcy´s velocity from the diving cell {0} ".format(str(darcys_velocity_averaged(df_darcys_vel_dc))))
    logging.info("Darcy´s velocity from the flowing cell {0} ".format(str(darcys_velocity_averaged(df_darcys_vel_fc))))

    #sasvig the results as excel file named "Results.xlsx"
    with pd.ExcelWriter("Results.xlsx") as writer:
        df_darcys_vel_dc.to_excel(writer, sheet_name="floating_cell")
        df_darcys_vel_fc.to_excel(writer, sheet_name="diving_cell")

    # PLOTS
    sensors_plot(df_time_con_cal_dc, df_time_con_cal_fc)
    velocity_plot(df_darcys_vel_dc, df_darcys_vel_fc)
    time_concentration_plot(df_darcys_vel_dc, df_darcys_vel_fc)

if __name__ == "__main__":
    main()
