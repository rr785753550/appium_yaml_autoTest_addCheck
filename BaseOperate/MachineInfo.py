import os


class machine:
    def get_machineInfo(self, infoName):
        cmd = "adb shell getprop %s" % infoName
        cmdResult = os.popen(cmd).readlines()
        machineInfo = cmdResult[0][0: -1]
        return machineInfo

    # 机器型号
    def get_productModel(self):
        infoName = "ro.product.model"
        productModel = self.get_machineInfo(infoName)
        return productModel

    # 产品名称
    def get_productName(self):
        infoName = "ro.yunovo.prj.name"
        productModel = self.get_machineInfo(infoName)
        return productModel

    # 软件版本
    def get_softwareVersion(self):
        infoName = "ro.build.display.id"
        softwareVersion = self.get_machineInfo(infoName)
        return softwareVersion


# print(machine().get_productModel())
# print(machine().get_productName())
# print(machine().get_softwareVersion())
