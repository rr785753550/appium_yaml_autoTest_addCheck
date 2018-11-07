# coding: utf-8
import unittest
import os
from time import sleep
from BaseOperate.run import run_testcaseYaml
from BaseOperate.getDriver import mdriver
from BaseOperate.Excel import Report


class SendFm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = mdriver("fmsend")
        sleep(5)
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        app_yamlFolder = PATH('../common/testcaseyaml/fmsend/')
        # app_yamlFolder = os.path.join(os.getcwd(), 'common/testcaseYaml/fmsend/')
        cls.app_yamlFolder = app_yamlFolder
        cls.tag = "fmsend"
        print("fmsend Start")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("fmsend End")

    def test_statusBar(self):
        yamlFile_list = os.listdir(self.app_yamlFolder)
        yamlFile_list.sort()
        # print(yamlFile_list)
        for file in yamlFile_list:
            yamlFile = os.path.join(self.app_yamlFolder, file)
            print(yamlFile)
            result_tuple = run_testcaseYaml(self.driver, yamlFile).run_testcase(self.tag)
            print(result_tuple)
            Report().worksheet2_write_data(yamlFile, result_tuple)


if __name__ == "__main__":
    unittest.main()
