# coding: utf-8
import unittest
import os
from time import sleep
from BaseOperate.run import run_testcaseYaml
from BaseOperate.getDriver import mdriver
from BaseOperate.Excel import Report


class Settings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = mdriver("btcall")
        sleep(2)
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        app_yamlFolder = PATH('../common/testcaseyaml/btcall/')
        # app_yamlFolder = os.path.join(os.getcwd(), 'common/testcaseYaml/btcall/')
        cls.app_yamlFolder = app_yamlFolder
        cls.tag = "btcall"
        print("btcall Start")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("btcall End")

    def test_btcall(self):
        yamlFile_list = os.listdir(self.app_yamlFolder)
        yamlFile_list.sort()
        # print(yamlFile_list)
        for file in yamlFile_list:
            yamlFile = os.path.join(self.app_yamlFolder, file)
            print(yamlFile)
            actualResult, resultOutput, testConclusion = run_testcaseYaml(self.driver, yamlFile).run_testcase(self.tag)
            Report().worksheet2_write_data(yamlFile, actualResult, resultOutput, testConclusion)


if __name__ == "__main__":
    unittest.main()
