# num=11
# assert num>10, "enter higher value"
#
# def test_name():
#     details={"name":"ravi", "age":25, "gender":"single"}
#
#     assert type(details["name"])==str, "change data type"
#
# def test_age():
#     details={"name":"ravi", "age":25, "gender":"single"}
#     check=details["age"]
#     assert type(details["age"])==str, "change data type"
#
# def test_frndnature():
#     nature={"anil":"loverboy","phani":"buisinessman","murthi":"helping","shivaji":"innocent"}
#     assert (nature[anil])=="loverboy", "its wrong"
#
# def test_number():
#     enternumber=int(input("enter a number "))
#     assert enternumber%2==0, "enter a even number"

# try:
#     enternumber=int(input("enter a number "))
#     enternumber%2==0
#     print("its even number")
# except:
#     print("thats odd")
# finally:
#     print("Done")
#
#
#
# try:
#     enternumber=int(input("enter a number "))
#     assert enternumber%2==0
#     print("its even number")
# except:
#     print("thats odd")
# finally:
#     print("Done")

def test_dvsn():
    num1=int(input("enter a number"))
    num2=int(input("enter a number"))
    assert print("div=",num1/num2, "addn=",num1+num2,"mult=",num1*num2), "number should not be zero"
