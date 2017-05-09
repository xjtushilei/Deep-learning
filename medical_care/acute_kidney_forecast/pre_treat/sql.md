1. 获取 icustay_id 对应的 hadm_id
```postgresql
SELECT 
DISTINCT mimiciii.icustays.icustay_id,
mimiciii.icustays.hadm_id
FROM
mimiciii.icustays ,
pt_score.pt_scores_all
WHERE
mimiciii.icustays.icustay_id = pt_score.pt_scores_all.icustay_id::INTEGER
```
2. 获取所有的 icustay_id
```postgresql
SELECT DISTINCT
pt_scores.icustay_id
FROM
pt_scores
```
3. 获取所有的得病的人的 hadm_id

```postgresql
SELECT 
Count( DISTINCT mimiciii.diagnoses_icd.hadm_id)
FROM
mimiciii.diagnoses_icd
WHERE
mimiciii.diagnoses_icd.icd9_code = '5848' OR
mimiciii.diagnoses_icd.icd9_code = '5849'
```