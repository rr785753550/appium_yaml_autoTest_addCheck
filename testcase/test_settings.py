# coding: utf-8
import unittest
import os
from time import sleep
from BaseOperate.run import run_testcaseYaml
from BaseOperate.getDriver import mdriver
from BaseOperate.grabLog import kill_logcat
from BaseOperate.Excel import Report


class Settings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = mdriver("settings")
        sleep(2)
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        app_yamlFolder = PATH('../common/testcaseyaml/settings/')
        # app_yamlFolder = os.path.join(os.getcwd(), 'common/testcaseYaml/settings/')
        cls.app_yamlFolder = app_yamlFolder
        cls.tag = "YOcSettings"
        print("settings Start")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("settings End")

    def test_settings(self):
        yamlFile_list = os.listdir(self.app_yamlFolder)
        yamlFile_list.sort()
        # print(yamlFile_list)
        for file in yamlFile_list:
            try:
                yamlFile = os.path.join(self.app_yamlFolder, file)
                print(yamlFile)
                try:
                    run_testcaseYaml(yamlFile).run_testcase(self.driver, self.tag)
                except:
                    pass
            finally:
                result_tuple = run_testcaseYaml(yamlFile).get_run_results()
                print(result_tuple)
                Report().worksheet2_write_data(yamlFile, result_tuple)

    # def test_01_wifi(self):
    #     yamlFile = os.path.join(self.app_yamlFolder, '01_wifi.yaml')
    #     try:
    #         run_testcaseYaml(yamlFile).run_testcase(self.driver, self.tag)
    #     finally:
    #         result_tuple = run_testcaseYaml(yamlFile).get_run_results()
    #         print(result_tuple)
    #         Report().worksheet2_write_data(yamlFile, result_tuple)
    #
    # def test_06_drivingCollision(self):
    #     yamlFile = os.path.join(self.app_yamlFolder, '06_driving_collision.yaml')
    #     try:
    #         run_testcaseYaml(yamlFile).run_testcase(self.driver, self.tag)
    #     finally:
    #         result_tuple = run_testcaseYaml(yamlFile).get_run_results()
    #         print(result_tuple)
    #         Report().worksheet2_write_data(yamlFile, result_tuple)


if __name__ == "__main__":
    unittest.main()
