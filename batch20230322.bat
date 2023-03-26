call activate tieba
cd /d S:\pachong\Tieba_Spider
python modify_config.py 深圳大学&&scrapy run 深圳大学 深圳大学data -p 1 8 
timeout /t 4719
python modify_config.py 广东警官学院&&scrapy run 广东警官学院 广东警官学院data -p 1 8 
timeout /t 4719
python modify_config.py 广东科技学院&&scrapy run 广东科技学院 广东科技学院data -p 1 8 
timeout /t 4719
python modify_config.py 广东理工学院&&scrapy run 广东理工学院 广东理工学院data -p 1 8 
timeout /t 4719
python modify_config.py 东莞城市学院&&scrapy run 东莞城市学院 东莞城市学院data -p 1 8 
timeout /t 4719