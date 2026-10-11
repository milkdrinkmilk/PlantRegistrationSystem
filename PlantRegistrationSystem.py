#Time:2026.10.11
#Author:InS_Liu
#File:PlantRegistrationSystem.py

print("=== 欢迎使用植物信息记录系统 ===")
name=input("请输入植物的品种名称：")    #用户输入品种名称(字符串)    #input默认键入string值，不能进行数学运算
total_count=int(input(f"请输入{name}的种植数量(请键入整数):"))    #接收用户输入的种植数量(整数)    #在input前键入int转换变量type
unit_price=float(input(f"请输入{name}的单价(元/斤，可键入小数):"))    #用户输入单价(浮点数)
health_count=int(input(f"请输入{name}的健康棵数(请键入整数):"))    #用户输入健康棵数(整数)
is_healthy=health_count>(total_count/2)    #判断是否健康(布尔值)    #判断标准为健康数是否大于总数一半    #比较自动变为Bool
total_value=unit_price*health_count    #总价=单价×健康棵数   
health_rate=health_count/total_count*100    #健康率=健康棵数/种植数量×100%
diseased_count=total_count-health_count    #病变棵数=种植数量-健康棵数

#扩展内容,添加更多计算指标
estimated_yield = round(health_count*1.98, 1)    #预估产量，假设每棵健康植物产出 1.98 斤     #下面使用round()以控制小数位数，所以下方变量是float浮点形式
#计算时直接使用变量即可，这里在输出格式中控制
total_value_rounded = round(total_value, 2)
health_rate_rounded = round(health_rate, 2)
#下方使用print()和f-string格式化输出完整的植物信息报告
print("\n" + "="*35)
print(f"【{name}】植物信息报告")
print("="*35)
print(f"种植数量：{total_count} 棵")
print(f"单价：    {unit_price} 元/斤")
print(f"健康棵数：{health_count} 棵")
print(f"病变棵数：{diseased_count} 棵")
print(f"是否健康：{'是 (状态良好)'if is_healthy else'否 (需注意病害)'}")     #这里使用了if用于判断情况，其主要作用在一当is_healthy变量布尔值不同时输出不同内容
print("-" * 35)    #这里起到分隔作用
print(f"总价值：  {total_value_rounded} 元")
print(f"健康率：  {health_rate_rounded}%")
print(f"预估产量：{estimated_yield} 斤")
print("="*35)
#这里可以使用\g换行，减少行数，作者太懒了直接复制了，需要可以等下次