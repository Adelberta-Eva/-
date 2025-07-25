from pyspark.sql import SparkSession

# 创建SparkSession
spark = SparkSession.builder \
    .appName("StudentCourseAnalysis") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# 读取学生数据集的CSV文件并创建临时视图
student_df = spark.read.csv("C:/Users/HONOR/Desktop/大数据/student.csv", header=True, inferSchema=True)
student_df.createOrReplaceTempView("students")

# 读取课程数据集的CSV文件并创建临时视图
course_df = spark.read.csv("C:/Users/HONOR/Desktop/大数据/course.csv", header=True, inferSchema=True)
course_df.createOrReplaceTempView("courses")

# 读取学生选课数据集的CSV文件并创建临时视图
scores_df = spark.read.csv("C:/Users/HONOR/Desktop/大数据/score.csv", header=True, inferSchema=True)
scores_df.createOrReplaceTempView("scores")

# 执行连接查询
join_query ="""
SELECT   
    sc.Sno,  
    stu.Sname, 
    co.Ccredit,
    sc.Score     
FROM   
    scores sc,
    courses co  
JOIN   
    students stu ON sc.Sno = stu.Sno     
"""

# 显示查询结果
join_df = spark.sql(join_query)
join_df.show()
# 停止SparkSession
spark.stop()
