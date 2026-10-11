CN
程序设计报告：植物登记系统 (Plant Registration System)

一、 项目概述
项目名称：
	植物登记系统（Plant Registration System）

开发环境
	编程语言：Python 3.x
	开发工具：Visual Studio Code (VS Code)
	版本控制：Git / GitHub

二、 需求分析
本系统主要满足以下功能需求：
	数据录入：能够交互式地获取用户输入的植物名称、种植数量、单价及健康棵数。
	数据类型校验：确保数量和棵数为整数，单价支持浮点数（小数）。
	自动计算：
    		产值计算：根据单价×健康棵数。计算总经济价值。
    		健康率计算：根据健康棵数/种植数量×100%。评估种植质量。
	结果展示：清晰地向用户反馈计算结果。

三、 系统设计
核心逻辑流程
	程序采用线性顺序结构，主要包含三个部分：输入、处理、输出

	输入：使用 input()函数结合 f-string 格式化提示语，收集四项数据。
	处理：利用转换函数 int()和 float()对数据进行格式转换，并进行数学运算。
	输出：打印计算后的产值和健康率。

变量定义
	name		植物品种名称
	count		种植总数量
	unit_price		市场单价（元/斤）
	health_count	存活/健康的植株数量
	total_value	计算得出的总产值
	health_rate	计算得出的健康百分比

四、 核心代码实现
以下是系统的关键代码逻辑片段：

rint("=== 欢迎使用植物信息记录系统 ===")
name=input("请输入植物的品种名称：")    #用户输入品种名称(字符串)    #input默认键入string值，不能进行数学运算
total_count=int(input(f"请输入{name}的种植数量(请键入整数):"))    #接收用户输入的种植数量(整数)    #在input前键入int转换变量type
unit_price=float(input(f"请输入{name}的单价(元/斤，可键入小数):"))    #用户输入单价(浮点数)
health_count=int(input(f"请输入{name}的健康棵数(请键入整数):"))    #用户输入健康棵数(整数)
is_healthy=health_count>(total_count/2)    #判断是否健康(布尔值)    #判断标准为健康数是否大于总数一半    #比较自动变为Bool
total_value=unit_price*health_count    #总价=单价×健康棵数   
health_rate=health_count/total_count*100    #健康率=健康棵数/种植数量×100%
diseased_count=total_count-health_count    #病变棵数=种植数量-健康棵数

五、 测试与运行
在开发过程中，对程序进行了多组数据测试：
正常测试：输入整数数量和带小数的单价，程序能准确计算出产值。
遇到的问题：input默认输入的是字符串，不能进行数学运算，会发生报错
异常处理：通过 int() 和 float() 进行格式转换，防止了字符串直接参与数学运算导致的错误。

六、 总结
本次实验成功实现了一个基础的植物信息登记模块。通过 Python 的交互式输入输出功能，实现了数据的采集与自动化处理。


EN
Program Design Report: Plant Registration System

I. Project Overview
Project Name
 Plant Registration System

development environment
 Programming language: Python 3.x
 Development Tools: Visual Studio Code (VS Code)
 Version Control: Git / GitHub

II. Requirements Analysis
This system primarily meets the following functional requirements:
 Data Entry: Capable of interactively capturing user input for plant names, planting quantities, unit prices, and healthy plant counts.
 Data type validation: Ensure that quantity and tree count are integers, while unit price supports floating-point numbers (decimals).
 Automatic calculation:
   Output value calculation: Total economic value is calculated by multiplying the unit price by the number of healthy trees.
   Health Rate Calculation: Based on healthy plants / total planted × 100%. Assessing planting quality.
 Result Display: Clearly present the calculation results to the user.

III. System Design
Core logic flow
 The program adopts a linear sequential structure and primarily consists of three parts: input, processing, and output

 Use the input() function in combination with f-string formatted prompts to collect four pieces of data.
 Processing: Use the conversion functions int() and float() to transform data formats and perform mathematical operations.
 Print the calculated output value and health rate.

variable definition
 name    Plant Variety Name
 count		Total planting quantity
 unit_price		Market unit price (Yuan/jin)
 health_count  Number of surviving/healthy plants
 total_value	the calculated total output value
 health_rate	Computed health percentage
 
IV. Core Code Implementation
Here is a key code logic snippet from the system:

rint("=== 欢迎使用植物信息记录系统 ===")
name=input("请输入植物的品种名称：")    #用户输入品种名称(字符串)    #input默认键入string值，不能进行数学运算
total_count=int(input(f"请输入{name}的种植数量(请键入整数):"))    #接收用户输入的种植数量(整数)    #在input前键入int转换变量type
unit_price=float(input(f"请输入{name}的单价(元/斤，可键入小数):"))    #用户输入单价(浮点数)
health_count=int(input(f"请输入{name}的健康棵数(请键入整数):"))    #用户输入健康棵数(整数)
is_healthy=health_count>(total_count/2)    #判断是否健康(布尔值)    #判断标准为健康数是否大于总数一半    #比较自动变为Bool
total_value=unit_price*health_count    #总价=单价×健康棵数   
health_rate=health_count/total_count*100    #健康率=健康棵数/种植数量×100%
diseased_count=total_count-health_count    #病变棵数=种植数量-健康棵数

V. Testing and Operation
During the development process, the program underwent multiple sets of data testing
Normal testing: Enter the quantity as an integer and the unit price with decimals, and the program accurately calculates the output value.
The issue encountered: The default input is a string, which cannot perform mathematical operations and will result in an error
Exception Handling: The conversion between string and numerical types via int() and float() prevents errors arising from direct mathematical operations on strings.

VI. Summary
This experiment successfully implemented a basic plant information registration module. Through Python's interactive input and output functions, data collection and automated processing were achieved.
