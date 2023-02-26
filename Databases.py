SELECT = "SELECT"
UPDATE = "UPDATE"
DELETE = "DELETE"
INSERT = "INSERT"
CREATE = "CREATE"
Remember_Me = {
    'database': "LoginDetails.db",
    'table': "Remember_Me",
    'columns': ["Username", "Status","pc_name"]
}
LoginTable = {
    'database': "LoginDetails.db",
    'table': "login_table",
    'columns': ["Full_Name","Contact","Email_Address","Account_Type","ID","Address","Username","Password"]
}
assign_IDs_Table = {
    'database': "LoginDetails.db",
    'table': "IDs_Table",
    'columns': ["ID","Username"]
}
Diary_no_table = {
    'database': "BillingDetails.db",
    'table': "Diary_no",
    'columns': ["Title","Diary_no"]
}

# 3 Tables for Bills 
# 1) To save just main details of a Bill
# 2) To save details of each Bill including Item pricing etc.
# 3) To save details of Printed document of a bill 
Bills_Table = {
    'database': "BillingDetails.db",
    'table': "Bill_Table",
    'columns': ["Date","Diary_No","Bill_Subject","Department","Firm_Name","Comp_Firm1","Comp_Firm2","Bill_Type","Group_ID","Bill_Limit","Status","Cheque_No"]
}

Bill_Items_Table = {
    'database': "BillingDetails.db",
    'table': "Bill_Details_Table",
    'columns': ["Diary_No","Item_Name","Specs","Qty","Rate","Tax","Comp1_amount","Comp2_Amount","Purchase_rate"]
}
Bill_Prints_Table = {
    'database': "BillingDetails.db",
    'table': "Bill_Prints_Table",
    'columns': ["Diary_No","Prints"]
}

# Lists Table
Item_List_Table = {
    'database': "BillingDetails.db",
    'table': "items_list",
    'columns': ["Item_name","Specs","Rate","Unit","Type"]
}
specs_List_Table = {
    'database': "BillingDetails.db",
    'table': "specs_list",
    'columns': ["Specifications"]
}
Depart_List_Table = {
    'database': "BillingDetails.db",
    'table': "Depart_List_Table",
    'columns': ["Department_List"]
}
Subject_List_Table = {
    'database': "BillingDetails.db",
    'table': "Subject_List_Table",
    'columns': ["Subject_List"]
}
Firms_List_Table = {
    'database': "BillingDetails.db",
    'table': "Firm_List_Table",
    'columns': ["Firm_List"]
}
Unit_List_Table = {
    'database': "BillingDetails.db",
    'table': "Unit_List_Table",
    'columns': ["Unit_List"]
}
pdf_setting = {
    'database': "Settings.db",
    'table': "pdf_setting_table",
    'columns': ["Sr","Json_Data"]
}
files_path = {
    'database': "Settings.db",
    'table': "files_path_table",
    'columns': ["Title","Path"]
}
tables = [Bills_Table,Bill_Items_Table,Bill_Prints_Table,Item_List_Table,Firms_List_Table,Subject_List_Table,
    Depart_List_Table,Unit_List_Table,specs_List_Table,pdf_setting,assign_IDs_Table,LoginTable,Diary_no_table,Remember_Me,files_path]

