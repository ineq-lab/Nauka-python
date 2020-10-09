# -*- coding: utf8 -*-

print("Przekątna twojego Telewizora w calach?")
cal = float(input())
cm_to_cal = cal*2.54
m_to_cal = cal*0.0254
km_to_cal = cal*2.54E-5
print("Przekątna w cm to:{:.2f}cm w metrach:{:.3f}m a w kilometrach:{:.6f}km".format(cm_to_cal, m_to_cal, km_to_cal))
