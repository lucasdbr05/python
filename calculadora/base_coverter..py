import streamlit as st


def convert_float_num(enter, base_i, base_f):
    int_part, irr_part = enter.split(".")
    n_base_int_num = convert_int_num(int_part, base_i, base_f)
    
    decimal_irr_num = 0
    for i, d in enumerate(irr_part):
        decimal_irr_num += base_dict_float[d]*(base_i**(-(i+1)))
    x =decimal_irr_num
    n_base_irr_num = ""
    while x!=0.0 and len(n_base_irr_num)<=10:
        di = x*base_f
        print(di)
        x = di%1
        d = int(di//1)
        n_base_irr_num += base_dict_int[d]
    str_ans = n_base_int_num +"."+ n_base_irr_num
    return str_ans

def convert_int_num(enter, base_i, base_f):
    init_num = int(enter, base_i)
    num = abs(init_num)
    ans = ""
    while num>=base_f:
        d = num % base_f
        num //=base_f
        ans= base_dict_int[d] + ans
    ans = base_dict_int[num] + ans
    if init_num<0:
        ans='-'+ans
    return ans


def final_num(enter=0, base_i=10, base_f=2):
    global base_dict_int, base_dict_float
    if "." in enter:
        return convert_float_num(enter, base_i, base_f)
    else: 
        return convert_int_num(enter, base_i, base_f)

    
st.title("Base Converter")
list_base= ['2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list_operations= ['*','/',"+",""]
st.header("Initials Bases")
base_i = st.selectbox("Initial Base", [list_base.index(x)+2 for x in list_base]+[36])


#if any(list_operations) in initial_num:
#    list_nums = initial_num.strip().split(list_operations) 

st.header("Finals Bases")
base_f = st.selectbox("Final Base", [list_base.index(x)+2 for x in list_base]+[36])
base_dict_int = {i:x for i,x in enumerate(["0","1"]+list_base[:base_f])}
base_dict_float = {x:i for i,x in enumerate(["0","1"]+list_base[:base_i])}

initial_num = st.text_input("Type the value you wanna convert: ")
initial_num =  initial_num.upper()

confirm_button = st.button("CALCULATE")
if confirm_button:
    try:
        st.write(final_num(initial_num, base_i, base_f))
    except ValueError:
        st.write(final_num(0, base_i, base_f))
    except TypeError:
        st.write("This value has wrong characters, please check the input.")
    except TypeError:
        st.write("This value has wrong characters, please check the input.")
    


