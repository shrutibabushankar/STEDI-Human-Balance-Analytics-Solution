--select * from stedi_human_balance.machine_learning_curated limit 10;

CREATE EXTERNAL TABLE IF NOT EXISTS `stedi_human_balance`.`machine_learning_curated` (
  `user` string,
  `timeStamp` bigint,
  `x` double,
  `y` double,
  `z` double,
  `sensorReadingTime` bigint,
  `distanceFromObject` int,
  `serialNumber` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://shruti-lake-house/machine_learning_curated/'
TBLPROPERTIES ('classification' = 'parquet');