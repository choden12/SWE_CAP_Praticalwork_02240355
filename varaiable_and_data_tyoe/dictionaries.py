name="Sangay Choden"
age= 18
height=1.57
is_student =True

person_info= {
    "name": name,
    "age":age,
    "is_student": is_student

}
print(person_info)

person_info["favorite_color"]="Black"
print(person_info)

try:
    print(person_info["weight"])
except KeyError as e:
    print(f"Error: {e}")

    


