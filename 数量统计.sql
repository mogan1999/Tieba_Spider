SELECT 
  SUM(comment_count) AS total_comment_count, 
  SUM(post_count) AS total_post_count, 
  SUM(thread_count) AS total_thread_count 
FROM 
(
  SELECT 
    table_schema, 
    SUM(CASE WHEN table_name = 'comment' THEN table_rows ELSE 0 END) AS comment_count, 
    SUM(CASE WHEN table_name = 'post' THEN table_rows ELSE 0 END) AS post_count, 
    SUM(CASE WHEN table_name = 'thread' THEN table_rows ELSE 0 END) AS thread_count 
  FROM 
    information_schema.tables 
  WHERE 
    table_schema LIKE '%data' 
    AND table_name IN ('comment', 'post', 'thread') 
  GROUP BY 
    table_schema, 
    table_name
) AS t;
