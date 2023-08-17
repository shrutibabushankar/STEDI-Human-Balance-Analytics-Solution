--stedi_human_balance.accelerometer_trusted;

CREATE EXTERNAL TABLE IF NOT EXISTS `stedi_human_balance`.`accelerometer_trusted` (
  `user` string,
  `timeStamp` bigint,
  `x` double,
  `y` double,
  `z` double
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://shruti-lake-house/accelerometer_trusted/'
TBLPROPERTIES ('classification' = 'parquet');