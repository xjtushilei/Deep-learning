#  Acute kidney Forecast

## 数据库信息

### 编码

#### 疾病编码(icd9_code)

需要使用的icd9_code: `5848`、`5849`

具体如下：
- Acute kidney failure NEC 5848
- Acute kidney failure NOS 5849

#### 指标编码（item_id）

**“-”前面是item_id , 后面是数量**

##### lab_events 中的
- [x] 肾小球滤过率估计值（ eGFR , estimated glomerular ﬁltration rate）：item_id：50920 - 63253 条数据，但是好多不全的信息
- [x] 中性白细胞与淋巴细胞比值(NLR, neutrophil-to-lymphocyte ratio)
    - [x] 中性白细胞（Neutrophils）：item_id：51256 - 172131 条数据
    - [x] 淋巴细胞（Lymphocytes）：item_id：51244 - 
    
以上指标引入：`是否正常（flag）`：abnormal不正常，Null正常

##### chart_events 中的
- [x] 凝血酶时间(thrombin time ,TT)：item_id：227469 - 115 条数据
- [x] 血清钾（Serum potassium）：227442 - 165813 条数据
- [x] 尿酸(Uric acid)：225695 - 1656 条数据
- [x] 血清蛋白（Serum albumin）：227456 - 22945 条数据
- [x] 谷草转氨酶(AST): 220587 - 37598 条数据
- [x] 胆固醇（Total cholesterol）：220603 - 1567 条数据
- [x] 性别（Gender）：226228 - 25326 条数据
- [x] 凝血酶原时间(prothrombin time,PT):227465 - 93030 条数据
- [x] 血红蛋白（Hemoglobin）：220228 - 137117 条数据

以上指标可引入：`是否有警告（warning）`：1警告，0正常

##### 其他
- [x] 是否感染（Pulmonary infection）一些列感染

- [x] 年龄（Age）在 `patients` 表中有出生日期，减去住院日期 `admissions` 中的 `admittime` 
- [x] 当前体重:226512(病人入院体重)，item_id：762、763、2765


### 查询总结
- 诊断结果表（diagnoses_icd）中病人总数：`58976`
- 诊断结果表（diagnoses_icd）中肾衰竭个数：`9173`
- prescriptions表中总icustay_id数：`50216`
- prescriptions表中总hadm_id数：`52151`
- prescription有多少条记录：`4156450`
- icu_score表中的icu_id个数： `52955`
- icu_score表有肾衰竭的个数： `10112` 个， 占比: `19.10%` (可能同一个病人多次进入icu)


