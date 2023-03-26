##下面为单独的schema统计##

#post分析#
SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(post.content, ' ', numbers.n), ' ', -1) AS word, COUNT(*) AS count
FROM (
    SELECT 1 n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL
    SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10
) numbers 
INNER JOIN post ON CHAR_LENGTH(post.content) - CHAR_LENGTH(REPLACE(post.content, ' ', '')) >= numbers.n - 1
WHERE SUBSTRING_INDEX(SUBSTRING_INDEX(post.content, ' ', numbers.n), ' ', -1) 
REGEXP '^(?!.*win|.*lose|.*http|.*专|.*好|.*加油|.*打搅|.*好似|.*已阅|.*原神|.*女留id男自强|.*6|.*老东西|.*你说得对|.*单机|.*新年快乐).+$'
AND LENGTH(SUBSTRING_INDEX(SUBSTRING_INDEX(post.content, ' ', numbers.n), ' ', -1)) >= 8
GROUP BY SUBSTRING_INDEX(SUBSTRING_INDEX(post.content, ' ', numbers.n), ' ', -1)
ORDER BY count DESC
LIMIT 50;

#thread#分析
SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(title, ' ', n), ' ', -1) AS word, COUNT(*) AS frequency
FROM thread
INNER JOIN (
    SELECT 1 + units.i + tens.i * 10 AS n
    FROM (SELECT 0 i UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9) units
    CROSS JOIN (SELECT 0 i UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9) tens
    ORDER BY n
) numbers
ON CHAR_LENGTH(title) - CHAR_LENGTH(REPLACE(title, ' ', '')) >= n - 1
WHERE SUBSTRING_INDEX(SUBSTRING_INDEX(title, ' ', n), ' ', -1) NOT IN ('win', 'lose')
GROUP BY word
ORDER BY frequency DESC
LIMIT 10;

##下面为所有的schema整合统计##

#post分析#
SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(post.content, ' ', numbers.n), ' ', -1) AS word, COUNT(*) AS count
FROM (
    SELECT 1 n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL
    SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10
) numbers 
INNER JOIN information_schema.tables t
ON t.TABLE_NAME='post' AND t.TABLE_SCHEMA REGEXP '.*data$'
INNER JOIN post ON CHAR_LENGTH(post.content) - CHAR_LENGTH(REPLACE(post.content, ' ', '')) >= numbers.n - 1
WHERE SUBSTRING_INDEX(SUBSTRING_INDEX(post.content, ' ', numbers.n), ' ', -1) 
REGEXP '^(?!.*win|.*lose|.*http|.*专|.*好|.*加油|.*打搅|.*好似|.*已阅|.*原神|.*女留id男自强|.*6|.*老东西|.*你说得对|.*单机|.*新年快乐).+$'
AND LENGTH(SUBSTRING_INDEX(SUBSTRING_INDEX(post.content, ' ', numbers.n), ' ', -1)) >= 8
GROUP BY SUBSTRING_INDEX(SUBSTRING_INDEX(post.content, ' ', numbers.n), ' ', -1)
ORDER BY count DESC
LIMIT 50;

#thread分析#


#过滤thread#
ALTER TABLE post DROP FOREIGN KEY post_ibfk_1;
DELETE FROM `thread` WHERE `title` REGEXP 'win|lose|赢|输' AND `id` IN 
(SELECT `thread_id` FROM `post` WHERE `id` IN 
(SELECT `post_id` FROM `comment` WHERE `post_id` IS NOT NULL));

#过滤post#
DELETE FROM post
WHERE content REGEXP '打胶|打搅|+3';

#过滤所有post#
SELECT CONCAT('DELETE FROM `', TABLE_SCHEMA, '`.`post` WHERE `content` REGEXP \'郊县|打搅|打胶|原神|好似|已阅|老东西|你说得对|你说的对\';') AS query
FROM information_schema.tables
WHERE TABLE_SCHEMA LIKE '%data';

#过滤所有title#
SELECT CONCAT('DELETE FROM `', TABLE_SCHEMA, '`.`thread` WHERE `title` REGEXP \'打搅|打胶\';') AS query
FROM information_schema.tables
WHERE TABLE_SCHEMA LIKE '%data';