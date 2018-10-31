1、common -> deviceYaml （存在device信息，app信息）

    1.1.启动设备中某个应用时，BaseOperate -> getDriver.py来启动
    1.2.testcase中调用getDriver.py时需传入appName，通过appName才可确定当前启用的是哪个应用，appName需与deviceYaml中的app名称保存一致，
        否则无法调起
    1.3.如需增加新的app信息，可直接在deviceYaml中添加，具体添加规则需参考已添加的应用


2、BaseOperate - > testcaseYaml

    2.1.yaml写入文件的格式已固定，请参考已写好的格式
        testcase1:
          step1:
            element_info:
            element_type:
            element_operate:
            sleep_time:
            operate_times:
            operate_details:
          check1:
            check_content:
            check_method:
            expect_value:
            pass_output:
            fail_output:

    2.2.yaml文件：key值中含有step的内容
        element_info：必选项，定位元素的详细信息
        element_type：必选项，操作控件属性id、xpath、text、class、position代表info为一个坐标点
        element_operate: 必选项，控件操作 click、send_keys、back、swipe_up、swipe_down
        operate_times: 必选项，操作的次数（如，操作为click、back、swipe_up/down时必写）
        sleep_time: 等待时间
        operate_details： 操作详情

        send_content：send_keys时填写的内容
                    -非必选项，只需在operate_type为send_keys时使用

    2.3. yaml文件： key值中含有check的内容
        check_content:  表示需要判断的内容
                # check_method:  判断的方法（属性为：check_logcatContent、check_sysContent、elementExist）
        expect_value:   期待的结果
        pass_output:    如果pass输出内容为XXX
        fail_output:    如果fail输出内容为XXX
     2.4.注：
        操作时若必选项无任何信息输入时，此必选项key的value值可为空，比如element_operate为back时会会用



3、BaseOperate文件夹
    3.1. appiumServer.py 封装有启动appium和关闭appium服务操作
    3.2 check_operatesult_Method.py 封装操作控件，判断是否成功的方法
    3.3 elementMethod.py 封装定位、滑动、seekBar的基本方法
    3.4. elementOperate.py 检查对元素执行的操作
    3.5. get_testcaseyaml_info.py 读取testcaseYaml中yaml所写的各功能控件信息
    3.6 getDriver.py 启动driver
    3.7. grabLog.py 抓取logcat
    3.8. run_testcaseYaml.py 运行testcase的yaml文件

