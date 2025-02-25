import streamlit as st
import pandas as pd
import mysql.connector

# Establishing database connection
mycon = mysql.connector.connect(host="localhost", user="root", password="root", database="sboutique")
mycur = mycon.cursor()

# Utility Functions
def check_customer_signin(cust_id, password):
    qry = "SELECT cust_id, c_nam FROM customer WHERE cust_id = %s AND password = %s;"
    mycur.execute(qry, (cust_id, password))
    result = mycur.fetchone()
    if result:
        return result[1]  # Return the customer's first name
    return None

def check_customer_signin_id(cust_id, password):
    qry = "SELECT cust_id FROM customer WHERE cust_id = %s AND password = %s;"
    mycur.execute(qry, (cust_id, password))
    result = mycur.fetchone()
    if result:
        return result[0]  # Return the customer's first name
    return None

def check_customer_ids():
    qry = "SELECT cust_id FROM customer;"
    mycur.execute(qry)
    return [row[0] for row in mycur.fetchall()]

def check_emr(emr_name, emr_pwd):
    qry = "SELECT emr_name FROM employer WHERE emr_name = %s AND emr_pwd = %s;"
    mycur.execute(qry, (emr_name, emr_pwd))
    result = mycur.fetchone()
    if result:
        return result[0]  # Return the customer's first name
    return None

def check_eme(eme_id, eme_pwd):
    qry = "SELECT eme_id FROM employee WHERE eme_id = %s AND eme_pwd = %s;"
    mycur.execute(qry, (eme_id, eme_pwd))
    result = mycur.fetchone()
    if result:
        return result[0]  # Return the customer's first name
    return None

def view_eme():
    qry = "SELECT eme_id, eme_name, eme_post, eme_adrs, eme_adhr, eme_phno FROM employee;"
    mycur.execute(qry)
    return mycur.fetchall()

def view_shirt():
    qry = "SELECT * FROM shirt;"
    mycur.execute(qry)
    return mycur.fetchall()

def view_pant():
    qry = "SELECT * FROM pant;"
    mycur.execute(qry)
    return mycur.fetchall()

def view_shirt_er():
    qry = "SELECT cust_id, s_id, cloth_material, design FROM shirt;"
    mycur.execute(qry)
    return mycur.fetchall()

def view_pant_er():
    qry = "SELECT cust_id, pa_id, cloth_material, design FROM pant;"
    mycur.execute(qry)
    return mycur.fetchall()

def view_re_shirt():
    qry = "SELECT * FROM re_shirt;"
    mycur.execute(qry)
    return mycur.fetchall()

def view_re_pant():
    qry = "SELECT * FROM re_pant;"
    mycur.execute(qry)
    return mycur.fetchall()

def view_shirt1(cust_id):
    qry = "SELECT * FROM shirt1 where cust_id = %s;"
    mycur.execute(qry, (cust_id,))
    return mycur.fetchall()

def view_re_shirt1(cust_id):
    qry = "SELECT * FROM re_shirt1 where cust_id = %s;"
    mycur.execute(qry, (cust_id,))
    return mycur.fetchall()

def view_pant1(cust_id):
    qry = "SELECT * FROM pant1 where cust_id = %s;"
    mycur.execute(qry, (cust_id,))
    return mycur.fetchall()

def view_re_pant1(cust_id):
    qry = "SELECT * FROM re_pant1 where cust_id = %s;"
    mycur.execute(qry, (cust_id,))
    return mycur.fetchall()

def view_shirt1_e():
    qry = "SELECT * FROM shirt1;"
    mycur.execute(qry)
    return mycur.fetchall()

def view_pant1_e():
    qry = "SELECT * FROM pant1;"
    mycur.execute(qry)
    return mycur.fetchall()

def add_customer(customer_details):
    qry = "INSERT INTO customer (cust_id, c_nam, c_lnam, c_phno, c_adrs, password) VALUES (%s, %s, %s, %s, %s, %s)"
    mycur.execute(qry, customer_details)
    mycon.commit()

def add_shirt(shirt_details):
    qry="insert into shirt(cust_id, s_id, cloth_material, design,neck, chest,hip, shoulder, sleeve,bicep, wrist, sleeve_len, shirt_len) values(%s,now(3),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    mycur.execute(qry, shirt_details)
    mycon.commit()

def add_pant(pant_details):
    qry="insert into pant(cust_id,pa_id,cloth_material, design, hip_size, thigh_size, calf_size, pant_len, waist_len) values (%s,now(3),%s,%s,%s,%s,%s,%s,%s);"
    mycur.execute(qry, pant_details)
    mycon.commit()
   
#def add_emr(emr_name, emr_pwd):
 #   qry = "INSERT INTO employer (emr_name, emr_pwd) VALUES (%s, %s);"
  #  mycur.execute(qry, (emr_name, emr_pwd))
   # mycon.commit()

def add_eme(employee_details):
    qry = "INSERT INTO employee (eme_name, eme_pwd, eme_post, eme_adrs, eme_adhr, eme_phno) VALUES (%s, %s, %s, %s, %s, %s)"
    mycur.execute(qry, employee_details)
    mycon.commit()

def add_re_shirt(s_id, why):
    qry = "insert into re_shirt select * from re_shirt1 where s_id = %s;"
    mycur.execute(qry,(s_id,))
    mycon.commit()
 
    qry = "delete FROM re_shirt1 where s_id = %s;"
    mycur.execute(qry,(s_id,))
    mycon.commit()

def add_re_pant(pa_id, why):
    qry = "insert into re_pant select * from re_pant1 where pa_id = %s;"
    mycur.execute(qry,(pa_id,))
    qry = "delete FROM re_pant1 where pa_id = %s;"
    mycur.execute(qry,(pa_id,))
    mycon.commit()

def add_shirt1(s_id, why):
    qry = """INSERT INTO re_shirt (cust_id, s_id, cloth_material, design, reason, neck, chest, hip, shoulder, sleeve, bicep, wrist, sleeve_len, shirt_len)
             SELECT cust_id, s_id, cloth_material, design, %s, neck, chest, hip, shoulder, sleeve, bicep, wrist, sleeve_len, shirt_len FROM shirt1 WHERE s_id = %s;"""
    mycur.execute(qry, (why, s_id))
    mycon.commit()

    qry = "DELETE FROM shirt1 WHERE s_id = %s;"
    mycur.execute(qry, (s_id,))
    mycon.commit()

def add_pant1(pa_id, why):
    qry = """INSERT INTO re_pant
             (cust_id, pa_id, cloth_material, design, reason, hip_size, thigh_size,
              calf_size, pant_len, waist_len)
             SELECT cust_id, pa_id, cloth_material, design, %s, hip_size, thigh_size,
                    calf_size, pant_len, waist_len
             FROM pant1 WHERE pa_id = %s;"""
   
    mycur.execute(qry, (why, pa_id))
    mycon.commit()

    qry = "DELETE FROM pant1 WHERE pa_id = %s;"
    mycur.execute(qry, (pa_id,))
    mycon.commit()


def delete_shirt(s_id):
    qry = "insert into shirt1 select * from shirt where s_id = %s;"
    mycur.execute(qry,(s_id,))
    mycon.commit()
    qry = "delete FROM shirt where s_id = %s;"
    mycur.execute(qry,(s_id,))
    mycon.commit()

def delete_re_shirt(s_id):
    qry = "insert into re_shirt1 select * from re_shirt where s_id = %s;"
    mycur.execute(qry,(s_id,))
    mycon.commit()
    qry = "delete FROM re_shirt where s_id = %s;"
    mycur.execute(qry,(s_id,))
    mycon.commit()

def delete_pant(pa_id):
    qry = "insert into pant1 select * from pant where pa_id = %s;"
    mycur.execute(qry,(pa_id,))
    mycon.commit()
    qry = "delete FROM pant where pa_id = %s;"
    mycur.execute(qry,(pa_id,))
    mycon.commit()

def delete_re_pant(pa_id):
    qry = "insert into re_pant1 select * from re_pant where pa_id = %s;"
    mycur.execute(qry,(pa_id,))
    mycon.commit()
    qry = "delete FROM re_pant where pa_id = %s;"
    mycur.execute(qry,(pa_id,))
    mycon.commit()

def delete_shirt1(s_id):
    qry = "delete FROM shirt1 where s_id = %s;"
    mycur.execute(qry,(s_id,))
    mycon.commit()


def delete_pant1(pa_id):
    qry = "delete FROM pant where pa_id = %s;"
    mycur.execute(qry,(pa_id,))
    mycon.commit()

def delete_re_shirt1(s_id):
    qry = "delete FROM re_shirt1 where s_id = %s;"
    mycur.execute(qry,(s_id,))
    mycon.commit()


def delete_re_pant1(pa_id):
    qry = "delete FROM re_pant where pa_id = %s;"
    mycur.execute(qry,(pa_id,))
    mycon.commit()
   
def check_shirt():
    qry = "SELECT s_id FROM shirt;"
    mycur.execute(qry)
    return [row[0] for row in mycur.fetchall()]

def check_re_shirt():
    qry = "SELECT s_id FROM re_shirt;"
    mycur.execute(qry)
    return [row[0] for row in mycur.fetchall()]

def check_pant():
    qry = "SELECT pa_id FROM pant;"
    mycur.execute(qry)
    return [row[0] for row in mycur.fetchall()]

def check_re_pant():
    qry = "SELECT pa_id FROM re_pant;"
    mycur.execute(qry)
    return [row[0] for row in mycur.fetchall()]

def check_shirt1():
    qry = "SELECT s_id FROM shirt1;"
    mycur.execute(qry)
    return [row[0] for row in mycur.fetchall()]

def check_re_shirt1():
    qry = "SELECT s_id FROM re_shirt1;"
    mycur.execute(qry)
    return [row[0] for row in mycur.fetchall()]

def check_pant1():
    qry = "SELECT pa_id FROM pant1;"
    mycur.execute(qry)
    return [row[0] for row in mycur.fetchall()]

def check_re_pant1():
    qry = "SELECT pa_id FROM re_pant1;"
    mycur.execute(qry)
    return [row[0] for row in mycur.fetchall()]

def c_pwd(new_password, custt_id):
    qry = "UPDATE customer SET password = %s WHERE cust_id = %s;"
    mycur.execute(qry, (new_password, custt_id))
    mycon.commit()

def update_employee_password(new_passworde, eme_id):
    qry = "UPDATE employee SET eme_pwd = %s WHERE eme_id = %s;"
    mycur.execute(qry, (new_passworde, eme_id))
    mycon.commit()

def e_pwd(new_password, emr_name):
    qry = "UPDATE employer SET emr_pwd = %s WHERE emr_name = %s;"
    mycur.execute(qry, (new_password, emr_name))
    mycon.commit()

def update_employee_in_db(eme_id, eme_name, eme_post, eme_adrs, eme_adhr, eme_phno):
    qry = """UPDATE employee
             SET eme_name = %s, eme_post = %s, eme_adrs = %s, eme_adhr = %s, eme_phno = %s
             WHERE eme_id = %s"""
    mycur.execute(qry, (eme_name, eme_post, eme_adrs, eme_adhr, eme_phno, eme_id))
    mycon.commit()

# Streamlit App
st.title("Shop Boutique Management")

# Initialize session state for Sign In
if "signed_in" not in st.session_state:
    st.session_state.signed_in = False
    st.session_state.customer_name = ""
    st.session_state.cust_id = ""
    st.session_state.emr_name = ""
    st.session_state.emr_pwd = ""
    st.session_state.employer_logged_in = False
    st.session_state.employee_logged_in = False
    st.session_state.customer_logged_in = False

# Navigation
menu = st.sidebar.selectbox(
    "Select Role", ["Home", "Customer", "Employee", "Employer"]
)

if menu == "Home":
    st.write("Welcome to the Shop Boutique Management System!")
    st.write("Please select a role from the sidebar to get started.")

# Customer Section
elif menu == "Customer":
    if not st.session_state.customer_logged_in:
        action = st.radio("What would you like to do?", ["Create Account", "Sign In"])
        if action == "Create Account":
            st.subheader("Create Customer Account")
            cust_id = st.number_input("Customer ID", min_value=1, step=1)
            c_nam = st.text_input("First Name")
            c_lnam = st.text_input("Last Name")
            c_phno = st.text_input("Phone Number")
            c_adrs = st.text_area("Address")
            password = st.text_input("Password", type="password")
            submit = st.button("Create Account")
            if submit:
                if cust_id in check_customer_ids():
                    st.error("Customer ID already exists. Please create a new ID.")
                elif len(c_nam) < 3:
                    st.error("First name should contain at least 3 letters.")
                elif len(c_phno) != 10 or not c_phno.isdigit():
                    st.error("Phone number must be exactly 10 digits.")
                elif len(c_adrs) < 10:
                    st.error("Address should be at least 10 letters.")
                elif len(password) < 8:
                    st.error("Password should be at least 8 characters long.")
                else:
                    add_customer((cust_id, c_nam, c_lnam, c_phno, c_adrs, password))
                    st.success("Customer account created successfully!")

        elif action == "Sign In":
            st.subheader("Customer Sign In")
            cust_id = st.text_input("Enter Customer ID")
            password = st.text_input("Password", type="password")
            c1, c2 = st.columns(2)

            with c1:
                submit = st.button("Sign-In")
                if submit:
                    customer_name = check_customer_signin(cust_id, password)
                    cust_id = check_customer_signin_id(cust_id, password)
                    if customer_name and cust_id:
                        st.session_state.customer_logged_in = True
                        st.session_state.customer_name = customer_name
                        st.session_state.cust_id = cust_id
                        st.success("Sign In successful!")
                    else:
                        st.error("Invalid Customer ID or Password.")
           
            # Password change feature
            change_password = st.session_state.get("change_password", False)
            with c2:
                change_password_button = st.button("Change Password")
                if change_password_button:
                    st.session_state.change_password = True

                if change_password:
                    st.subheader("Change Password")
                    cust_id = st.text_input("Customer ID")
                    old_password = st.text_input("Old Password", type="password", key="old_password")
                    new_password = st.text_input("New Password", type="password", key="new_password")
                    confirm_password = st.text_input("Confirm New Password", type="password", key="confirm_password")

                    # Handle password change
                    change_pwd_button = st.button("Submit New Password")
                    if change_pwd_button:
                        if new_password == confirm_password:
                            # Verify the old password
                            if check_customer_signin(cust_id, old_password):
                                c_pwd(new_password, cust_id)  # Change password function
                                st.success("Password updated successfully!")
                                st.session_state.change_password = False  # Hide the change password form after success
                            else:
                                st.error("Incorrect old password.")
                        else:
                            st.error("New passwords do not match.")                
    else:
        st.subheader(f"Welcome, {st.session_state.customer_name}!")
        action = st.radio("Choose one among the below:", ["Order Product","Dispatched Product","Returned products"])
       
        submit1 = st.button("Log-Out")
        if submit1:
                 st.session_state.customer_logged_in = False
                 st.success("Click again to log-out")
                 
        if action =="Order Product":
            Prod = st.selectbox("Select Role", ["Shirt", "Pant"])
            if Prod == "Shirt":
                #st.image("Remo.jpg")

                st.subheader("Enter the details of your shirt:")
                cust_id = st.session_state.cust_id
                cloth_material = st.text_input("cloth material")
                design = st.text_input("shirt design in detail")
                neck = st.number_input("neck size(cm)", min_value=1.0)
                chest = st.number_input("chest size(cm)", min_value=1.0)
                hip = st.number_input("hip size(cm)", min_value=1.0)
                shoulder = st.number_input("shoulder size(cm)", min_value=1.0)
                shirt_len = st.number_input("shirt length(cm)", min_value=1.0)

                sleeve = st.radio("What kind of sleeve do you want?", ["No sleeve", "Half sleeve", "Full sleeve"])
                if sleeve == "No sleeve":
                    bicep = 0
                    sleeve_len = 0
                    wrist = 0
                elif sleeve == "Half sleeve":
                    bicep = st.number_input("bicep size(cm)", min_value=1.0)
                    sleeve_len = st.number_input("Sleeve length(cm)", min_value=1.0)
                    wrist = 0
                elif sleeve == "Full sleeve":
                    bicep = st.number_input("bicep size(cm)", min_value=1.0)
                    sleeve_len = st.number_input("Sleeve length(cm)", min_value=1.0)
                    wrist = st.number_input("Wrist size(cm)", min_value=1.0)
                submit = st.button("Place order")
                if submit:
                    if len(cloth_material) < 2:
                        st.error("enter cloth material!!!")
                    elif len(design) < 5:
                        st.error("enter at least 5 letters in design you want!!!")
                    elif neck < 1:
                        st.error("enter neck size!!!")
                    elif chest < 1:
                        st.error("enter chest size!!!")
                    elif hip < 1:
                        st.error("enter hip size!!!")
                    elif shirt_len < 1:
                        st.error("enter shirt length!!!")
                    elif shoulder < 1:
                        st.error("enter shoulder size!!!")
                    elif sleeve not in ["No sleeve", "Half sleeve", "Full sleeve"]:
                        st.error("enter the type of sleeve!!!")
                    else:
                        add_shirt((cust_id, cloth_material, design, neck, chest, hip, shoulder, sleeve, bicep, wrist, sleeve_len, shirt_len))
                        st.success("submitted successfully!")
               

            elif Prod == "Pant":
                st.subheader("Enter the details of your pant")
                cust_id = st.session_state.cust_id
                cloth_material = st.text_input("cloth material")
                design = st.text_input("pant design in detail")
                hip_size = st.number_input("Hip Size(cm)", min_value=1.0)
                thigh_size = st.number_input("Thigh size(cm)", min_value=1.0)
                waist_len = st.number_input("Waist length(cm)", min_value=1.0)
                height = st.radio("choose one among the below", ["Pant", "Shorts/Boxer"])
                if height == "Pant":
                    pant_len = st.number_input("Pant length(cm)", min_value=1.0)
                    calf_size = st.number_input("Calf size(cm)", min_value=1.0)
                elif height == "Shorts/Boxer":
                    pant_len = st.number_input("Pant length(cm)", min_value=1.0)
                    calf_size = 0
                submit = st.button("Place Order")
                if submit:
                    if len(cloth_material) < 2:
                        st.error("enter cloth material!!!")
                    elif len(design) < 5:
                        st.error("enter at least 5 letters in design you want!!!")
                    else:
                        add_pant((cust_id, cloth_material, design, hip_size, thigh_size, calf_size, pant_len, waist_len))
                        st.success("Submitted successfully!!!")
       
        elif action =="Dispatched Product":
            Prod = st.selectbox("Select Role", ["Shirt", "Pant"])
            cust_id = st.session_state.cust_id
            if Prod == "Shirt":
                st.subheader("Shirt Order Track")
                shirt1 = view_shirt1(cust_id)
                column_names = ["cust_id", "s_id", "cloth_material", "design", "neck", "chest", "hip", "shoulder", "sleeve", "bicep", "wrist", "sleeve_len", "shirt_len"]

                shirt1_df = pd.DataFrame(shirt1 , columns=column_names)
                st.dataframe(shirt1_df, height= 400, width = 1000)

                s_id = st.text_input("Enter the id of the product", placeholder="Enter only after checking the product" )
                c1,c2 = st.columns(2)
                with c1:
                    submit = st.button("Recieved order")
                    if submit:
                        if s_id in check_shirt1():
                            delete_shirt1(s_id)
                            st.success("Transaction done successfully!!!")
                        else:
                            st.error("Product ID is Invalid!!")
                with c2:
                    with st.container():
                        resubmit = st.button("Replace order")

                    if resubmit:
                        st.session_state["show_input"] = True  # Store state

                    if st.session_state.get("show_input"):
                        why = st.text_input("Why do you want to replace?", placeholder="Only valid reason!!")
                        whybut = st.button("Done")

                        if whybut:
                            if whybut and s_id in check_shirt1():
                                add_shirt1(s_id, why)
                                st.success("Transaction done successfully!!!")
                        ############################################################## To Be continued
                   
            elif Prod == "Pant":
                st.subheader("Pant Order Track")
                pant1 = view_pant1(cust_id)
                column_names = ["cust_id", "pa_id", "cloth_material", "design", "hip_size", "thigh_size", "calf", "pant_length", "waist_length"]

                pant1_df = pd.DataFrame(pant1 , columns = column_names)
                st.dataframe(pant1_df, height= 400, width = 1000)
               
                pa_id = st.text_input("Enter the id of the Received product", placeholder="Enter only after checking the product" )
                c1,c2 = st.columns(2)
                with c1:
                    submit = st.button("Recieved Product")
                    if submit:
                        if pa_id in check_pant1():
                            delete_pant1(pa_id)
                            st.success("Transaction done successfully!!!")
                        else:
                            st.error("Product ID is Invalid!!")
                with c2:
                    with st.container():
                        resubmit = st.button("Replace order")

                    if resubmit:
                        st.session_state["show_inputp"] = True  # Store state

                    if st.session_state.get("show_inputp"):
                        why = st.text_input("Why do you want to replace?", placeholder="Only valid reason!!")
                        whybut = st.button("Done")

                        if whybut:
                            if pa_id in check_pant1():
                                add_pant1(pa_id, why)
                                st.success("Transaction done successfully!!!")
       
        elif action == "Returned products":
            st.header("remo")
            Produ = st.selectbox("Select Role", ["Shirt", "Pant"])
            cust_id = st.session_state.cust_id

            if Produ == "Shirt":
                st.subheader("Shirt Order Track")
                re_shirt1 = view_re_shirt1(cust_id)
                column_names = ["cust_id", "s_id", "cloth_material", "design","reason", "neck", "chest", "hip", "shoulder", "sleeve", "bicep", "wrist", "sleeve_len", "shirt_len"]

                re_shirt1_df = pd.DataFrame(re_shirt1 ,columns = column_names)
                st.dataframe(re_shirt1_df, height= 400, width = 1000)

                s_id = st.text_input("Enter the id of the product", placeholder="Enter only after checking the product")
                c1, c2 = st.columns(2)

                with c1:
                    submit = st.button("Received order")
                    if submit:
                        if s_id in check_re_shirt1():
                            delete_re_shirt1(s_id)
                            st.success("Transaction done successfully!!!")
                        else:
                            st.error("Product ID is Invalid!!")

                with c2:
                    with st.container():
                        resubmit = st.button("Replace order")

                    if resubmit:
                        st.session_state["show_input"] = True

                    if st.session_state.get("show_input"):
                        why = st.text_input("Why do you want to replace?", placeholder="Only valid reason!!")
                        whybut = st.button("Done")

                        if whybut:
                            if s_id in check_re_shirt1():
                                add_re_shirt(s_id, why)
                                st.success("Transaction done successfully!!!")

            elif Produ == "Pant":
                st.subheader("Pant Order Track")
                re_pant1 = view_re_pant1(cust_id)
                column_names = ["cust_id", "pa_id", "cloth_material", "design","reason", "hip_size", "thigh_size", "calf", "pant_length", "waist_length"]

                re_pant1_df = pd.DataFrame(re_pant1 , columns=column_names)
                st.dataframe(re_pant1_df, height= 400, width = 1000)
               
                pa_id = st.text_input("Enter the id of the Received product", placeholder="Enter only after checking the product")
                c1, c2 = st.columns(2)
               
                with c1:
                    submit = st.button("Received Product")
                    if submit:
                        if pa_id in check_re_pant1():
                            delete_re_pant1(pa_id)
                            st.success("Transaction done successfully!!!")
                        else:
                            st.error("Product ID is Invalid!!")
               
                with c2:
                    with st.container():
                        resubmit = st.button("Replace order")
                   
                    if resubmit:
                        st.session_state["show_inputp"] = True
                   
                    if st.session_state.get("show_inputp"):
                        why = st.text_input("Why do you want to replace?", placeholder="Only valid reason!!")
                        whybut = st.button("Done")
                   
                        if whybut:
                            if pa_id in check_re_pant1():
                                add_re_pant(pa_id, why)
                                st.success("Transaction done successfully!!!")
               
                    ####Show the products which are going to process and not finished these products can be rejected by
                        #the customer and employee should give start before starting to stitch the product

                ## A list of Ready made product with description should be done to show to customer for order.

               
elif menu == "Employee":
    if not st.session_state.employee_logged_in:
        st.subheader("Employer Sign In")
        eme_id = st.text_input("Enter Your id ")
        eme_pwd = st.text_input("Password", type="password")
        c1, c2 = st.columns(2)

        with c1:
            submit = st.button("Sign In")
            if submit:
                eme_id = check_eme(eme_id, eme_pwd)
                if eme_id:
                    st.session_state.employee_logged_in = True
                    st.session_state.eme_id = eme_id
                    st.success("Sign In successful!")
                else:
                    st.error("Invalid Employee ID or Password.")

            change_passworde = st.session_state.get("change_passworde", False)

        with c2:
            change_password_buttone = st.button("Change Password")
            if change_password_buttone:
                st.session_state.change_passworde = True

            if change_passworde:
                st.subheader("Change Password")
                eme_id = st.text_input("Employee ID: ")  # Use the logged-in employee's ID
                old_passworde = st.text_input("Old Password", type="password")
                new_passworde = st.text_input("New Password", type="password")
                confirm_passworde = st.text_input("Confirm New Password", type="password")

                change_pwd_buttone = st.button("Submit New Password")
                if change_pwd_buttone:
                    if new_passworde == confirm_passworde:
                        if check_eme(eme_id, old_passworde):  # Use old password for verification
                            update_employee_password(new_passworde, eme_id)
                            st.success("Password updated successfully!")
                            st.session_state.change_passworde = False
                        else:
                            st.error("Invalid Old Password!")
                    else:
                        st.error("New passwords do not match!")
           
    else:
       
        st.subheader("Employee Section")
        submit3 = st.button("Log-Out")
        if submit3:
                    st.session_state.employee_logged_in = False
                    st.success("Click again to log-out")
        act = st.radio("Choose an action",["Order List","Delivery List","Replacement Items"])
        if act == "Order List":
            action = st.selectbox("Choose an action", ["shirt order list", "pant order list"])
           
           
            if action == "shirt order list":
                st.subheader("Shirt order List")
                shirt = view_shirt()
                column_names = ["cust_id", "s_id", "cloth_material", "Design Of the shirt", "neck", "chest", "hip", "shoulder", "sleeve", "bicep", "wrist", "sleeve_len", "shirt_len"]

                shirt_df = pd.DataFrame(shirt, columns=column_names)
                st.dataframe(shirt_df , height = 400,width = 1000)

                s_id = st.text_input("Enter the id of the finished product")
                submit = st.button("finish order")
                if submit:
                    if s_id in check_shirt():
                        delete_shirt(s_id)
                        st.success("Product List Updated Successfully!!")
                    else:
                        st.error("Product ID is Invalid!!")


            elif action == "pant order list":
                st.subheader("Pant order List")
                pant = view_pant()
                column_names = ["cust_id", "pa_id", "cloth_material", "design", "hip_size", "thigh_size", "calf", "pant_length", "waist_length"]
                pant_df = pd.DataFrame(pant, columns=column_names)
                st.dataframe(pant_df , height = 400, width = 1000)

                pa_id = st.text_input("Enter the id of the finished product")
                submit = st.button("finish order")
                if submit:
                    if pa_id in check_pant():
                        delete_pant(pa_id)
                        st.success("Product List Updated Successfully!!")
                    else:
                        st.error("Product ID is Invalid!!")
        elif act == "Delivery List":
            st.header("Delivery List")
            Prod = st.selectbox("Select Role", ["Shirt", "Pant"])
           
            if Prod == "Shirt":
                st.subheader("Shirt Order Track")
                shirt1 = view_shirt1_e()  # Assuming this returns the data
                column_names = ["cust_id", "s_id", "cloth_material", "design", "neck", "chest", "hip", "shoulder", "sleeve", "bicep", "wrist", "sleeve_len", "shirt_len"]

                # Convert the shirt1 data into a DataFrame
                shirt1_df = pd.DataFrame(shirt1, columns=column_names)

                # Display the DataFrame with scroll
                st.dataframe(shirt1_df, height=400, width=1000)  # Adjust width as needed

               
            elif Prod == "Pant":
                st.subheader("Pant Order Track")
                pant1 = view_pant1_e()
                column_names = ["cust_id", "pa_id", "cloth_material", "design", "hip_size", "thigh_size", "calf", "pant_length", "waist_length"]

                pant1_df = pd.DataFrame(pant1, columns=column_names)
               
                st.dataframe(pant1_df, height=400, width=1000)  # Adjust width as needed
               
        elif act == "Replacement Items":
            st.header("Replacement Items")
            action = st.selectbox("Choose an action", ["shirt list", "pant list"])

            if action == "shirt list":
                re_shirt = view_re_shirt()
                column_names = [
                    "cust_id", "s_id", "cloth_material", "reason", "Design Of the shirt",
                    "neck", "chest", "hip", "shoulder", "sleeve", "bicep",
                    "wrist", "sleeve_len", "shirt_len"
                ]

                if re_shirt:
                    # Convert to DataFrame for better visualization with scroll
                    import pandas as pd
                    df = pd.DataFrame(re_shirt, columns=column_names)
                   
                    # Display table with horizontal scrolling enabled
                    st.dataframe(df, height=400, width=1000)  # Adjust width as needed

                s_id = st.text_input("Enter the ID of the finished product")
                submit = st.button("Finish Order")

                if submit:
                    if s_id in check_re_shirt():
                        delete_re_shirt(s_id)
                        st.success("Product List Updated Successfully!!")
                    else:
                        st.error("Product ID is Invalid!!")
           
            elif action == "pant list":
                re_pant = view_re_pant()
                column_names = [
                    "cust_id", "pa_id", "cloth_material", "design", "reason",
                    "hip_size", "thigh_size", "calf", "pant_length", "waist_length"
                ]

                if re_pant:
                    # Convert to DataFrame for better visualization with scroll
                    import pandas as pd
                    df = pd.DataFrame(re_pant, columns=column_names)

                    # Display table with horizontal scrolling enabled
                    st.dataframe(df, height=400, width=1000)  # Adjust width as needed

                pa_id = st.text_input("Enter the ID of the finished product")
                submit = st.button("Finish Order")

                if submit:
                    if pa_id in check_re_pant():
                        delete_re_pant(pa_id)
                        st.success("Product List Updated Successfully!!")
                    else:
                        st.error("Product ID is Invalid!!")

               
           
elif menu == "Employer":
    if not st.session_state.employer_logged_in:
        st.subheader("Employer Sign In")
        emr_name = st.text_input("Enter Employee name")
        emr_pwd = st.text_input("Password", type="password")

        c1,c2=st.columns(2)
        with c1:
            submit = st.button("Sign In")

            if submit:
                emr_name = check_emr(emr_name, emr_pwd)
                if emr_name:
                    st.session_state.employer_logged_in = True
                    st.session_state.emr_name = emr_name
                    st.success("Sign In successful!")
                else:
                    st.error("Invalid Employee name or Password.")
        with c2:
            sub = st.button("Change Password")
            if sub:
                emr_name = st.text_input("Enter Employer name")
                emr_pwd = st.text_input("Current Password", type="password")
                new_password = st.text_input("New Password", type="password")
                sub1 = st.button("change password")
                if sub1:
                   
                    if emr_name == check_emr(emr_name, emr_pwd):
                        e_pwd(new_password, emr_name)
                        st.success("Password updated successfully!")
                    else:
                        st.error("Incorrect old password.")


    else:
        action = st.radio("Choose an action", ["Add Employee","Employee Details", "View Product Details"])

        submit1 = st.button("Log-Out")
        if submit1:
                 st.session_state.employer_logged_in = False
                 st.success("Click again to log-out")
                 
        if action == "Add Employee":

            eme_name    =st.text_input("name")
            eme_post    =st.text_input("Posting")
            eme_adrs    =st.text_area("Address")
            eme_adhr    =st.text_input("Adhaar")
            eme_phno    =st.text_input("phone number")
            submit      =st.button("Create account")
            if submit:
                if len(eme_name)<3:
                    st.error("Check the length of the name!!!!")
                elif len(eme_adrs)<10:
                    st.error("adrs should atleast be 10 characters!!!!")
                elif len(eme_adhr)!=12 or not eme_adhr.isdigit():
                    st.error("Aadhaar must be comprised of 12 digits only!!!")
                elif len(eme_phno) != 10 or not eme_phno.isdigit():
                    st.error("Phone number must be comprised of 10 digits only!!!")
                else:
                    add_eme((eme_name, eme_adhr, eme_post, eme_adrs, eme_adhr, eme_phno))
                    st.success("Customer account created successfully!")
           
            st.markdown("<p style='color:red; font-weight:bold;'>Default password of employee is their adhaar ID!!!</p>",unsafe_allow_html=True)

           

           
  ########change password should be given to all customer,employee,employer.'##############################


        elif action == "Employee Details":  
            st.subheader("Employee Details.")
            eme = view_eme()
           
            column_names = ["Eme ID", "Eme Name", "Posting", "Address", "Aadhaar", "Phone number"]
           
            eme_df = pd.DataFrame(eme, columns=column_names)
            st.dataframe(eme_df, height=400, width=1000)

            edited_eme_df = eme_df.copy()

            for i, row in eme_df.iterrows():
                with st.expander(f"Edit details of Employee ID {row['Eme ID']}"):
                    eme_name = st.text_input(f"Name (ID: {row['Eme ID']})", value=row['Eme Name'])
                    eme_post = st.text_input(f"Posting (ID: {row['Eme ID']})", value=row['Posting'])
                    eme_adrs = st.text_input(f"Address (ID: {row['Eme ID']})", value=row['Address'])
                    eme_adhr = st.text_input(f"Aadhaar (ID: {row['Eme ID']})", value=row['Aadhaar'])
                    eme_phno = st.text_input(f"Phone Number (ID: {row['Eme ID']})", value=row['Phone number'])
                   
                    if st.button(f"Apply Changes to Employee ID {row['Eme ID']}"):
                        update_employee_in_db(row['Eme ID'], eme_name, eme_post, eme_adrs, eme_adhr, eme_phno)
                        st.success(f"Employee ID {row['Eme ID']} details updated successfully!")
           
           
        elif action == "View Product Details":
            st.subheader("Product List")
            action = st.radio("Choose an action", ["shirt", "pant"])  
            if action == "shirt":
                st.subheader("Shirt Details")
                shirt = view_shirt_er()
                column_names = ["cust_id", "s_id", "cloth_material","design"]
               
                shirt_df = pd.DataFrame(shirt, columns=column_names)
                st.dataframe(shirt_df, height=400, width=1000)

            elif action == "pant":
                st.subheader("Pant Details")
                pant = view_pant_er()
                column_names = ["cust_id", "pa_id", "cloth_material", "design"]

                pant_df = pd.DataFrame(pant, columns=column_names)
                st.dataframe(pant_df, height=400, width=1000)
