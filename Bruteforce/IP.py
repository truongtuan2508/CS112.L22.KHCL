def check_ip(ip): 
    ip = ip.split(".") 
    for i in ip: 
        if (len(i) > 3 or int(i) < 0 or int(i) > 255): 
            return False
        if len(i) > 1 and int(i) == 0: 
            return False
        if (len(i) > 1 and int(i) != 0 and
            i[0] == '0'): 
            return False
    return True

def output(ip):
    x = len(ip) 
    if x > 12: 
        return [] 
    new_ip = ip
    for i in range(1, x - 2): 
        for j in range(i + 1, x - 1): 
            for k in range(j + 1, x): 
                new_ip = new_ip[:k] + "." + new_ip[k:]
                new_ip = new_ip[:j] + "." + new_ip[j:]
                new_ip = new_ip[:i] + "." + new_ip[i:]
                if check_ip(new_ip): 
                    print(new_ip)                      
                new_ip = ip

ip = input()

output(ip)