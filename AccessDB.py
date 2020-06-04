import MySQLdb #pip install mysqlclient
import pandas as pd
import numpy as np
import xlrd
import helper
import app_qa_rule_new

config_main = {'sql_conn': {'host': '***',
                            'user': '***',
                            'passwd': '***!',
                            'charset': 'utf8'}}

db = 'techweek'

conn = MySQLdb.connect(host=config_main['sql_conn']['host'],
                       user=config_main['sql_conn']['user'],
                       passwd=config_main['sql_conn']['passwd'],
                       charset=config_main['sql_conn']['charset']) 

catAir = '30'
catRef = '1'
#######################

bingxiang = 'category_refrigerator'
bingxiangSql = 'SELECT * FROM ' + db + '.vb_' + bingxiang
bingxiangDF = pd.read_sql(bingxiangSql, conn)
#######################

kongtiao = 'category_air_conditioning'
kongtiaoSql = 'SELECT * FROM ' + db + '.vb_' + kongtiao
kongtiaoDF = pd.read_sql(kongtiaoSql, conn)
#######################

final = pd.DataFrame()


def generator(catId, category):
	finalDF = pd.DataFrame()

	ruleTablename = 'web_field_map_new_add_rule'
	ruleSql = 'SELECT * FROM ' + db + '.' + ruleTablename + ' where categoryId = ' + catId
	ruleDF = pd.read_sql(ruleSql, conn)

	tableName = ''

	if catId == '1':
		tableName = 'category_refrigerator'
	elif catId == '30':
		tableName = 'category_air_conditioning'

	for i in range(len(ruleDF.attr_name)):
		if ruleDF.attr_name[i] in category.columns.tolist():
            # Tags
			categoryName = ruleDF.category[i]

			final_display = ruleDF.attr_display[i]
			final_unitRule = ruleDF.rule[i]
			final_unit = ruleDF.unit[i]
			final_connect = ruleDF.connect_word[i]

			attrName = ruleDF.attr_name[i]
			colList = category[attrName].drop_duplicates().dropna().reset_index(drop=True)

			for j in range(len(colList)):
				fieldValue = colList[j]
				answer = app_qa_rule_new.getAnswerAfterRule(final_display, fieldValue, final_unitRule, final_unit, final_connect)

				dfTemp = pd.DataFrame([[catId,      # Create DF for each row datas 
	                                    categoryName,
	                                    tableName,
	                                    attrName,
	                                    final_display,
	                                    final_unitRule,
	                                    final_unit,
	                                    final_connect,
	                                    answer,
	                                    fieldValue]], 

	                                    columns=['categoryId',   
		                                          'category',
		                                          'tableName',
		                                          'attr_name',
		                                          'attr_display',
		                                          'rule',
		                                          'unit',
		                                          'connect_word',
		                                          'answer',
		                                          'value'])

				finalDF = finalDF.append(dfTemp)  # Insert each row datas into DF
	return finalDF


ref = generator(catRef, bingxiangDF)
air = generator(catAir, kongtiaoDF)
final = final.append(ref).append(air)


# Export DF to csv
final.to_csv('NewData.csv', index = False, encoding = 'utf-8-sig')

# print(final.to_string())







