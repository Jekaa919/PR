import socket

def resolve_domain_or_ip(query):#reprezentarea domeniului sau ip
    try:
        if query.replace('.', '').isdigit():  
            domain_name = socket.gethostbyaddr(query)[0]
            print("Numele de domeniu asociat cu adresa IP {} este: {}".format(query, domain_name))
        else:
            ip_addresses = socket.gethostbyname_ex(query)[2]
            print("Adresele IP asociate domeniului {} sunt:".format(query))
            for ip in ip_addresses:
                print(ip)
    except socket.gaierror:
        print("Nu am putut obține informațiile pentru domeniul sau adresa IP {}.".format(query))
    except socket.herror:
        print("Nu am putut obține numele de domeniu pentru adresa IP {}.".format(query))

def change_dns_server(ip):#actualizarea variabilei cu ip sau dns
    global dns_server
    dns_server = ip
    print(f'Serverul DNS a fost schimbat cu succes la adresa: {dns_server}')

if __name__ == "__main__":
    dns_server = socket.gethostbyname(socket.gethostname())  # Serverul DNS implicit

    while True:
        command = input("Introduceți comanda: ")
        parts = command.split()

        if parts[0] == "resolve":
            if len(parts) != 2:
                print("Comandă incorectă. Folosiți 'resolve <domain>' sau 'resolve <ip>'.")
                continue
            resolve_domain_or_ip(parts[1])

        elif parts[0] == "use" and parts[1] == "dns":
            if len(parts) != 3:
                print("Comandă incorectă. Folosiți 'use dns <ip>'.")
                continue
            change_dns_server(parts[2])

        else:
            print("Comandă necunoscută.")
