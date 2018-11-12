# coding: utf-8
import unittest
import os
from time import sleep
from BaseOperate.run import runYaml
from BaseOperate.getDriver import mdriver
from BaseOperate.Excel import Report


class Launcher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = mdriver("launcher")
        sleep(5)
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        app_yamlFolder = PATH('../common/testcaseyaml/launcher/')
        # app_yamlFolder = os.path.join(os.getcwd(), 'common/testcaseYaml/launcher/')
        cls.app_yamlFolder = app_yamlFolder
        cls.tag = "launcher"
        print("launcher Start")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("launcher End")

    def test_launcher(self):
        app_Folder = os.listdir(self.app_yamlFolder)
        # print(app_Folder)
        for folder in app_Folder:
            appsFolder = os.path.join(self.app_yamlFolder, folder)
            appsFolder_list = os.listdir(appsFolder)
            appsFolder_list.sort()
            # print(appsFolder_list)
            for file in appsFolder_list:
                try:
                    yamlFile = os.path.join(appsFolder, file)
                    print(yamlFile)
                    try:
                        runYaml(yamlFile).run_testcase(self.driver, self.tag)
                    except:
                        pass
                finally:
                    result_tuple = runYaml(yamlFile).get_run_results()
                    print(result_tuple)
                    Report().worksheet2_write_data(yamlFile, result_tuple)


if __name__ == "__main__":
    unittest.main()
