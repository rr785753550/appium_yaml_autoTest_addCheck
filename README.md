1、common -> deviceYaml （存在device信息，app信息）

    1.1.启动设备中某个应用时，BaseOperate -> getDriver.py来启动
    1.2.testcase中调用getDriver.py时需传入appName，通过appName才可确定当前启用的是哪个应用，appName需与deviceYaml中的app名称保存一致，
        否则无法调起
    1.3.如需增加新的app信息，可直接在deviceYaml中添加，具体添加规则需参考已添加的应用

2、common - > testcaseYaml

    2.1.yaml写入文件的格式已固定，请参考已写好的格式

        testinfo:
            title:
            condition:
        testcase:
          step1:
            element_info:
            element_type:
            element_operate:
            sleep_time:
            operate_times:
            operate_details:
        check:
           result1:
             check_content: fragmentName
             expect_value:
        output:
            pass_output:
            fail_output:
    2.2.yaml文件：testcase中step的内容

        element_info：   必选项，定位元素的详细信息
        element_type：   必选项，操作控件属性id、xpath、text、class、position代表info为一个坐标点、
        element_operate: 必选项，控件操作 click、send_keys、back、swipe_up、swipe_down、swipe_left、swipe_right、swipe_position、tap
        operate_times: 必选项，操作的次数（如，操作为click、back、swipe_up/down时必写）
        sleep_time:     等待时间
        operate_details： 操作详情

        send_content：send_keys时填写的内容
                    -非必选项，只需在operate_type为send_keys时使用
    2.3. yaml文件： check中的result内容

        check_content:  表示需要判断的内容
        expect_value:   期待的结果
    2.4. yaml文件： output中的内容

        pass_output:    如果pass输出内容为XXX
        fail_output:    如果fail输出内容为XXX
     2.4.注：

        操作时若必选项无任何信息输入时，此必选项key的value值可为空，比如element_operate为back时会会用

3、common -> emailReceiver：

    ---用为存在收件人地址

4、BaseOperate文件夹

    3.1. appiumServer.py 封装有启动appium和关闭appium服务操作
    3.2 check_operateResult_bylog.py 分析抓取的logcat信息，通过check_conten将log中对应的value值放至actualValue_list
    3.3 elementMethod.py 封装定位、滑动、seekBar的基本方法
    3.4. elementOperate.py 检查对元素执行的操作
    3.5. get_testcaseyaml_info.py 读取testcaseYaml中yaml所写的各功能控件信息
    3.6 getDriver.py 启动driver
    3.7. grabLog.py 抓取logcat
    3.8. run.py 运行testcase的yaml文件
    3.9. Excel.py 将yaml文件中操作步骤、检查点、期望结果，run中的实际结果、输出以及测试结论放至excel表格中，作为测试报告发送
    3.10. sendEmail.py发送测试报告

5、results文件夹：

    4.1. appiumlog：用来存放appium的运行log
    4.2. logcat：用来存在测试过程中抓取的logcat
    4.3. report：用来生成测试报告
    4.4. screenshot： 用来存放错误截图

6. testcase文件夹：
    
    存放所有应用的测试用例，会通过调用commom/testcaseyaml中对应app的配置文件来执行，若一个app某个功能的对应控件或位置有变化，可直接通过改变testcaseyaml中对应的功能操作步骤即可

7.main.py：

    主函数，运行testcase文件夹中所有的test

