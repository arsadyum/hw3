
# import mysql.connector
import pymongo
def ha3(univDB):
#-------------------------------------------------------------------------------
#   Part 1:
#   Create MySQL DB, create tables and populate them from univDV as per
#   HA3 instructions.
#   Fill in below:


#     mydb = mysql.connector.connect(
#   host="localhost",
#   user="temp",
#   password="",
#   autocommit = True
# )
#
#
#     mydb.cursor().execute("drop database if exists udb;")
#     mydb.cursor().execute("create database udb;")
#     mydb.cursor().execute("use udb;")
#     mydb.cursor().execute("""CREATE TABLE `student` (
#         `ssn` INT(11) NOT NULL,
#         `name` VARCHAR(45) NOT NULL,
#         `major` VARCHAR(45) NOT NULL,
#         `status` VARCHAR(45) NOT NULL,
#         PRIMARY KEY (`ssn`))""");
#
#     for row in univDB["tables"]["student"]:
#             mydb.cursor().execute("""INSERT INTO student VALUES(%d,"%s","%s","%s");""" % (row["ssn"],row["name"],row["major"],row["status"]));
#     mydb.cursor().execute("""CREATE TABLE `class` (
#         `class` INT(11) NOT NULL,
#         `dcode` VARCHAR(14) NOT NULL,
#         `cno` INT(11) NOT NULL,
#         `instr` INT(11) NOT NULL)""");
#     for row in univDB["tables"]["class"]:
#         #Insert into student (`ssn`,`name`,`major`,`status`) values (833,"John", "CS", "active")
#         mydb.cursor().execute("""INSERT INTO class VALUES(%d,"%s","%d","%d");""" % (row["class"],row["dcode"],row["cno"],row["instr"]));

#-------------------------------------------------------------------------------
#   Part 2:
#   Create mongoDB, and populate it with data from univDB as per HA3 instuctions
#   Fill in below:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["UnivDB"]
    for key,value in univDB["tables"].items():
        if len(value)>0:
            mydb[key].insert_many(value)
    # print([a for a in mydb["course"].find({"dcode":"CS"},{"_id":0})])
#-------------------------------------------------------------------------------
# Part 3: QUERIES
# For each of the following queries, implemennt SQL and Mongo subsqueries first.
# The SQL and Mongo subqueries must extract the MINIMAL amount of data necessary
# from MySQL DB and MongoDB, respectively.
# Choose their order, i.e., SQL subquery first vs. Mongo subquery first, as the
# result from the first subquery may be used to minimize the amount of data
# extracted in the second.
# Add commands (assignments etc) if needed.
# The overall Python query can only use SQL and Mongo subqueries (not allowed
# to use univDB directly)
#-------------------------------------------------------------------------------
# Auxiliary functions
# You can access MySQL DB and MongoDB, but not univDB directly
#-------------------------------------------------------------------------------
    def studentGotAorB(ssn, dcode, cno):
        aOrB = "tbd"
        return(aOrB)

    def studentSatCoursePrereqs(ssn,dcode,cno):
        prereqsSatisfied = "tbd"
        return(prereqsSatisfied)

    def studentSatClassPrereqs(ssn,cl):
        prereqsSatisfied = "tbd"
        return(prereqsSatisfied)
#-------------------------------------------------------------------------------
# Boolean queries
#-------------------------------------------------------------------------------
    bool_a_sql_subquery = "tbd"
    bool_a_mongo_subquery = "tbd"
    boolQuery_a = all([True for table in mydb["transcript"].find({}) if ["ssn"] == 82 and ["cno"] == 530 and ["dcode"] == "CS"])
#-------------------------------------------------------------------------------
    bool_b_sql_subquery = "tbd"
    bool_b_mongo_subquery = "tbd"
    # boolQuery_b = all([True for table in mydb["transcript"].find({}) if ["name"] == "John Smith" and ["cno"] == 530 and ["dcode"] == "CS"])
#-------------------------------------------------------------------------------
    bool_c_sql_subquery = "tbd"
    bool_c_mongo_subquery = "tbd"
    boolQuery_c = "tbd"
#-------------------------------------------------------------------------------
    bool_d_sql_subquery = "tbd"
    bool_d_mongo_subquery = "tbd"
    boolQuery_d = "tbd"
#-------------------------------------------------------------------------------
    bool_e_sql_subquery = "tbd"
    bool_e_mongo_subquery = "tbd"
    boolQuery_e = "tbd"
#-------------------------------------------------------------------------------
    bool_f_sql_subquery = "tbd"
    bool_f_mongo_subquery = "tbd"
    boolQuery_f = "tbd"
#-------------------------------------------------------------------------------
    bool_g_sql_subquery = "tbd"
    bool_g_mongo_subquery = "tbd"
    boolQuery_g = "tbd"
#-------------------------------------------------------------------------------
    bool_h_sql_subquery = "tbd"
    bool_h_mongo_subquery = "tbd"
    boolQuery_h = some c in mydb["course"].find({}) if ["ssn"] == 82 and ["cno"] == 530 and ["dcode"] == "CS"])
#-------------------------------------------------------------------------------
    bool_i_sql_subquery = "tbd"
    bool_i_mongo_subquery = "tbd"
    boolQuery_i = "tbd"
#-------------------------------------------------------------------------------
    bool_j_sql_subquery = "tbd"
    bool_j_mongo_subquery = "tbd"
    boolQuery_j = "tbd"
#-------------------------------------------------------------------------------
    bool_k_sql_subquery = "tbd"
    bool_k_mongo_subquery = "tbd"
    boolQuery_k = "tbd"
#-------------------------------------------------------------------------------
    bool_l_sql_subquery = "tbd"
    bool_l_mongo_subquery = "tbd"
    boolQuery_l = "tbd"
#-------------------------------------------------------------------------------
# Data queries
#-------------------------------------------------------------------------------
    data_a_sql_subquery = "tbd"
    data_a_mongo_subquery = "tbd"
    # dataQuery_a = ([for table in mydb["transcript"].find({}) if ["ssn"] == 82 and ["cno"] == 530 and ["dcode"] == "CS"])
#-------------------------------------------------------------------------------
    data_b_sql_subquery = "tbd"
    data_b_mongo_subquery = "tbd"
    dataQuery_b = "tbd"
#-------------------------------------------------------------------------------
    data_c_sql_subquery = "tbd"
    data_c_mongo_subquery = "tbd"
    dataQuery_c = "tbd"
#-------------------------------------------------------------------------------
    data_d_sql_subquery = "tbd"
    data_d_mongo_subquery = "tbd"
    dataQuery_d = "tbd"
#-------------------------------------------------------------------------------
    data_e_sql_subquery = "tbd"
    data_e_mongo_subquery = "tbd"
    dataQuery_e = "tbd"
#-------------------------------------------------------------------------------
    data_f_sql_subquery = "tbd"
    data_f_mongo_subquery = "tbd"
    dataQuery_f = [ {"dcode": co["dcode"], "cno": co["cno"]}
        for co in mydb["course"].find({})
        if not(any([p["dcode"] == co["dcode"] and p["cno"] == co["cno"]
                for p in mydb["prereq"].find({})
            ]))
    ]
#-------------------------------------------------------------------------------
    data_g_sql_subquery = "tbd"
    data_g_mongo_subquery = "tbd"
    # dataQuery_g = [{"dcode": co["dcode"], "cno": co["cno"]}
    #     for co in mydb["course"].find({})
    #     if any([p["dcode"] == co["dcode"] and p["cno"] == co["cno"]
    #             for p in mydb["prereq"].find({})
    #     ])
    # ]
    dataQuery_h = "tbd"
#-------------------------------------------------------------------------------
    data_i_sql_subquery = "tbd"
    data_i_mongo_subquery = "tbd"
    dataQuery_i = "tbd"
#-------------------------------------------------------------------------------
    data_j_sql_subquery = "tbd"
    data_j_mongo_subquery = "tbd"
    dataQuery_j = "tbd"
#-------------------------------------------------------------------------------
    return({
        "boolQuery_a": boolQuery_a,
        # "boolQuery_b": boolQuery_b,
        "boolQuery_c": boolQuery_c,
        "boolQuery_d": boolQuery_d,
        "boolQuery_e": boolQuery_e,
        "boolQuery_f": boolQuery_f,
        "boolQuery_g": boolQuery_g,
        "boolQuery_h": boolQuery_h,
        "boolQuery_i": boolQuery_i,
        "boolQuery_j": boolQuery_j,
        "boolQuery_k": boolQuery_k,
        "boolQuery_l": boolQuery_l,
        # "dataQuery_a": dataQuery_a,
        "dataQuery_b": dataQuery_b,
        "dataQuery_c": dataQuery_c,
        "dataQuery_d": dataQuery_d,
        "dataQuery_e": dataQuery_e,
        "dataQuery_f": dataQuery_f,
        # "dataQuery_g": dataQuery_g,
        "dataQuery_h": dataQuery_h,
        "dataQuery_i": dataQuery_i,
        "dataQuery_j": dataQuery_j
    })
