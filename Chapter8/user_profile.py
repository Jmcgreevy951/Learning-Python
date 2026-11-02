def build_profile(f_name, l_name, **details): #Note: Kwargs (**) store a pair of key values (eg, age=24) in a dictionary, also defined through function call
    full_name = f'{f_name} {l_name}'

    print(f"\nHere are details about {full_name}:")
    print(f"Name: {f_name}")
    print(f"Surname: {l_name}")

    for detail in details:
        print(f"{detail.title()}: {details[detail]}")