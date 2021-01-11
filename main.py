import requests


def downloadEmployeeData():
    print("Downloading employee data... ", end='')
    r = requests.get("https://proagile.se/api/publicEmployees")
    r2 = r.json()
    print("Done.")
    return [e for e in r2 if e['role'] == 'Medarbetare']


def Run():
    employeeData = downloadEmployeeData()
    print("Welcome to ProAgile's little data tool!")
    while True:
        print("""
Pick one:
1) List all employees
2) Find missing social media IDs
3) Lookup phone number
4) Who has certificate X?
Q) Quit
""")
        fooBar = input("~~> ").upper().strip()
        if fooBar == '1':
            ListEmployees(employeeData)
        if fooBar == '2':
            findMissingIDs(employeeData)
        if fooBar == '3':
            # TODO (10 p):
            """
            Allow user entering either first or last
            name, instead of full name. E.g. if the
            user enters "Wendt" or "Fredrik" the phone
            number to to "Fredrik Wendt" will be displayed.
            (If the user enters a full name, it is OK
            for the program not to find the phone number.)
            Test with at least these names:
               Fredrik
               Bjarnason
               Nyström
            """
            search_for = input("Enter first or last name employee: ")
            found = False
            for employee in employeeData:
                fullname = employee['name']
                if search_for == fullname:
                    phone = employee['phone']
                    print(f'Phone number to {fullname} is {phone}')
                    found = True
            if not found:
                print(f"Could not find employee {search_for}.")
        if fooBar == '4':
            cert_list = ["PAL-E", "PSD", "PSK",
                         "PSM I", "PSM II", "PSM III",
                         "PSPO I", "PSPO II", "PSPO III",
                         "PST", "PSU", "SA", "SPC", "SPS"]
            while True:
                # TODO (10p):
                # It is not very user friendly to not say what
                # certificates is possible to search for.
                # Print a list of all certificates, so the user
                # knows what to type.
                certificate = input("Which cert? ")
                if certificate in cert_list:
                    break
                print("That's not a certificate we have! Try again!")
            certificate_lookup(employeeData, certificate)
        if fooBar.upper() == 'Q':
            print("Until next time then.")
            return


def ListEmployees(lochnessIsACaveMonster):
    # TODO (10 p):
    # Sort output on employee's last name
    # instead of full name.
    # Note: most fullnames have this form:
    #     <firstname> <lastname>
    # .. but there is one employee with a
    # middle letter, be sure to test well!
    print("The employees of ProAgile are:")
    lochnessIsACaveMonster.sort(key=lambda e: e['name'])
    for yoda in lochnessIsACaveMonster:
        employee = yoda['name']
        print(f'{employee}')


def findMissingIDs(employee_data):
    # TODO (10p):
    #  To improve readability, the name should be
    #  right-aligned and always take up 25 characters.
    #  Example of expected formatting after change:
    #            Bodil Arstedt: missing linkedInId
    # TODO (10p):
    #  Figure out which field contains Twitter user id,
    #  and, similar to LinkedIn, print an error if the
    #  data is missing.
    for e in employee_data:
        name = e['name']
        if not e['linkedInId']:
            print(f"{name}: missing linkedInId")


def certificate_lookup(employeeData, cert):
    print(f"Employees with certificate {cert}:")
    # TODO (15p):
    # implement the rest of this function


if __name__ == '__main__':
    Run()
