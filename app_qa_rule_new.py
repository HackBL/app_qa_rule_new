def getAnswerAfterRule(final_display, fieldValue, final_unitRule, final_unit, final_connect):

    sub = ''

    # 处理单位换算问题
    if final_unitRule is None:
        pass
    else:
        if final_unitRule == '毫米到厘米':
            fieldValue /= 10
        elif final_unitRule == '克到千克' or final_unitRule == '毫米到米' or final_unitRule == '立方毫米到立方厘米':
            fieldValue /= 1000
        elif final_unitRule == '立方毫米到升':
            fieldValue /= 1000000
        elif final_unitRule == '立方毫米到立方米':
            fieldValue /= 1000000000
        else:
            pass

    # add unit:
    final_unit_value = ''
    try:
        if final_unit is not None:
            final_unit_value = final_unit
        else:
            final_unit_value = ''

    except:
        pass

    if final_display == '能效等级':
        sub = '的' + final_display + '是' + str(fieldValue) + final_unit_value + '的,符合国家' + str(fieldValue) + '能耗，非常省电'
    elif final_display == '显示屏类型':
        sub = '的显示屏类型是' + str(fieldValue) + final_display

    else:


        if final_connect == 'is':

            # 功率是XXX 的
            sub = final_display + '是' + str(fieldValue) + final_unit_value + '的'
        elif final_connect == 'is_direct':
            sub = '是' + str(fieldValue) + '的'


        elif final_connect == 'is_support':
            support = None
            if fieldValue == '是':
                support = '支持'
            elif fieldValue == '否':
                support = '不支持'

            else:
                support

            if support is None:
                pass
            else:
                sub = support + final_display

        elif final_connect == 'is_support_bit':
            if fieldValue == 1:
                sub = final_display
            elif fieldValue == 0:
                sub = '不' + final_display
            else:
                pass

        elif final_connect == 'is_support_bit2':
            if fieldValue == 1:
                sub = '是' + final_display
            elif fieldValue == 0:
                sub = '不是' + final_display
            else:
                pass

        elif final_connect == 'is_support_yesno':
            if fieldValue == '是':
                sub = '有' + final_display
            elif fieldValue == '否':
                sub = '无' + final_display
            else:
                pass

        elif final_connect == 'is_support_yesno2':
            if fieldValue == '是':
                sub = final_display
            elif fieldValue == '否':
                sub = '不' + final_display
            else:
                pass


        elif final_connect == 'is_support_yesno3':
            if fieldValue is None:
                pass
            elif fieldValue == '有':
                sub = '有' + final_display
            else:
                pass


        elif final_connect == 'include':
            sub = final_display + '有' + str(fieldValue)
        elif final_connect == 'include2':
            sub = final_display + '包含' + str(fieldValue)

        elif final_connect == 'is_value_header':
            sub = str(fieldValue) + final_display
        elif final_connect == 'noword':
            sub = final_display + str(fieldValue) + final_unit_value


    return sub.replace(' ','').replace("\t",'').replace("\r",'').replace("\n",'').strip("\n")

