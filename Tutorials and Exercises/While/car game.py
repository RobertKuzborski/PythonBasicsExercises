#car game

command = ""
car_started = False

while True: #command != "quit":  #was before
    command = input("> ").lower()
    if command == "start":
        if not car_started:
            print("car started")
        else:
            print("car already running")
        car_started = True
    elif command == "stop":
        if car_started:
            print("car stopped")
        else:
            print("car is not running to stop it")
        car_started = False
    elif command == "help":
        print("""
start
stop
quit
        """)
    elif command == "quit":
        break
    else:
        print("dont understand")
