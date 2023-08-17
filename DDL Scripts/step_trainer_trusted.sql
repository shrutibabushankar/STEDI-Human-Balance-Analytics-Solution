--stedi_human_balance.step_trainer_trusted
CREATE EXTERNAL TABLE IF NOT EXISTS `stedi_human_balance`.`step_trainer_trusted` (
  `sensorReadingTime` bigint,
  `distanceFromObject` int,
  `serialNumber` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://shruti-lake-house/step_trainer_trusted/'
TBLPROPERTIES ('classification' = 'parquet');