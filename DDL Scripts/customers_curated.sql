--stedi_human_balance.customers_curated

CREATE EXTERNAL TABLE IF NOT EXISTS `stedi_human_balance`.`customers_curated` (
  `serialNumber` string,
  `customerName` string,
  `email` string,
  `phone` string,
  `birthDay` string,
  `registrationDate` bigint,
  `lastUpdateDate` bigint,
  `shareWithResearchAsOfDate` bigint,
  `shareWithPublicAsOfDate` bigint,
  `shareWithFriendsAsOfDate` bigint
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://shruti-lake-house/customers_curated/'
TBLPROPERTIES ('classification' = 'parquet');