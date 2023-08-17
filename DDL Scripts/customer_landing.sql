--stedi_human_balance.customer_landing

CREATE EXTERNAL TABLE IF NOT EXISTS `stedi_human_balance`.`customer_landing` (
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
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'ignore.malformed.json' = 'FALSE',
  'dots.in.keys' = 'FALSE',
  'case.insensitive' = 'TRUE',
  'mapping' = 'TRUE'
)
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://shruti-lake-house/customer_landing/'
TBLPROPERTIES ('classification' = 'json');