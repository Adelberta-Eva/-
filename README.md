# 数据仓库学习（sqlserver）以及大数据系统（Spark）
1.数据仓库

这个课程主要围绕数据仓库的核心概念和实际操作展开，通过 SQL Server 平台进行建模与数据处理实践。学习内容包括：

&nbsp;&nbsp;&nbsp;&nbsp;掌握 ETL（Extract-Transform-Load）流程，使用 SQL Server Integration Services (SSIS) 工具进行数据抽取、清洗和加载；   
&nbsp;&nbsp;&nbsp;&nbsp;完成了基本的 多维数据建模，包括事实表和维度表的设计，尝试构建星型模型等；   
&nbsp;&nbsp;&nbsp;&nbsp;学习了数据仓库与业务系统之间的解耦方式，以及如何支持多维度分析查询。  

其实在一开始，第一次进行实验的时候老是会分不清mysql和sqlserver两个软件的一些语法不同以及它们使用的一些场景和功能，简单认识是sqlserver更适合企业场景，可以处理更复杂的事物和报表生成。     
这次实践学习，我了解了SQL Server Integration Services (SSIS) 这一强大的ETL工具并掌握了其基本操作和原理。       
在传统数据仓库中，数据量比较小，计算逻辑相对简单，我们可以直接用ETL工具实现数据转换（T），转换之后再加载到目标库，即（Extract-Transform-Load）,这样简单的步骤就能解决很多问题。  

注意：在实现表数据ETL过程的过程中，数据清洗和转换在ETL过程中十分重要，否则会影响实验结果。以及最后部署的时候，要注意服务器名称是否匹配，默认的服务器名称是：localhost。     

但当数据量变大、业务逻辑变得复杂时，这种模式在以下方面容易暴露瓶颈：   
&nbsp;&nbsp;&nbsp;&nbsp;处理性能问题：转换（T）操作在中间层完成，若数据量庞大，内存和计算资源容易吃紧，严重时导致任务失败；   
&nbsp;&nbsp;&nbsp;&nbsp;可扩展性差：传统 ETL 工具部署在单机或固定服务器上，面对大数据吞吐时缺乏弹性；   
&nbsp;&nbsp;&nbsp;&nbsp;实时性差：ETL 是批处理为主，难以满足分钟级甚至秒级的数据处理需求；     
&nbsp;&nbsp;&nbsp;&nbsp;调度与容错能力弱：处理链条长，某一步出错可能导致全流程失败，重跑代价高。     

2.大数据系统（Spark）   

在这次实践中，我主要使用了 Apache Spark 来处理和分析名数据集，重点掌握了 Spark DataFrame 和 RDD 两大核心概念及其应用。主要实践的内容是学生课程表信息等。  
（1）Spark DataFrame 实践   
&nbsp;&nbsp;&nbsp;&nbsp;初始化：利用 Spark SQL API 读取数据，创建结构化的 DataFrame，明确每列数据类型（schema）。查看 DataFrame 结构，确认数据正确加载。   
&nbsp;&nbsp;&nbsp;&nbsp;实现连接查询操作：将学生表（students）和选课表（courses）通过学生ID字段进行 join，支持多种连接类型（内连接、左连接等），获取每个学生所选课程的信息。   
&nbsp;&nbsp;&nbsp;&nbsp;将连接结果保存为新的 DataFrame，验证查询正确性。  
（2）Spark RDD 实践   
&nbsp;&nbsp;&nbsp;&nbsp;使用 SparkContext 的 sc.textFile() 方法读取英文文本文件，转为弹性分布式数据集（RDD）。   
&nbsp;&nbsp;&nbsp;&nbsp;通过 RDD 的 flatMap、map、reduceByKey 等算子实现：   
&nbsp;&nbsp;&nbsp;&nbsp;统计文本中每个单词的出现次数。统计文本中每个英文字母的出现次数。   
&nbsp;&nbsp;&nbsp;&nbsp;通过这些操作深入理解了 RDD 的不可变性、分区及并行计算特性。    
（3）Spark SQL 学习   
&nbsp;&nbsp;&nbsp;&nbsp;掌握了将 DataFrame 注册为临时视图或表，并使用 Spark SQL 执行复杂的 SQL 查询，包括连接查询。   

