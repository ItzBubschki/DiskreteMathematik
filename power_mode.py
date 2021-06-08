base = int(input("Enter the base num: "))
exponent = int(input("Enter the exponent: "))
modulo = int(input("enter the modulo: "))

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)

if gcd(base, modulo) == 1:
    phi = phi_func(modulo)
    print(f"Phi is {phi} and the gcd is 1.")
    new_base = base%modulo
    new_exponent = exponent%phi
    procedure = int(input(f"Do you want to continue with {new_base}(0) or with the negative {new_base-modulo}(1)? "))
    if procedure == 1:
        new_base = new_base-modulo
    multi_exponets = input(f"The current exponent is {new_exponent}. Please enter the new exponents: ")
    multi_exponents_list = []
    for element in multi_exponets.split():
        multi_exponents_list.append(int(element))
    
    recieved_results = []
    for i in range(multi_exponents_list[0]):
        result = (new_base**i)%modulo
        if not recieved_results.__contains__(result):
            recieved_results.append(result)
            print(f"{new_base}^{i} = {new_base**i} = {result}.")
        else:
            print(f"{new_base}^{i} = {result}")
            break
    overview_text = ""
    for expo in multi_exponents_list:
        overview_text += f"{new_base}^{expo} "
        if not multi_exponents_list[len(multi_exponents_list)-1] == expo:
            overview_text += "* "
    print(overview_text)

    result_text = ""
    for expo in multi_exponents_list:
        result_text += f"{(new_base**expo)%modulo} "
        if not multi_exponents_list[len(multi_exponents_list)-1] == expo:
            result_text += "* "
    print(result_text)
    print(f"Result for {base}^{exponent}%{modulo} = {new_base}^{new_exponent}%{modulo} = {(new_base**new_exponent)%modulo}")
else:
    print("The gcd is greater then 1, so the euler way doesn't work.")
    recieved_results = []
    repeting_num = -1
    for i in range(exponent):
        result = (base**i)%modulo
        if not recieved_results.__contains__(result):
            recieved_results.append(result)
            print(f"{base}^{i} = {base**i} = {result}.")
        else:
            print(f"{base}^{i} = {result}")
            repeting_num = i
            break
    if not repeting_num == -1:
        expo_mod = repeting_num-1
        new_expo = exponent%expo_mod
        print(f"{base}^{exponent} mod {expo_mod} = {base}^{new_expo} = {base**new_expo}%{modulo} = {(base**new_expo)%modulo}.")