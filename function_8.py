def username_validity(name):
    if len(name) < 3:
      print("Invalid")
    elif len(name) > 15:
      print("Invalid")
    else:
      print("Valid")
username_validity("johnny")