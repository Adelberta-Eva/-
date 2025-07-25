from pyspark.sql import SparkSession

# 初始化SparkSession
spark = SparkSession.builder.appName("StudentCourseExample").getOrCreate()

# 读取CSV文件（确保文件路径和文件名正确，且CSV格式无误）
students_df = spark.read.csv("C:/Users/HONOR/Desktop/大数据/student.csv", header=True, inferSchema=True)
students_df.createOrReplaceTempView("students")
courses_df = spark.read.csv("C:/Users/HONOR/Desktop/大数据/course.csv", header=True, inferSchema=True)
courses_df.createOrReplaceTempView("courses")
scores_df = spark.read.csv("C:/Users/HONOR/Desktop/大数据/score.csv", header=True, inferSchema=True)
scores_df.createOrReplaceTempView("scores")

# 显示DataFrame内容
students_df.show()
courses_df.show()
scores_df.show()

# 执行连接查询
join_query = """  
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
join_df = spark.sql(join_query)
# 显示查询结果
join_df.show()