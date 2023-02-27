import logging
from file_utils.base_files import BaseFile
import pandas as pd
import numpy as np
from typing import List
from sklearn.linear_model import LinearRegression

#classes to check if specified column names exists
class DataSheet:
    def __init__(self,
                 data_dataframe: pd.DataFrame,
                 parameters: List[str] = ["dilution time (s)", "fluorescense"]
                 ):
        self.parameters = parameters
        self.combined_data_dataframe = data_dataframe
        self.__verify_parameters()
        self.data = self.combined_data_dataframe

    def __verify_parameters(self):
        if not all([param in self.combined_data_dataframe.columns for param in self.parameters]):
            raise Exception(logging.error(f"Invalid column names for parameters: {self.parameters}"))

class CalibrationSheet:
    def __init__(self,
                 calibration_dataframe: pd.DataFrame,
                 parameters: List[str] = ["Concentration", "Flourescense"]
                 ):
        self.parameters = parameters
        self.combined_calibration_dataframe = calibration_dataframe
        self.__verify_parameters()
        self.data = self.combined_calibration_dataframe

    def __verify_parameters(self):
        if not all([param in self.combined_calibration_dataframe.columns for param in self.parameters]):
            raise Exception(logging.error(f"Invalid column names for parameters: {self.parameters}"))

#Separate classes have be written for field data and calibration data so that if the names of the data is changed in future in either of the files, it can be altered in the code in the specific class for that data, without disturbing the other
            
#authoured by Chinmayee
class SensorPairData(BaseFile):
    def __init__(
            self,
            name: str,
            filepath: str,
            dc_data_sheet_name: str = "Data DC",
            fc_data_sheet_name: str = "Data FC",
            dc_cal_sheet_name: str = "DC_calibration",
            fc_cal_sheet_name: str = "FC_calibration",
            **kwargs
    ):
        self.name = name
        super().__init__(filepath)
        self.__dc_data_sheet_name = dc_data_sheet_name
        self.__fc_data_sheet_name = fc_data_sheet_name
        self.__dc_cal_sheet_name = dc_cal_sheet_name
        self.__fc_cal_sheet_name = fc_cal_sheet_name
        self.__read_sensor_excel()

    def __read_sensor_excel(self):
        try:
            logging.debug('Taking information from the excel sheet...')
            self.dc_data = pd.read_excel(self.filepath, sheet_name=self.__dc_data_sheet_name)
            self.fc_data = pd.read_excel(self.filepath, sheet_name=self.__fc_data_sheet_name)
            self.dc_cal_data = pd.read_excel(self.filepath, sheet_name=self.__dc_cal_sheet_name)
            self.fc_cal_data = pd.read_excel(self.filepath, sheet_name=self.__fc_cal_sheet_name)
        except Exception as e:
            logging.critical(f'Invalid inputs that track information from excel. Check them again:'
                             f'\n{self.__dc_data_sheet_name},\n{self.__fc_data_sheet_name},'
                             f'\n{self.__dc_cal_sheet_name},\n{self.__fc_cal_sheet_name}')

#Write the data and calibration sheets to `DataSheet` and `CalibrationSheet` classes
        self.dc_data = DataSheet(data_dataframe=self.dc_data)
        self.fc_data = DataSheet(data_dataframe=self.fc_data)
        self.dc_cal_data = CalibrationSheet(calibration_dataframe=self.dc_cal_data)
        self.fc_cal_data = CalibrationSheet(calibration_dataframe=self.fc_cal_data)

    def check_calibration(self):
        """
        Checks for both FC and DC calibration data

        :return: tuple(FC_cal_vals, DC_cal_vals)
        """
        return {
            "FC": self.__check_sub_cal(in_data=self.fc_cal_data.data),
            "DC": self.__check_sub_cal(in_data=self.dc_cal_data.data)
        }


#Calculation of Coefficient of determination of the calibration data
    def __check_sub_cal(
            self,
            in_data: pd.DataFrame,
            return_coeffs: bool = True
    ):
        x = in_data["Flourescense"].values.reshape(-1, 1)
        y = in_data["Concentration"]
        self.model = LinearRegression().fit(x, y)
        r_sq = self.model.score(x, y)
        logging.info(f"CALIBRATION : Coefficient of Determination: \t {r_sq}")

        a = self.model.intercept_
        b = self.model.coef_

        if return_coeffs:
            return a, b[0]

        if a < 0:
            return f"y = {b[0]} * x {a}"
        elif a == 0:
            return f"y = {b[0]} * x"

        return f"y = {b[0]} * x + {a}"


    def __str__(self):
        return \
            f"""
{f"     SensorPairData : {self.name} : File INFO    ".center(100, "-")}
1.  file path:                          {self.filepath}
2.  file name:                          {self.filename}
3.  file extension:                     {self.extension}
4.  DC Data SheetName:                  {self.__dc_data_sheet_name}
5.  FC Data SheetName:                  {self.__fc_data_sheet_name}
6.  DC Calibration SheetName:           {self.__dc_cal_sheet_name}
7.  FC Calibration SheetName:           {self.__fc_cal_sheet_name}
{"".center(100, '-')}
            """
